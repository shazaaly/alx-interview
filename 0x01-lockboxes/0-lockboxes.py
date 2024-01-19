#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys
"""

def canUnlockAll(boxes):
    """return trure if all boxes unlocked"""
    unlocked_boxes = [0]  # Box 0 is already unlocked
    keys = list(boxes[0])  # Start with keys from Box 0  like [1, 2, 4]

    while keys:
        key = keys.pop() # pop a key and try it
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.append(key)
            keys.extend(boxes[key])  #newly opened box keys

    return len(unlocked_boxes) == len(boxes)

