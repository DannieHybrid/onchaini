from collections import defaultdict
from storage.db import get_connection

WHALE_THRESHOLD = 100 * 10**18  # 100 ETH


wallet_stats = defaultdict(lambda: {
    "tx_count": 0,
    "total_value": 0,
    "large_txs": 0
})


def process_transaction(tx):
    sender = tx["from"]
    value = tx["value"]
    block = tx.get("block", 0)
    tx_hash = tx["hash"]

    # in-memory stats
    wallet_stats[sender]["tx_count"] += 1
    wallet_stats[sender]["total_value"] += value

    if value >= WHALE_THRESHOLD:
        wallet_stats[sender]["large_txs"] += 1

    # persist to DB
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO wallet_activity (wallet, tx_hash, block_number, value)
        VALUES (?, ?, ?, ?)
    """, (
        sender,
        tx_hash,
        block,
        value
    ))

    conn.commit()
    conn.close()


def get_top_wallets(limit=10):
    return sorted(
        wallet_stats.items(),
        key=lambda x: x[1]["total_value"],
        reverse=True
    )[:limit]