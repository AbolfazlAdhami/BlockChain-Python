import pickle


def save_file(blockchain, open_transactions):
    with open("blockchian.p", mode='wb') as f:
        save_data = {
            'chain': blockchain, 'ot': open_transactions
        }
        f.write(pickle.dumps(save_data))
