from Crypto.PublicKey import RSA
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
        pass

    def generated_keys(self):
        private_key = RSA.generate(1024, Crypto.Random.new().read)
        public_key = private_key.publickey()

        private_key_hex = binascii.hexlify(
            private_key.export_key(format='DER')).decode('ascii')
        public_key_hex = binascii.hexlify(
            public_key.export_key(format='DER')).decode('ascii')
        return private_key_hex, public_key_hex
