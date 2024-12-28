import functools

# The reward we give to miners (for creating a new Block)
MINING_REWARD = 10
# Out Structur for the Blockchain
genesis_block = {
    'pervious_hash': '',
    'index': 0,
    'transactions':  []
}

#   Initializing our (empty) blockchain list
blockchain = [genesis_block]
# Unhandled transaction
open_transactions = []
#   We are the owner of the blockchain node, hence this is our identifier (e.g. for sending coins)
owner = 'Abolfazl'
#   Registered participants: Ourself + other people sending / reciving coins
participants = {'Abolfazl'}


def hash_block(block):
    """ retunr the hash string for minning a new block
    Args:
        block : last block of a blockchain list
    Returns:
        hash: join all block key with -
    """
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    """Calculate and return the balanced for ad participant.

    Args:
        participant (String): The person for whom to calculate the balanced

    Returns:
        Number: Differnt between received and send amount
    """
    #  Fetch a list of all sent coin amount for the given person (empty lists are returned if the person was NOT the sender)
    #  This fetches sent amounts of transactions that were already included in blocks of the blockchain
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]

    # Fetch a list of all sent coins amounts for the given person
    # This fetches sent amount of open transctions (to avoid double spending)
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    # Calculate the total amount of coins sent
    amount_sent = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum+tx_amt[0] if len(tx_amt) > 0 else 0, tx_sender, 0)
    # This is fetches received coin amounts of transactions that were already included in block of the blockchain
    # we ignore open transactions here because you shouldn't be able to spend coins before the transaxtion was confirmed + included in a block
    tx_recipient = [[tx['amount']for tx in block['transactions'] if tx['sender'] == participant]
                    for block in blockchain]
    amount_received = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum+tx_amt[0]if len(tx_amt) > 0 else 0, tx_recipient, 0)
    #  Return the totla balance
    return amount_received - amount_sent


def get_last_blockchain_value():
    """Return the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    """Verify a transaction by checking whether the sender has sufficient coins.

    Args:
        transaction: The transaction that should be verified
    """
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


# This fucntion accepts two arguments.
# One required one  (transaction_amout), and one  optional one (last_transaction)
# the optional one is becuse it has a default value => [1]
def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new Value aw well as the last blockchain value to the blockchian
    Args:
        :sender: The sender of the coins
        :recipient: The recipient of the coins
        :amount: The amount of coins send with the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender, 'recipient': recipient, 'amount': amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        print(open_transactions)
        return True

    return False


def mine_block():
    """Create a new block and add opne transaction to it"""
    # Fetch the currently last block of the blockchain
    last_block = blockchain[-1]
    # Hash the last block (=>to be able to compare it to the stored hash value)
    hashed_block = hash_block(last_block)
    # Miners should be rewarded, so let's create a reward transaction
    reward_tranaction = {
        'sender': 'MININNG', 'recipinet': owner, 'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_tranaction)
    block = {
        'pervious_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions
    }
    blockchain.append(block)
    print(blockchain)
    return True


def get_transaction_value():
    """ Return the input of the user (a new transaction amount) as a Float. """
    # get user input and Transform it from a string to a float and store it in user input
    tx_recipinet = input("Enter of the Recipient of Trnasaction:")
    tx_anount = float(input("Please Enter Amount Transaction : "))
    return (tx_recipinet, tx_anount)


def get_user_choise():
    """Prompt the user for its choice and return it."""
    user_input = input("Your Choice:  ")
    return user_input


def print_blockchain_elements():
    """Output all blocks of the block"""
    # Outputing blocks to the console
    for block in blockchain:
        print('\nOutputing Blocks')
        print(block)

    print('-'*20)


def verify_chain():
    '''Verify the current blockchain and return True if it's valid , False otherwise'''
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['pervious_hash'] != hash_block(blockchain[index-1]):
            return False
    return True


def verify_transctions():
    return all([verify_transaction(tx) for tx in open_transactions])


waitin_for_input = True
#  A While Loop for User input interface
#  It's a  loop exsit once waiting_for_input becomes False oe wehen break is called
while waitin_for_input:
    print('Please choose :')
    print('1: Add a new transaction value.')
    print('2: Mine a new Block.')
    print('3: Output the Blockchain Blocks.')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('h: Manipulate th chain')
    print('q: Quit')
    user_choise = get_user_choise()
    if user_choise == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add new transaction to the blockchain
        if add_transaction(recipient, amount=amount):
            print("Transaction Successfully Added")
        else:
            print("Transaction Failed")
    elif user_choise == '2':
        if mine_block():
            open_transactions = []
    elif user_choise == '3':
        print_blockchain_elements()
    elif user_choise == 'h':
        # Make sure you don't try to 'Hack' the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = {
                'pervious_hash': '',
                'index': 0,
                'transactions':  [
                    {'sender': 'Chris', 'recipient': 'Max', 'amount': 100}
                ]
            }
    elif user_choise == '4':
        print(participants)
    elif user_choise == '5':
        if verify_transctions():
            print("Alltransactions Valid")
        else:
            print("There are invalid transactions")
    elif user_choise == 'q':
        # This will load to the loop to exist becuse it's runnig condition becomes False
        waitin_for_input = False
    else:
        print('Input was invalid, please pick a value from the list.')
    if not verify_chain():
        print_blockchain_elements()
        print("Invalid Blockchain!")
        # Break out of loop
        break
    print("Balanced of {}: {:6.2f}".format(owner, get_balance(owner)))


print('Done!')
