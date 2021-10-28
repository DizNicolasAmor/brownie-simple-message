from brownie import accounts, config, SimpleMessage, network

def main():
    account = get_account()
    initial_message = 'Hello world!'
    simple_message = SimpleMessage.deploy(initial_message, { "from": account })

def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

