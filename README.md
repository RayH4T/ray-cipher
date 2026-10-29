Ray Cipher

A Python-based numerical encoding and decoding system.

Ray Cipher is an educational command-line project built with Python. It converts alphabetic text into numerical sequences using a fixed alphabet shift and allows users to decode the sequences back into readable text.

Features

* Encode: Convert text into numerical sequences.
* Decode: Restore encoded sequences to readable text.
* Colored Interface: A terminal interface with colored output and an ASCII banner.
* Interactive Menu: Simple menu for encoding, decoding, and viewing project information.
* Lightweight: Uses Python’s standard library without additional dependencies.

Screenshots

Decode Example
IMG_8718.jpeg 
This screenshot demonstrates the decoding function, which converts a numerical sequence back into readable text.

Encode Example
IMG_8719.jpeg 
This screenshot demonstrates the encoding function, which converts text into a numerical sequence.

Requirements

* Python 3
* A terminal or command-line interface

No third-party Python packages are required.

Installation

Clone the repository:

git clone https://github.com/RayH4T/ray-cipher.git
cd ray-cipher

Usage

Run Ray Cipher:

python3 ray_cipher.py

Follow the on-screen menu to encode or decode a message.

How It Works

Ray Cipher applies a fixed alphabet shift derived from an internal key. Letters are converted into numbers, while spaces are represented by 0. Numbers are separated by hyphens.

Disclaimer

Ray Cipher is intended for educational purposes and experimentation with basic cryptography concepts. It is not secure encryption and should not be used to protect passwords, confidential information, or sensitive communications.

Author

RAY

License

No license has been specified yet.
