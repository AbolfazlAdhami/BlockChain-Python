#   Initializing our (empty) blockchain list
blockchain = []


def get_last_blockchain_value():
    """Return the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# This fucntion accepts two arguments.
# One required one  (transaction_amout), and one  optional one (last_transaction)
# the optional one is becuse it has a default value => [1]
def add_transaction(transaction_amout, last_transaction=[1]):
    """ Append a new Value aw well as the last blockchain value to the blockchian

    Args:
        transaction_amout : the amount should be added 
        last_transaction (list, optional): _description_. Defaults to [1].
    """
    if last_transaction == None:
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amout])
    print(blockchain)


def get_transaction_value():
    """ Return the input of the user (a new transaction amount) as a Float. """
    # get user input and Transform it from a string to a float and store it in user input
    user_input = input("Please Enter Amount Transaction : ")
    return float(user_input)


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
    is_valid = True
    for block_idnex in range(len(blockchain)):
        if block_idnex == 0:
            # If we're checking the grist block, we should skip the iteration (since there's no pervios block)
            continue
        # check the pervious block (the entire one) vs the frist of the current block
        elif blockchain[block_idnex][0] == blockchain[block_idnex-1]:
            is_valid = True
        else:
            is_valid = False

    return is_valid


waitin_for_input = True


#  A While Loop for User input interface
#  It's a  loop exsit once waiting_for_input becomes False oe wehen break is called
while waitin_for_input:
    print('Please choose :')
    print('1: Add a new transaction value.')
    print('2: Output the Blockchain Blocks.')
    print('h: Manipulate th chain')
    print('q: Quit')
    user_choise = get_user_choise()
    if user_choise == '1':
        tx_anount = get_transaction_value()
        add_transaction(tx_anount, get_last_blockchain_value())
    elif user_choise == '2':
        print_blockchain_elements()
    elif user_choise == 'h':
        # Make sure you don't try to 'Hack' the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = [2]
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


print('Done!')
