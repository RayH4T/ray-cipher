# Ray Cipher

A Python-based numerical cipher encoder, decoder, and brute-force shift analyzer.

## Features

- Encode text into numerical sequences.
- Decode numerical sequences into readable text.
- Test all 26 possible alphabet shifts.
- Colored terminal interface and loading animation.

## Project Structure

| File | Description |
| --- | --- |
| `ray_cipher.py` | Encodes and decodes messages. |
| `ray_cracker.py` | Tests all 26 possible shifts. |

## Requirements

- Python 3
- Terminal or command-line interface

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/ray-cipher.git
cd ray-cipher
```

## Usage

Run Ray Cipher:

```bash
python3 ray_cipher.py
```

Run Ray Cracker:

```bash
python3 ray_cracker.py
```

## Example

Input:

```text
WHO IS RAY
```

Output:

```text
15-12-19-19-22-0-4-22-25-19-11
```

## How It Works

Ray Cipher uses a fixed alphabet shift derived from an internal key. Spaces are represented by `0`, and numbers are separated by hyphens.

Ray Cracker tests all 26 possible shifts and displays each candidate.

## Disclaimer

This project is for educational purposes only. It is not secure encryption and should not be used to protect confidential information.

## Author

RAY

## License

No license has been specified yet.
