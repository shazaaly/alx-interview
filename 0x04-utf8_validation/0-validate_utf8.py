#!user/bin/env python3

""" A script to determines if a given data 
    set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ٌ Return  True if data is a valid UTF-8 encoding, else return False

    Args:
        data (_type_):  list of integers
    """
    count = 0
    for byte in data:
        if count == 0:
            mask = 0x80
            while (byte & mask) != 0:
                count += 1
                mask >>= 1
            if count == 0:
                continue
            if count > 4 or count == 1:
                return False
        else:
            if (byte & 0xC0) != 0x80:
                return False
    return count == 0
