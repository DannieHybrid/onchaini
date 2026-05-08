EXCHANGE_WALLETS = {
    "Binance": [
        "0x28C6c06298d514Db089934071355E5743bf21d60"
    ],
    "Coinbase": [
        "0x71660c4005BA85c37cCe4B0fbb1de10F3C9cac6d"
    ]
}


exchange_stats = {
    "Binance": {
        "inflow": 0,
        "outflow": 0
    },
    "Coinbase": {
        "inflow": 0,
        "outflow": 0
    }
}


def process_exchange_tx(tx):

    sender = tx["from"]
    receiver = tx["to"]
    value = tx["value"]

    for exchange, wallets in EXCHANGE_WALLETS.items():

        if sender in wallets:
            exchange_stats[exchange]["outflow"] += value

        if receiver in wallets:
            exchange_stats[exchange]["inflow"] += value


def get_exchange_flows():
    return exchange_stats