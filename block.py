from time import time


class Block:
    def __init__(self, index, pervious_hash, transactions, proof, time=time()):
        self.index = index
        self.pervious_hash = pervious_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof
