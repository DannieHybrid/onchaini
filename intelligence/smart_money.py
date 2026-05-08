from collections import defaultdict

wallet_history = defaultdict(lambda: {
    "inflow": 0,
    "outflow": 0,
    "tx_count": 0,
    "blocks_seen": set()
})


def update_wallet(tx, block_number):
    wallet = tx["from"]
    value = tx["value"]

    wallet_history[wallet]["outflow"] += value
    wallet_history[wallet]["tx_count"] += 1
    wallet_history[wallet]["blocks_seen"].add(block_number)


def classify_wallet(wallet):
    data = wallet_history[wallet]

    activity = len(data["blocks_seen"])
    volume = data["inflow"] + data["outflow"]

    if volume > 500 * 10**18:
        return "WHALE"

    if activity > 10 and volume > 100 * 10**18:
        return "SMART_MONEY"

    if activity > 20:
        return "BOT"

    return "RETAIL"


def get_all_labels():
    return {
        w: classify_wallet(w)
        for w in wallet_history
    }