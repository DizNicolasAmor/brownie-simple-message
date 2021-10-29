from brownie import accounts, config, SimpleMessage, network

def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def read_contract():
    simple_message = SimpleMessage[-1]
    print(simple_message.retrieve())
