#!/usr/bin/python3


def uppercase(s):
    for char in s:
        diff = 32 if ord(char) >= 97 and ord(char) <= 122 else 0
        print(chr(ord(char) - diff), end='')
    print()  # New line

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
