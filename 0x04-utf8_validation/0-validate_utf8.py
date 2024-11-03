#!/usr/bin/python3
"""
utf-8 validation
"""


def validUTF8(data):
    """
    function that validate utf-8
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking the significant bits of each byte
    mask1 = 1 << 7   # 10000000 in binary
    mask2 = 1 << 6   # 01000000 in binary

    for byte in data:
        # Only interested in the 8 least significant bits of each integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine how many bytes the UTF-8 character should have
            if (byte & mask1) == 0:
                # 1-byte character (ASCII), starts with 0xxxxxxx
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                # 2-byte character, starts with 110xxxxx
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 | mask2):
                # 3-byte character, starts with 1110xxxx
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 | mask2 | (mask2 >> 1)):
                # 4-byte character, starts with 11110xxx
                num_bytes = 3
            else:
                # Not a valid UTF-8 start byte
                return False
        else:
            # Check that each continuation byte starts with 10xxxxxx
            if (byte & mask1) != mask1 or (byte & mask2) != 0:
                return False
            num_bytes -= 1

    # If num_bytes is 0, all characters were valid UTF-8
    return num_bytes == 0
