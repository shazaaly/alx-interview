#!/usr/bin/python3

def canUnlockAll(boxes):
    """Function to return true if all boxes unlocked """
    unlocked_boxes = [0]
    keys = list(boxes[0])


    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.append(key)
            keys.extend(boxes[key])

        return len(unlocked_boxes) == len(boxes)
