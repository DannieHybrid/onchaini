from ingestion.services.block_reader import get_latest_block
from analytics.exchange_flows import (
    process_exchange_tx,
    get_exchange_flows
)


def run():

    block = get_latest_block()

    for tx in block["transactions"]:
        process_exchange_tx(tx)

    flows = get_exchange_flows()

    print("\nEXCHANGE FLOWS:\n")

    for exchange, stats in flows.items():
        print(exchange)
        print(stats)
        print()


if __name__ == "__main__":
    run()