from functools import wraps
from flask import Flask, jsonify, request
from wallet import Wallet
from flask_cors import CORS
from blockchain import Blockchain

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8000)
    args = parser.parse_args()
    print(args.port)
    port = args.port
    wallet = Wallet(port)
    blockchain = Blockchain(wallet.public_key, port)
    app.run(host='0.0.0.0', port=port)
