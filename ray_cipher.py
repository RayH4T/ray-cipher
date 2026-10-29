#!/usr/bin/env python3
# ==================================================
#       R A Y   C I P H E R   //   V 2 . 0
#       Numerical Encoding & Decoding System
# ==================================================

import os
import shutil

KEY = 7391
SHIFT = KEY % 26

# ANSI terminal colors
RED = "\033[91m"
DARK_RED = "\033[31m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
GRAY = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def center(text):
    width = shutil.get_terminal_size().columns
    return text.center(width)


def banner():
    art = r"""
 ____   ___  __   __
|  _ \ / _ \ \ \ / /
| |_) | | | | \ V /
|  _ <| |_| |  | |
|_| \_\\___/   |_|
"""

    print()
    print(RED + BOLD)

    for line in art.strip("\n").splitlines():
        print(center(line))

    print(RESET)
    print(CYAN + BOLD +
          center("R A Y   C I P H E R   V 2 . 0") + RESET)
    print(GRAY + center("NUMERICAL ENCRYPTION TERMINAL") + RESET)
    print(RED + center("=" * 42) + RESET)
    print(GRAY + center("STATUS  : ONLINE") + RESET)
    print(GRAY + center("SYSTEM  : ENCODE / DECODE") + RESET)
    print(GRAY + center("=" * 42) + RESET)


def encode(text):
    result = []

    for char in text.upper():
        if 'A' <= char <= 'Z':
            number = ord(char) - ord('A')
            encrypted = (number + SHIFT) % 26 + 1
            result.append(str(encrypted))

        elif char == ' ':
            result.append('0')

        # Ignore punctuation and unsupported characters

    return '-'.join(result)


def decode(code):
    result = []

    for token in code.split('-'):
        token = token.strip()

        if not token:
            raise ValueError("Empty number in code")

        if not token.isdigit():
            raise ValueError("Code must contain numbers only")

        number = int(token)

        if number == 0:
            result.append(' ')

        elif 1 <= number <= 26:
            original = (number - 1 - SHIFT) % 26
            result.append(chr(original + ord('A')))

        else:
            raise ValueError("Numbers must be between 0 and 26")

    return ''.join(result)


def show_menu():
    print()
    print(WHITE + BOLD + center("[1]  ENCODE MESSAGE") + RESET)
    print(WHITE + BOLD + center("[2]  DECODE MESSAGE") + RESET)
    print(WHITE + BOLD + center("[3]  ABOUT RAY CIPHER") + RESET)
    print(WHITE + BOLD + center("[0]  EXIT TERMINAL") + RESET)
    print(RED + center("-" * 42) + RESET)


def encode_mode():
    print(CYAN + "\n  >> ENCODING MODE" + RESET)
    print(GRAY + "  Enter your message below." + RESET)

    message = input(WHITE + "\n  MESSAGE > " + RESET)
    encrypted = encode(message)

    if not encrypted:
        print(RED + "\n  [!] No valid letters found." + RESET)
        return

    print(YELLOW + "\n  ENCRYPTION COMPLETE" + RESET)
    print(RED + BOLD + "\n  " + encrypted + RESET)
    print(GRAY + "\n  Copy the complete numerical sequence." + RESET)


def decode_mode():
    print(GREEN + "\n  >> DECODING MODE" + RESET)
    print(GRAY + "  Paste the complete numerical sequence." + RESET)

    code = input(WHITE + "\n  CODE > " + RESET)

    try:
        message = decode(code)

        print(GREEN + "\n  DECODING COMPLETE" + RESET)
        print(WHITE + BOLD + "\n  " + message + RESET)

    except ValueError:
        print(RED + "\n  [!] Invalid code. Check your input." + RESET)


def about():
    print(CYAN + "\n  >> ABOUT RAY CIPHER" + RESET)
    print(WHITE + "  Name   : Ray Numerical Cipher")
    print("  Version: 2.0")
    print("  Method : Fixed alphabet shift")
    print("  Format : Numbers separated by hyphens")
    print("  Key    : Configured internally" + RESET)
    print(GRAY + "\n  Educational cipher, not secure encryption." + RESET)


def main():
    while True:
        clear_screen()
        banner()
        show_menu()

        choice = input(WHITE + "\n  SELECT OPTION > " + RESET).strip()

        if choice == "1":
            encode_mode()

        elif choice == "2":
            decode_mode()

        elif choice == "3":
            about()

        elif choice == "0":
            print(RED + "\n  RAY CIPHER OFFLINE. GOODBYE." + RESET)
            break

        else:
            print(RED + "\n  [!] Invalid selection." + RESET)

        input(GRAY + "\n  Press ENTER to return to menu..." + RESET)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RED + "\n\n  SESSION TERMINATED." + RESET)
