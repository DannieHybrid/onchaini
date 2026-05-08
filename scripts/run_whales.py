from ingestion.services.block_reader import get_latest_block
from analytics.whales import process_transaction, get_top_wallets
from storage.db import init_db


def run():
    init_db()

    block = get_latest_block()

    for tx in block["transactions"]:
        process_transaction(tx)

    whales = get_top_wallets()

    print("\nTOP WALLETS:")
    for wallet, stats in whales:
        print(wallet, stats)


if __name__ == "__main__":
    run()