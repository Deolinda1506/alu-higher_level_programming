#!/usr/bin/python3


def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the last digit using modulo
    print(last_digit, end='')
    return last_digit  # Return the last digit value

# Example usage
if __name__ == "__main__":
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print()  # Add a newline after the function calls
    print(r)
