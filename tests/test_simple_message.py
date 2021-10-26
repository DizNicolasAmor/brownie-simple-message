from brownie import SimpleMessage, accounts

def test_deploy():
    account = accounts[0]
    initial_message = "Hello world"
    simple_message = SimpleMessage.deploy(initial_message, { "from": account })
    initial_message_from_blockchain = simple_message.getMessage()

    assert initial_message_from_blockchain == initial_message

def test_updating_message():
    account = accounts[0]
    initial_message = "Hello world"
    simple_message = SimpleMessage.deploy(initial_message, { "from": account })

    updated_message = "updated message"
    simple_message.setMessage(updated_message )

    assert simple_message.getMessage() == updated_message
