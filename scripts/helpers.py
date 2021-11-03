from brownie import accounts, config, SimpleMessage, network

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local']
is_local_environments = network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS

def get_account():
    if is_local_environments:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def read_contract():
    simple_message = SimpleMessage[-1]
    print(simple_message.retrieve())
