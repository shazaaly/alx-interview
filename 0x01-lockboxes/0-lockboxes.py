#!/usr/bin/python3

def canUnlockAll(boxes):
    """return trure if all boxes unlocked"""
    unlocked_boxes = [0]  # Box 0 is already unlocked
    keys = list(boxes[0])  # Start with keys from Box 0

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.append(key)
            keys.extend(boxes[key])  #newly opened box keys

    return len(unlocked_boxes) == len(boxes)

