# Cryptchat

[![Build Status](https://travis-ci.org/djohsson/Cryptchat.svg?branch=master)](https://travis-ci.org/djohsson/Cryptchat)

Chat program implemented in Python. The messages are encrypted using AES and the session key is established using Diffie-Hellman key exchange.

## Usage
Server mode:
```bash
python3 main.py nick 'server' port [dhgroup]
```

Client mode:
```bash
python3 main.py nick address port [dhgroup]
```

dhgroup determines which prime number, private key size and session key size will be used. Valid groups are 5, 14, 16, 17 and 18. 17 will be used if no dhgroup is specified, which results in a session key of 256 bits.

## Security

Cryptchat is **probably** secure against:

* Eavesdropping

Vulnerable to, **at the very least**:

* Traffic analysis
* Man-in-the-middle attack
* Replay attack

The AES cipher is using an IV the size of 16 bits. This means after 2^16 messages the IV have been reused with the same session key at least once. Keep the chat sessions below 65k messages.
