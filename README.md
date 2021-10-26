# brownie-simple-message

This is a dApp built with brownie. The user can get a message from the blockchain and update it.

## Requirements:

- brownie: https://github.com/eth-brownie/brownie
- yarn: https://classic.yarnpkg.com/en/
- ganache-cli: https://www.npmjs.com/package/ganache-cli

## Setup

```
   $ brownie compile

   $ brownie run scripts/deploy_hello_world.py
```

## How to run tests

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
