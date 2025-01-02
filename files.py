import json


def save_file(blockchain, open_transactions):
    with open("blockchian.txt", mode='w') as f:
        f.write(json.dumps(blockchain))
        f.write('\n')
        f.write(json.dumps(open_transactions))
