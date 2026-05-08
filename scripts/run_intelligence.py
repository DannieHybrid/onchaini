from ingestion.services.block_reader import get_latest_block
from intelligence.smart_money import update_wallet, get_all_labels
from storage.db import init_db


def run():
    init_db()

    block = get_latest_block()

    for tx in block["transactions"]:
        update_wallet(tx, block["number"])

    labels = get_all_labels()

    print("\nWALLET CLASSIFICATION:")
    for wallet, label in list(labels.items())[:10]:
        print(wallet, label)


if __name__ == "__main__":
    run()