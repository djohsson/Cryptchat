# Cryptchat

Work in progress.

Also, this will not be safe to use even when it is finished.

Cryptchat is **probably** secure against:

* Eavesdropping

Vulnerable to, **at the very least**:

* Traffic analysis
* Man-in-the-middle attack
* Replay attack

As of now, the AES cipher is using an IV the size of 16 bits. This means after 2^16 messages the IV have been reused with the same session key at least once. Keep the chat sessions below 65k messages.
