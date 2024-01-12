# Bitcoin Core with Falcon: Post-Quantum Security

🔒 This repository aims to enhance the security of Bitcoin Core by integrating the Falcon lattice-based digital signature algorithm into the Bitcoin Core. Falcon is designed to provide post-quantum security, safeguarding the Bitcoin network against potential quantum computing threats. [See Example](#code-testnetpy)

## About Falcon

Falcon is a cryptographic signature algorithm submitted to the NIST Post-Quantum Cryptography Project. It is designed to resist attacks from quantum computers, making it a promising choice for securing Bitcoin transactions in a post-quantum era.

Key features of Falcon include:

- **Security**: Falcon is based on the theoretical framework of Gentry, Peikert, and Vaikuntanathan for lattice-based signature schemes, providing robust security.
- **Compactness**: Falcon signatures are substantially shorter than many other lattice-based signature schemes, making them efficient for blockchain use.
- **Speed**: Implementation of fast Fourier sampling allows for rapid signature creation and verification.
- **Scalability**: Falcon offers efficient operations, allowing for long-term security parameters at a moderate cost.
- **RAM Economy**: Enhanced key generation in Falcon uses minimal RAM, making it compatible with memory-constrained devices.

## Performance

Falcon's performance on a common desktop computer is impressive:

- **Falcon-512**: Key generation time: 8.64 ms, Signature generation speed: 5948.1 signatures per second, Public key size: 897 bytes, Signature size: 666 bytes.
- **Falcon-1024**: Key generation time: 27.45 ms, Signature generation speed: 2913.0 signatures per second, Public key size: 1793 bytes, Signature size: 1280 bytes.

These performance metrics demonstrate Falcon's efficiency and suitability for real-world applications.

For more information, go to Bitcoin-Simulation folder.

## Additional Contents

- [Falcon Specification (PDF)](https://falcon-sign.info/falcon.pdf)
- [Falcon Website](https://falcon-sign.info/)
- [pybitcointools](https://github.com/primal100/pybitcointools)
- [falcon.py](https://github.com/tprest/falcon.py)
- [Validate Generated Wallet addresses](https://awebanalysis.com/en/bitcoin-address-validate/)
