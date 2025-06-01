# BlockChain-Python

A simple blockchain implementation in Python that demonstrates core concepts such as blocks, transactions, mining, wallets, and basic peer-to-peer networking.
## 🚀 Features

- ✅ Block creation and chaining with cryptographic hashes
- ✅ Basic transaction handling and verification
- ✅ Wallet system using public/private RSA key pairs
- ✅ Proof-of-work mining mechanism
- ✅ Simple node-based peer-to-peer communication

## 📁 Project Structure
```yaml
BlockChain-Python/
├── ui/ # Contains UI files (e.g., Flask or frontend interface)
│ └── app.js 
│ └── node.html # Web interface for interacting with the blockchain
│ └── style.css 
├── utility/ # Contains utility 
│ └── hash_util.py # Hashes a block/string and returns a string representation of it
│ └── printble.py # A base class which implements printing functionality
│ └── verification.py # A helper class which offer various static and class-based verification and validation methods.
├── block.py # Defines the Block class and hashing logic
├── blockchain.py # Manages the blockchain and proof-of-work
├── transaction.py # Handles transaction creation, signing, and validation
├── wallet.py # Generates public/private keys and signs data
├── node.py # Sets up and runs a blockchain network node
├── OLD_node.py # Previous version of the node implementation usign terminal
├── requirements.txt # Lists Python package dependencies
├── LICENSE # License file (MIT)
└── README.md # Project documentation
```
## 📦 Requirements
- Python 3.6+

### requirements.txt

```yaml
blinker==1.9.0
click==8.1.8
Flask==3.1.0
flask-cors==5.0.1
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
pycryptodome==3.22.0
Werkzeug==3.1.3
```
### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/AbolfazlAdhami/BlockChain-Python.git
cd BlockChain-Python
pip install -r requirements.txt
```
## ⚙️ Usage

Once you've installed the necessary dependencies from the `requirements.txt`, follow these steps to use the components of the blockchain project.

### 1. **Starting the Blockchain**

To run the blockchain and start mining blocks, run the `node.py` script:

```bash
python node.py
```
### 2. **Starting the Minning**
Should be create or load a wallet ID and then you can start minning or add new transaction to open list transactions 

## 📘 What is Blockchain?
Blockchain is a decentralized, distributed digital ledger that records transactions across many computers in a way that ensures the data cannot be altered retroactively. Each record (or "block") contains a group of transactions, a timestamp, and a link (hash) to the previous block — forming a secure "chain." This structure makes it nearly impossible to alter any single record without changing all subsequent blocks, which is why blockchain is considered tamper-resistant and ideal for systems that require trust without central authority, such as cryptocurrencies.    
## 🪙 Cryptocurrency
Cryptocurrency is a digital or virtual form of money that uses cryptography for security and operates on decentralized networks, usually a blockchain. It allows peer-to-peer transactions without the need for central authorities like banks. Bitcoin, Ethereum, and Litecoin are popular examples.

## 🔐 Wallet
A wallet in the context of cryptocurrency is a digital tool that stores your public and private keys. It allows users to send, receive, and manage their crypto assets securely. Wallets come in various forms: hardware (USB-like devices), software (desktop/mobile apps), and web-based (online services).

## 🌐 Node
A node is any computer that participates in a blockchain network. It stores a copy of the blockchain and helps validate and relay transactions. Some nodes are full nodes (which store the entire blockchain and enforce consensus rules), while others may be lightweight or mining nodes.

## 🔗 WEB3
Web3 (or Web 3.0) refers to the next evolution of the internet that integrates blockchain technology to create decentralized applications (dApps). It emphasizes user ownership, transparency, and removing reliance on centralized platforms. Tools like MetaMask and platforms like Ethereum are central to the Web3 ecosystem.

## 🔐 RSA (Rivest–Shamir–Adleman)
RSA is a widely used public-key cryptographic algorithm that enables secure data encryption and digital signatures. It uses a pair of keys:

- A public key for encryption or verification

- A private key for decryption or signing

In blockchain and wallet systems, RSA is often used to sign transactions, allowing others to verify the authenticity using the sender's public key.

## 📦 PKCS#1 v1.5
PKCS#1 v1.5 (Public-Key Cryptography Standards #1, version 1.5) is a padding scheme defined for RSA encryption and signing.
It ensures that messages are securely formatted before being signed or encrypted with RSA. This padding prevents certain cryptographic attacks and is commonly used for digital signatures in combination with hash functions like SHA-256.
In Python, it's used like this:
```python
from Crypto.Signature import PKCS1_v1_5
```
## 🔒 SHA-256 (Secure Hash Algorithm 256-bit)

SHA-256 is a cryptographic hash function that produces a fixed 256-bit (32-byte) output. It is:

- Deterministic: the same input always produces the same hash

- Irreversible: cannot retrieve original data from the hash

- Collision-resistant: hard to find two different inputs with the same hash

In blockchain, SHA-256 is used to:

- Hash block data

- Link blocks together

- Verify data integrity

- Create digital signatures

It's a foundational part of both Bitcoin and many other blockchain systems.


## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License.  
See the [MIT]((https://choosealicense.com/licenses/mit/)) file for more details.




