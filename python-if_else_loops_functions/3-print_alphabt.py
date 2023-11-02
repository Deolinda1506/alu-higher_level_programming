#!/usr/bin/python3

for i in range(97, 123):
    if i != 101 and i != 113:  # Excludes 'e' and 'q' ASCII values
        print(chr(i), end='')

# Ensure the output doesn't include a newline
