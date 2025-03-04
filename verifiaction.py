from hash_util import hash_string_256


class Verification:
    '''A helper class which offer varios static and class-based verfication and validation methods.'''
    @staticmethod
    def valid_proof(transactions, last_hash, proof):
        """_summary_

        Args:
            transactions: The transactions of the block for which the proof is created.
            last_hash: The previos block's hash which will be stored in the currrent block.
            proof: the proof number we're testing
        """

        # Create a string with all the hash inputs
        guess = (str())
        # Hash the string
        # IMPORTANT : This is NOT the same hash as will be stored in the previos_hash. It's a not a block's hash. It's only used for proof-of-work algorithm.
        guess_hash = hash_string_256(guess)
        # Only a hash (wich is based on the above inputs) which starts with tow 0s is treated as valid
        # This condition is of  course defined by you. You could also require 10 leading 0s - this would take signficantly longer (and this allows you to control the speed at which new blocks can be added)
        return guess_hash[0:2] == '00'

    @classmethod
    def verify_chain(cls, blockchain):
        """ Verify the current blockchain and return True if It's valid,False otherwise."""
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue

    @staticmethod
    def verify_transaction(transaction, get_balance):
        """Verify a transaction by checking whether the sender has sufficient coins.

        Args:
            transaction : THe transactions that should be verified.
        """
        sender_balance = get_balance()
        return sender_balance >= transaction.amount

    @classmethod
    def verify_transactions(cls, open_transactions, get_balance):
        '''Verifies all open transactions.'''
        return all([cls.verify_transaction])
