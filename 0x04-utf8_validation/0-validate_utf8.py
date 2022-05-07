#!/usr/bin/python3
''' utf-8 validation function '''


def validUTF8(data) -> bool:
    ''' returns True for valid utf-8 encoding and False otherwise '''
    next_bytes = 0
    for num in data:
        binary_rep = bin(num).replace('0b', '').rjust(8, '0')[-8:]

        if next_bytes == 0:
            if binary_rep.startswith('11110'):
                next_bytes = 3
            if binary_rep.startswith('1110'):
                next_bytes = 2
            if binary_rep.startswith('110'):
                next_bytes = 1
            if binary_rep.startswith('10'):
                return False
        else:
            if not binary_rep.startswith('10'):
                return False
            next_bytes -= 1
    if next_bytes != 0:
        return False

    return True
