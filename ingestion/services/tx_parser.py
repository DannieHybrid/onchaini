def parse_transaction(tx, block_number):
    return {
        "hash": tx["hash"].hex() if not isinstance(tx["hash"], str) else tx["hash"],
        "from": tx["from"],
        "to": tx["to"],
        "value": tx["value"],
        "block": block_number,
        "gas": tx["gas"],
        "gas_price": tx["gasPrice"],
    }