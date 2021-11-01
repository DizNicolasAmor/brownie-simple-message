from brownie import SimpleMessage
from scripts.helpers import get_account

def main():
    account = get_account()
    initial_message = 'Hello world!'
    simple_message = SimpleMessage.deploy(initial_message, { "from": account }, publish_source=True)
