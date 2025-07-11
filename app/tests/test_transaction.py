import unittest
from collections import OrderedDict
from ..transaction import Transaction


class TransactionTestCase(unittest.TestCase):
    def setUp(self):
        self.sender = "sender_public_key"
        self.recipient = "recipient_public_key"
        self.signature = "some_signature"
        self.amount = 50.0
        self.transaction = Transaction(
            self.sender, self.recipient, self.signature, self.amount)

    def test_transaction_initialization(self):
        self.assertEqual(self.transaction.sender, self.sender)
        self.assertEqual(self.transaction.recipient, self.recipient)
        self.assertEqual(self.transaction.signature, self.signature)
        self.assertEqual(self.transaction.amount, self.amount)

    def test_to_ordered_dict(self):
        expected_dict = OrderedDict([
            ('sender', self.sender),
            ('recipient', self.recipient),
            ('amount', self.amount)
        ])
        self.assertEqual(self.transaction.to_ordered_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
