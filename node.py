from uuid import uuid4

from blockchain import Blockchain
from utility.verifiaction import Verification


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

    def print_blockchain_elements(self):
        """ Output all blocks of the blockchain. """
        # Output the blockchain list to the console
        for block in self.blockchain.chain:
            print('Outputting Block')
            print(block)
        else:
            print('-' * 20)

    def listen_for_input(self):
        """Starts the node and waits for user input."""
        waiting_for_input = True

        # A while loop for the user input interface
        # It's a loop that exits once waiting_for_input becomes False or when break is called
        while waiting_for_input:
            print('Please choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Check transaction validity')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                # Add the transaction amount to the blockchain
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                # This will lead to the loop to exist because it's running condition becomes False
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('Invalid blockchain!')
                # Break out of the loop
                break
            print('Balance of {}: {:6.2f}'.format(
                self.id, self.blockchain.get_balance()))
        else:
            print('User left!')

        print('Done!')


node = Node()
node.listen_for_input()
