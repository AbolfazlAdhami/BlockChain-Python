from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import Crypto.Random
import binascii


class Wallet:
    """Creates ,loads,and holds private keys, Manages transaction signing and verification"""

    def __init__(self):
        self.private_key = None
        self.public_key = None

    def create_keys(self):
        """Create a new pair of privet and public keys"""
        private_key, public_key = self.generated_keys()
        self.private_key = private_key
        self.public_key = public_key

    def save_keys(self):
        """Saves the keys to a file (wallet.txt)"""
        if self.public_key != None and self.private_key != None:
            try:
                with open('wallet.txt', mode='w') as f:
                    f.write(self.public_key)
                    f.write('\n')
                    f.write(self.private_key)
                    return True
            except (IOError, IndexError):
                print("Saving Files Failed...")
                return False

    def load_keys(self):
        """Loads the keys from the wallet.txt file into memory."""
        try:
            with open('wallet.txt', mode='r') as f:
                keys = f.readlines()
                public_key = keys[0][:-1]  # [:-1] for skip new line \n
                private_key = keys[1]
                self.public_key = public_key
                self.private_key = private_key
                return True
        except (IOError, IndexError):
            print("Loading Files Failed...")
            return False

    def generated_keys(self):
        """Generate a new pair of private and public"""
        private_key = RSA.generate(1024, Crypto.Random.new().read)
        public_key = private_key.publickey()

        private_key_hex = binascii.hexlify(
            private_key.export_key(format='DER')).decode('ascii')
        public_key_hex = binascii.hexlify(
            public_key.export_key(format='DER')).decode('ascii')
        return private_key_hex, public_key_hex

    def sign_transaction(self, sender, recipient, amount):
        """Sign a transaction and return the signature.

        Args:
            sender : The sender of transaction.
            recipient : The recipient of the Transaction 
            amount : The amount of the tranaction 

        Returns: A Hex binacii number that Should be Valid for Accept Tranaction and build a new Block

        """
        signer = PKCS1_v1_5.new(RSA.importKey(
            binascii.unhexlify(self.private_key)))
        h = SHA256.new((str(sender)+str(recipient)+str(amount)).encode('utf8'))
        signature = signer.sign(h)
        return binascii.hexlify(signature).decode('ascii')

    @staticmethod
    def verify_transaction(transaction):
        """Verify the signature of the transaction.

        Args:
            transaction : The Transaction that Should be verified 
        """
        if transaction.sender == 'MINING':
            return True
        public_key = RSA.importKey(binascii.unhexlify(transaction.sender))
        verifier = PKCS1_v1_5.new(public_key)
        h = SHA256.new((str(transaction.sender)+str(transaction.recipient) +
                       str(transaction.amount)).encode('utf8'))
        return verifier.verify(h, binascii.unhexlify(transaction.signature))
