from functools import wraps
from flask import Flask, jsonify, request
from wallet import Wallet
from flask_cors import CORS
from blockchain import Blockchain
app = Flask(__name__)
CORS(app)


def require_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            response = {
                "error": "Unsupported Media Type",
                "message": "Content-Type must be application/json"
            }
            return jsonify(response), 415
        return f(*args, **kwargs)
    return decorated_function

@app.route('/wallet', methods=['POST'])
def create_keys():
    wallet.create_keys()
    if wallet.save_keys():
        global blockchain
        blockchain = Blockchain(wallet.public_key,port)
        response = {
            'public_key': wallet.public_key,
            'private_key': wallet.private_key,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201

    response = {
        'message': "Saving the keys failed."
    }
    return jsonify(response), 500


@app.route('/wallet', methods=['GET'])
def load_keys():
    if wallet.load_keys():
        global blockchain
        blockchain = Blockchain(wallet.public_key,port)
        response = {
            'public_key': wallet.public_key,
            'private_key': wallet.private_key,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 200

    response = {
        'message': "Saving the keys failed."
    }
    return jsonify(response), 500


@app.route('/balance', methods=['GET'])
def get_balance():
    balance = blockchain.get_balance()
    if balance != None:
        response = {
            'message': 'Fetched balance Successfully.',
            'funds': balance
        }
        return jsonify(response), 200

    response = {
        'message': 'Loading wallet is faulled.',
        'wallet_set_up': wallet.public_key != None
    }
    return jsonify(response), 500


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_snapshot = blockchain.chain
    dict_chain = [block.__dict__.copy() for block in chain_snapshot]
    for dict_block in dict_chain:
        dict_block['transactions'] = [
            tx.__dict__ for tx in dict_block['transactions']]
    return jsonify(dict_chain), 200

@app.route('/broadcast-transaction',methods=['POST'])
@require_json
def broadcast_tranaction():
    values=request.get_json()
    if not values:
        response={'message':'Not Data Found'}
        return jsonify(response),400
    required=['sender','recipient','amount','signature']
    if not all(key in values for key in required):
        response={'message':'Some Data is Missing'}
        return jsonify(response),422     
    success=blockchain.add_transaction(values['recipient'],values['sender'],values['signature'],values['amount'])  
    if success:
            response = {
            'message': 'Successfully added tranaction.', 'transaction': {
                'sender': values['sender'], 'recipient': values['recipient'], 'amount': values['amount'], 'signature': values['signature']
            },
            'funds': blockchain.get_balance()
            }
            return jsonify(response), 201
        
@app.route('/transaction', methods=['GET'])
def get_open_transaction():
    transactions = blockchain.get_open_transactions()
    dict_transaction = [tx.__dict__ for tx in transactions]
    return jsonify(dict_transaction), 200


@app.route('/transaction', methods=['POST'])
@require_json
def add_transaction():
    if wallet.public_key == None:
        response = {
            'message': 'Adding a block failed.',
        }
        return jsonify(response), 401
    values = request.get_json()
    if not values:
        response = {
            'message': 'No Data found.'
        }
        return jsonify(response), 402
    require_fields = ['recipient', 'amount']
    if not all(field in values for field in require_fields):
        response = {
            'message': 'Require Data is missing.'
        }
        return jsonify(response), 402
    recipient = values['recipient']
    amount = values['amount']
    signature = wallet.sign_transaction(wallet.public_key, recipient, amount)
    success = blockchain.add_transaction(
        recipient, wallet.public_key, signature, amount)
    print(success, "this is where have bug")
    if success:
        response = {
            'message': 'Successfully added tranaction.', 'transaction': {
                'sender': wallet.public_key, 'recipient': recipient, 'amount': amount, 'signature': signature
            },
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Creating a transaction failed'
        }
        return jsonify(response), 500


@app.route('/mine', methods=['POST'])
def mine():
    block = blockchain.mine_block()
    if block != None:
        dict_block = block.__dict__.copy()
        dict_block['transactions'] = [
            tx.__dict__ for tx in dict_block['transactions']]
        response = {
            'message': 'Block added successfully.',
            'block': dict_block,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Adding a block failed.',
            'wallet_set_up': wallet.public_key != None

        }
        return jsonify(response), 500


@app.route('/node', methods=['POST'])
@require_json
def add_node():
    values = request.get_json()
    if not values:
        response = {
            'message': 'No Data attached.'
        }
        return jsonify(response), 400

    if 'node' not in values:
        response = {
            'message': 'No NODE Data attached.'
        }
        return jsonify(response), 404
    node = values['node']
    blockchain.add_peer_node(node)
    response = {
        'message': 'Node Added successfully.',
        'all_nodes': blockchain.get_peer_node()
    }
    return jsonify(response), 201


@app.route('/node/<node_url>', methods=['DELETE'])
def remove_node(node_url):
    if node_url == '' or node_url == None:
        response = {
            'message': 'No Node found.'
        }
        return jsonify(response), 404
    blockchain.remove_peer_node(node_url)
    response = {
        'message': 'Node Removed.',
        'all_nodes': blockchain.get_peer_node()
    }
    return jsonify(response), 200


@app.route('/nodes', methods=['GET'])
def get_nodes():
    response = {
        'all_nodes': blockchain.get_peer_node()
    }
    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser=ArgumentParser()
    parser.add_argument('-p','--port',type=int,default=8000)
    args=parser.parse_args()
    print(args.port)
    port=args.port
    wallet = Wallet(port)
    blockchain = Blockchain(wallet.public_key,port)
    app.run(host='0.0.0.0', port=port)
