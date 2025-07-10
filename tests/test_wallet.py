import unittest
import os
from ..wallet import Wallet


class MockTransaction:
    def __init__(self, sender, recipient, amount, signature):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature


class WalletTest(unittest.TestCase):
    def setUp(self):
        self.node_id = 'testnode'
        self.wallet = Wallet(self.node_id)
        self.wallet.create_keys()

    def tearDown(self):
        file = f'wallet-{self.node_id}.txt'
        if os.path.exists(file):
            os.remove(file)

    def test_create_keys(self):
        self.assertIsNotNone(self.wallet.private_key)
        self.assertIsNotNone(self.wallet.public_key)
        self.assertIsInstance(self.wallet.private_key, str)
        self.assertIsInstance(self.wallet.public_key, str)

    def test_save_keys(self):
        result = self.wallet.save_keys()
        self.assertTrue(result)
        self.assertTrue(os.path.exists(f'wallet-{self.node_id}.txt'))

    def test_load_keys(self):
        self.wallet.save_keys()
        new_wallet = Wallet(self.node_id)
        result = new_wallet.load_keys()
        self.assertTrue(result)
        self.assertEqual(new_wallet.public_key, self.wallet.public_key)
        self.assertEqual(new_wallet.private_key, self.wallet.private_key)

    def test_sign_transaction_and_verify(self):
        signature = self.wallet.sign_transaction('sender', 'recipient', 10.0)
        self.assertIsInstance(signature, str)

        # Verify the signature
        tx = MockTransaction(
            sender=self.wallet.public_key,
            recipient='recipient',
            amount=10.0,
            signature=signature
        )
        result = Wallet.verify_transaction(tx)
        self.assertTrue(result)

    def test_verify_transaction_invalid(self):
        signature = self.wallet.sign_transaction('sender', 'recipient', 10.0)
        tx = MockTransaction(
            sender=self.wallet.public_key,
            recipient='someone-else',
            amount=100.0,
            signature=signature
        )
        result = Wallet.verify_transaction(tx)
        self.assertFalse(result)

    def test_verify_transaction_mining(self):
        tx = MockTransaction(
            sender='MINING',
            recipient='recipient',
            amount=10.0,
            signature=''
        )
        result = Wallet.verify_transaction(tx)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
