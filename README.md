# brownie-simple-message

This is a dApp built with brownie. The user can get a message from the blockchain and update it.

## Requirements:

- brownie: https://github.com/eth-brownie/brownie
- yarn: https://classic.yarnpkg.com/en/
- ganache-cli: https://www.npmjs.com/package/ganache-cli

## Setup

```
   $ brownie compile

   $ brownie run scripts/deploy.py
```

## Tests

### How to test locally

```
# run all tests:
$ brownie test

# run only one test, for example test_updating_message:
$ brownie test -k test_updating_message

# run post mortem tests to debug error:
$ brownie test -pdb

# run all tests and show more detailed info:
$ brownie test -s
```

### How to deploy to a testnet

1. Create an account, for example using MetaMask.
1. Switch into a testnet.
1. Fund your account, for example using a Faucet.
1. Signup in Infura (https://infura.io/) and create a project. Call it "brownie-simple-message".
1. Inside that project, select the testnet.
1. Save the PROJECT_ID and the ENDPOINTS values in the .env file

Documentation example: https://chain.link/bootcamp/brownie-setup-instructions

In **brownie**, you can select the network using the `--network` flag and the network name, for example `kovan`:

`brownie run scripts/deploy.py --network kovan`
