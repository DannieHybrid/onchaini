from collections import defaultdict
from storage.db import get_connection

wallet_state = defaultdict(lambda: {
    "inflow": 0,
    "outflow": 0,
    "tx_count": 0
})


def process_tx(tx):
    sender = tx["from"]
    receiver = tx["to"]
    value = tx["value"]
    block = tx.get("block", 0)

    wallet_state[sender]["outflow"] += value
    wallet_state[sender]["tx_count"] += 1

    if receiver:
        wallet_state[receiver]["inflow"] += value
        wallet_state[receiver]["tx_count"] += 1


def detect_signals():
    signals = []

    for wallet, data in wallet_state.items():

        if data["inflow"] > data["outflow"] * 2:
            signals.append({
                "type": "ACCUMULATION",
                "wallet": wallet,
                "score": data["inflow"]
            })

        if data["outflow"] > data["inflow"] * 2:
            signals.append({
                "type": "DISTRIBUTION",
                "wallet": wallet,
                "score": data["outflow"]
            })

    # persist signals
    conn = get_connection()
    cursor = conn.cursor()

    for s in signals:
        cursor.execute("""
            INSERT INTO signals (wallet, signal_type, score, block_number)
            VALUES (?, ?, ?, ?)
        """, (
            s["wallet"],
            s["type"],
            s["score"],
            0
        ))

    conn.commit()
    conn.close()

    return signals