from time import time

from printable import Pri

class Block:
    def __init__(self, index, pervious_hash, transactions, proof, time=time()):
        self.index = index
        self.pervious_hash = pervious_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof
