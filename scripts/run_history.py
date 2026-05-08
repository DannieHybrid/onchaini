from ingestion.services.block_reader import get_latest_block
from intelligence.history import (
    process_blocks,
    get_ranked_wallets
)
from storage.db import init_db


def run():

    init_db()

    latest_block = get_latest_block()["number"]

    process_blocks(
        latest_block - 5,
        latest_block
    )

    wallets = get_ranked_wallets()

    print("\nTOP HISTORICAL WALLETS:\n")

    for wallet, stats in wallets:
        print(wallet)
        print(stats)
        print()


if __name__ == "__main__":
    run()