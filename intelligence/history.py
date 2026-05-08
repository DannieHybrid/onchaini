from collections import defaultdict
import time

from ingestion.services.block_reader import get_block_by_number


historical_stats = defaultdict(lambda: {
    "tx_count": 0,
    "volume": 0,
    "blocks": set()
})


def process_blocks(start_block, end_block):

    for block_num in range(start_block, end_block + 1):

        try:
            print(f"Processing block {block_num}")

            block = get_block_by_number(block_num)

            for tx in block["transactions"]:

                wallet = tx["from"]
                value = tx["value"]

                historical_stats[wallet]["tx_count"] += 1
                historical_stats[wallet]["volume"] += value
                historical_stats[wallet]["blocks"].add(block_num)

            # avoid RPC rate limits
            time.sleep(0.25)

        except Exception as e:
            print(f"Failed block {block_num}: {e}")


def get_ranked_wallets(limit=10):

    ranked = sorted(
        historical_stats.items(),
        key=lambda x: (
            len(x[1]["blocks"]),
            x[1]["volume"]
        ),
        reverse=True
    )

    return ranked[:limit]