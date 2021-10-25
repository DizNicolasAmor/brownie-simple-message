from brownie import accounts, config, SimpleMessage

def main():
    # How to import accounts
    # option 1: take it from env variables
    # acount = accounts.add(os.getenv("PRIVATE_KEY"))

    # option 2: take it from variables from brownie-config.yaml
    # acount = accounts.add(config["wallets"]["from_key"])

    # option 3: use native accounts from brownie
    account = accounts[0]
    simple_message = SimpleMessage.deploy({ "from": account })
