#!/usr/bin/python3
from sys import stdeer


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=stderr)
        return False
    else:
        return True
