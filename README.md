Ray Cipher

A Python-based numerical cipher encoder, decoder, and brute-force shift analyzer.

Ray Cipher is an educational command-line project built with Python. It converts alphabetic text into numerical sequences using a fixed alphabet shift and allows users to decode the sequences back into readable text.

The companion tool, Ray Cracker, tests all 26 possible alphabet shifts to demonstrate how a simple substitution cipher can be analyzed and broken.

Features

* Encode: Convert text into numerical sequences.
* Decode: Restore encoded sequences to readable text.
* Brute-force analysis: Test all 26 possible alphabet shifts.
* Terminal interface: Colored output and a loading animation.
* Lightweight: Uses Python’s standard library without additional dependencies.

Project Files

File	Description
ray_cipher.py	Encodes and decodes messages.
ray_cracker.py	Tests all 26 possible shifts.

Requirements

* Python 3
* A terminal or command-line interface

No third-party Python packages are required.

Installation and Usage

Clone the repository:

git clone https://github.com/YOUR-USERNAME/ray-cipher.git
cd ray-cipher

Run the encoder and decoder:

python3 ray_cipher.py

Run the brute-force analyzer:

python3 ray_cracker.py

Replace YOUR-USERNAME with your GitHub username.

How It Works

Ray Cipher applies a fixed alphabet shift derived from an internal key. Letters are converted into numbers, and spaces are represented by 0. Numbers are separated by hyphens.

Ray Cracker attempts every possible shift from 0 to 25 and displays the resulting text for each candidate.

Example

Input:

WHO IS RAY

Example encoded output:

15-12-19-19-22-0-4-22-25-19-11

Disclaimer

Ray Cipher is intended for educational purposes and experimentation with basic cryptography concepts. It is not secure encryption and should not be used to protect passwords, confidential information, or sensitive communications.

Author

Created by YOUR-NAME

License

This project is available for learning and personal experimentation. A formal license can be added if you wish to define how others may use, modify, and distribute the code.
