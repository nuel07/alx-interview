#!/usr/bin/python3
'''determines if all the boxes can be opened.'''


def canUnlockAll(boxes):
    '''determines if all boxes have keys and
    returns True if all boxes can be opened.
    '''
    keys = [0]
    for idx, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in keys and key != idx:
                keys.append(key)
    if len(keys) == len(boxes):
        return True
    return False
