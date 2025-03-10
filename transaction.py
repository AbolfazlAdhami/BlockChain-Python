from collections import OrderedDict
from printable import Printable


class Transaction(Printable):
    """ A transaction which can be added a block in the blockchain.

    Attributes:
        :sender : The sender of the coins.
        :recipient : The recipient of the coins.
        :amount : The amount of coins 
    """

    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_ordered_dict(self):
        """Converts this transaction into a (hashable) OrderedDict."""
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])
