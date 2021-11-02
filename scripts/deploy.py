from brownie import config, network, SimpleMessage
from scripts.helpers import get_account

def main():
    account = get_account()
    initial_message = 'Hello world!'
    must_publish = config["networks"][network.show_active()].get("verify")

    simple_message = SimpleMessage.deploy(
        initial_message,
        { "from": account },
        publish_source=must_publish
    )
