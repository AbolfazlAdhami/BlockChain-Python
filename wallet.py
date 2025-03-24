from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import Crypto.Random
import binascii


class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def create_keys(self):
        private_key, public_key = self.generated_keys()
        self.private_key = private_key
        self.public_key = public_key

    def load_keys(self):
        try:
            with open('wallet.txt', mode='r') as f:
                keys = f.readline()
                self.public_key = keys[0][:-1]  # [:-1] for skip new line \n
                self.private_key = keys[1]
        except (IOError, IndexError):
            print("Loading Files Failed...")

    def save_keys(self):
        if self.public_key != None and self.private_key != None:
            try:
                with open('wallet.txt', mode='w') as f:
                    f.write(self.public_key)
                    f.write('\n')
                    f.write(self.private_key)
            except (IOError, IndexError):
                print("Saving Files Failed...")

    def generated_keys(self):
        private_key = RSA.generate(1024, Crypto.Random.new().read)
        public_key = private_key.publickey()

        private_key_hex = binascii.hexlify(
            private_key.export_key(format='DER')).decode('ascii')
        public_key_hex = binascii.hexlify(
            public_key.export_key(format='DER')).decode('ascii')
        return private_key_hex, public_key_hex

    def sign_transaction(self, sender, recipient, amount):
        """_summary_

        Args:
            sender (_type_): _description_
            recipient (_type_): _description_
            amount (_type_): _description_

        Returns:
            _type_: _description_
        """
        signer = PKCS1_v1_5.new(RSA.importKey(
            binascii.unhexlify(self.private_key)))
        h = SHA256.new((str(sender)+str(recipient)+str(amount)).encode('utf8'))
        signature = signer.sign(h)
        return binascii.hexlify(signature).decode('ascii')

    @staticmethod
    def verify_transaction(transaction):
        if transaction.sender == 'MINING':
            return True
        public_key = RSA.importKey(binascii.unhexlify(transaction.sender))
        verifier = PKCS1_v1_5.new(public_key)
        h = SHA256.new((str(transaction.sender)+str(transaction.recipient) +
                       str(transaction.amount)).encode('utf8'))
        return verifier.verify(h, binascii.unhexlify(transaction.signature))
