def save_file(blockchain, open_transactions):
    with open("blockchian.txt", mode='w') as f:
        f.write(str(blockchain))
        f.write('\n')
        f.write(str(open_transactions))
