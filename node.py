from uuid import uuid4

from blockchain import Blockchain
from verifiaction import Verification


class Node:
    """The Node runs the local blockchain instance.

    Attributes:
        id: the id of the node 
        blockcahin: The blockchain which is run by this node.
    """

    def __init__(self):
        self.id = 'Abolfazl'
        self.blockchain = Blockchain(self.id)

    def get_transaction_value(self):
        """ Returna the input of the user (a new transactions amount) as a float"""
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount = float(input('Your transactions amount please: '))
        return tx_recipient, tx_amount

    def get_user_choice(self):
        """"Prompt the user for its choice and return it."""
        user_input = input('Your Choice: ')
        return user_input

    def print_block_chain_elements(self):
        """ Outputting the node and waits for user input. """
        for block in self.blockchain.chain:
            print("Outputting Block")
            print(block)
        else:
            print('-'*20)

    def listen_for_input(self):
        """Start the node and wait for user input"""
        waiting_for_input = True

        # A while loop for the user input inferface
        # It's a loop that exits once waiting_for_input ot when break is called
        while waiting_for_input:
            print('Please choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Output participants')
            print('5: Check transaction validity')
            print('h: Manipulate the chain')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                # Add the transaction amount to the blockchain
                if self.blockchain.add_transaction(recipient, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(open_transactions)
            elif user_choice == '2':
                if mine_block():
                    open_transactions = []
                save_file(blockchain, open_transactions)
            elif user_choice == '3':
                print_blockchain_elements()
            elif user_choice == '4':
                print(participants)
            elif user_choice == '5':
                if verify_transactions():
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'h':
                # Make sure that you don't try to "hack" the blockchain if it's empty
                if len(blockchain) >= 1:
                    blockchain[0] = {
                        'previous_hash': '',
                        'index': 0,
                        'transactions': [{'sender': 'Chris', 'recipient': 'Abolfazl', 'amount': 100.0}]
                    }
            elif user_choice == 'q':
                # This will lead to the loop to exist because it's running condition becomes False
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
            if not verify_chain():
                print_blockchain_elements()
                print('Invalid blockchain!')
                # Break out of the loop
                break
            print('Balance of {}: {:6.2f}'.format(
                'Abolfazl', get_balance('Abolfazl')))
        else:
            print('User left!')

        print('Done!')
