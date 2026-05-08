from ingestion.services.block_reader import get_latest_block
from ingestion.services.tx_parser import parse_transaction

def run():
    block = get_latest_block()

    print("Block:", block["number"])
    print("Tx count:", len(block["transactions"]))

    sample_tx = block["transactions"][0]
    parsed = parse_transaction(sample_tx, block["number"])

    print("\nSample parsed tx:")
    print(parsed)


if __name__ == "__main__":
    run()