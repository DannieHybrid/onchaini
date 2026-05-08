from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv(override=True)

RPC_URL = os.getenv("RPC_URL")
print("RPC:", RPC_URL)

w3 = Web3(Web3.HTTPProvider(RPC_URL))


def get_latest_block():
    return w3.eth.get_block("latest", full_transactions=True)


def get_block_by_number(number: int):
    return w3.eth.get_block(number, full_transactions=True)