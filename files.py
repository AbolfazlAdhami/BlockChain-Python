from pickle import dumps


def save_file(blockchain, open_transactions):
    try:
        with open("blockchian.p", mode='wb') as f:
            save_data = {
                'chain': blockchain, 'ot': open_transactions
            }
            f.write(dumps(save_data))
    except IOError:
        print("Saving failed!")
