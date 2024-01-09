#!/usr/bin/python3

def canUnlockAll(boxes):
    unlocked_boxes = [0]  # Box 0 is already unlocked
    keys = list(boxes[0])  # Start with keys from Box 0

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.append(key)
            keys.extend(boxes[key])

    return len(unlocked_boxes) == len(boxes)

# Test cases
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected output: False

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False
