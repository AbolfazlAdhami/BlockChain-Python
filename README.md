# BlockChain‑Python 🚀

A Python-based blockchain implementation featuring core concepts like transactions, wallets, proof-of-work mining, and a simple Flask API 🔐

---

## 🧩 Features

- Transactions with RSA-signed wallets  
- Wallet generation and balance tracking  
- Proof‑of‑Work block mining  
- Flask API for submitting transactions and mining  
- Decorator support for JSON-only endpoints  
- Suitable for learning and experimentation

---

## 🛠️ Installation

Ensure you're using **Python 3.9+**

```bash
git clone https://github.com/AbolfazlAdhami/BlockChain-Python.git
cd BlockChain-Python
python3 -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

---

## ⚙️ Usage

### 1. Generate a wallet

```bash
python run.py wallet create
```

### 2. Start the API/server

```bash
python run.py server
```

By default runs on `http://127.0.0.1:5000`

### 3. Interact via HTTP

#### Submit a transaction

```bash
curl -X POST http://127.0.0.1:5000/transaction \
  -H 'Content-Type: application/json' \
  -d '{"sender": "...", "recipient": "...", "amount": 10.0, "signature": "..."}'
```

#### Mine a block

```bash
curl http://127.0.0.1:5000/mine
```

#### Check the blockchain

```bash
curl http://127.0.0.1:5000/chain
```

---

## ✅ Testing

Run unit tests with:

```bash
pytest
```

Tests cover:

- `Transaction` class
- `Wallet` signing and verifying
- `Blockchain` mining and validation
- `require_json` decorator

---

## 📁 Detailed Project Structure

```
BlockChain-Python/
│
├── app/
│   ├── __init__.py              # Package initializer
│   ├── blockchain.py            # Core blockchain & block logic
│   ├── transaction.py           # Transaction model
│   ├── wallet.py                # Key generation, signing, verification
│   └── server.py                # Flask API endpoints
│
├── utility/
│   ├── __init__.py
│   └── printable.py             # __str__ mixin for models
│
├── decorators.py                # Flask JSON decorator
├── run.py                       # Entrypoint: CLI for wallet/server
├── requirements.txt             # Python dependencies
├── tests/                       # Unit tests
│   ├── test_transaction.py
│   ├── test_wallet.py
│   ├── test_blockchain.py
│   └── test_decorators.py
├── .gitignore
└── README.md
```

---

## 🧠 Concepts Explained

### 🔐 Cryptography in Blockchain

Blockchain security is rooted in **asymmetric cryptography**, **digital signatures**, and **hash functions**.

#### ✅ RSA (Asymmetric Encryption)
- RSA generates a **public-private key pair**.
- Private key signs transactions; public key verifies them.

📚 [RSA Explained – Medium](https://medium.com/asecuritysite-when-bob-met-alice/rsa-an-example-and-walkthrough-4878857041d5)

---

### 🧾 Wallets & Digital Signatures

- Wallets manage private/public keys.
- Transactions are **digitally signed** to ensure authenticity and integrity.
- Signatures can be verified using public keys.

📚 [Digital Signatures – GeeksForGeeks](https://www.geeksforgeeks.org/digital-signatures/)

---

### 🧱 What is a Blockchain?

- A blockchain is an **immutable linked list** of blocks.
- Each block contains:
  - Transactions
  - Timestamp
  - Nonce (proof of work)
  - Hash of previous block

📚 [Blockchain Explained – IBM](https://www.ibm.com/topics/what-is-blockchain)

---

### 🔁 Proof of Work

- Requires solving a cryptographic puzzle before adding blocks.
- Prevents tampering and spam by making it expensive to mine malicious blocks.

📚 [Proof of Work (PoW) – Investopedia](https://www.investopedia.com/terms/p/proof-work.asp)

---

### 🔒 SHA‑256 Hashing

- One-way cryptographic function that outputs a fixed-size 256-bit hash.
- Used to secure block data and ensure chain integrity.

📚 [SHA-256 – Wikipedia](https://en.wikipedia.org/wiki/SHA-2)

---

### 🔄 How This Project Uses These Concepts

| Concept        | Used For                                         |
|----------------|--------------------------------------------------|
| RSA            | Wallet key generation & transaction signing      |
| SHA-256        | Block hashing and data integrity                 |
| Blockchain     | Store immutable record of transactions           |
| Proof of Work  | Secure and validate mined blocks                 |
| Digital Wallet | Sign and verify user identity in transactions    |
| Flask API      | Simplified interface for blockchain interaction  |

---

## 📚 References & Learning Resources

- [Mastering Bitcoin – by Andreas Antonopoulos](https://github.com/bitcoinbook/bitcoinbook)
- [Blockchain Demo – Interactive Visual Guide](https://andersbrownworth.com/blockchain/)
- [PyCryptodome Documentation](https://pycryptodome.readthedocs.io/en/latest/)
- [Bitcoin Whitepaper – Satoshi Nakamoto](https://bitcoin.org/bitcoin.pdf)

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or pull request.  
Suggestions, bugs, and improvements are encouraged.

---

## 📜 License

This project is open-source under the **MIT License**.