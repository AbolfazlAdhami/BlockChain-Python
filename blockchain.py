#   Initializing our (empty) blockchain list
MINING_REWARD = 10
genesis_block = {
    'pervious_hash': '',
    'index': 0,
    'transactions':  []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Abolfazl'
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
    tx_sender = [[tx['amount'] for tx in block['transactions']if tx['sender'] == participant]
                 for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount']for tx in block['transactions'] if tx['sender'] == participant]
                    for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def get_last_blockchain_value():
    """Return the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    if sender_balance >= transaction['amount']:
        return True
    else:
        return False


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
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_tranaction = {
        'sender': 'MININNG', 'recipinet': owner, amount: MINING_REWARD
    }
    open_transactions.append(reward_tranaction)
    block = {
        'pervious_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)
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
    """ Verify the current blockchian and return True if it's valid,False othervise  """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['pervious_hash'] != hash_block(blockchain[index-1]):
            return False
    return True


waitin_for_input = True

#  A While Loop for User input interface
#  It's a  loop exsit once waiting_for_input becomes False oe wehen break is called
while waitin_for_input:
    print('Please choose :')
    print('1: Add a new transaction value.')
    print('2: Mine a new Block.')
    print('3: Output the Blockchain Blocks.')
    print('4: Output participants')
    print('h: Manipulate th chain')
    print('q: Quit')
    user_choise = get_user_choise()
    if user_choise == '1':
        tx_data = get_transaction_value()
        # Add the tx_data to opne transaction
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
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
    print("Balanced", get_balance('Abolfazl'))


print('Done!')
