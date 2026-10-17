#!/usr/bin/env python3


def islower(c):
    """Check if a character is a lowercase letter."""
    if ord('a') <= ord(c) <= ord('z'):
        return True
    return False