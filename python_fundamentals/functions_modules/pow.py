#!/usr/bin/env python3


def pow(a, b):
    """Compute the value of a raised to the power of b."""
    if b == 0:
        return 1

    if b < 0:
        result = 1
        for _ in range(-b):
            result *= a
        return 1 / result
    else:
        result = 1
        for _ in range(b):
            result *= a
        return result
