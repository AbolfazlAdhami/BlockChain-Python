#
blockchain = []


def print_blockchain_elements():
    """Output all blocks of the block"""
    # Outputing blocks to the console
    for block in blockchain:
        print('Outputing Blocks')
        print(block)
    else:
        print('-'*20)


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transion_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transion_amount])


def get_user_input():
    user_input = input("Please Enter Amount Transaction : ")
    return float(user_input)


def get_user_choise():
    return


waitin_for_input = True


#  A While Loop for User input interface
#
while waitin_for_input:
    print('Please choose :')
    print('1: Add a new transaction value.')
    print('2: Output the Blockchain Blocks.')
    print('h: Manipulate th chain')
    print('q: Quit')
    user_choise = get_user_choise()
    if user_choise == 1:
        tx_anount = 1
    else:
        print('Input was invalid, please pick a value from the list.')
