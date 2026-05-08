from ingestion.services.block_reader import get_latest_block
from signals.engine import process_tx, detect_signals
from storage.db import init_db


def run():
    init_db()

    block = get_latest_block()

    for tx in block["transactions"]:
        process_tx(tx)

    signals = detect_signals()

    print("\nSIGNALS:")
    for s in signals:
        print(s)


if __name__ == "__main__":
    run()