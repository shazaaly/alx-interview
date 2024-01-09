#!/usr/bin/python3

def canUnlockAll(boxes):
    """Function to return true if all boxes unlocked """
    unlocked_boxes = list(boxes[0])  # [1]

    for i in range(len(boxes)):
        for key in boxes[i]:
            if i in unlocked_boxes and i > 0 and key > 0:
                unlocked_boxes.append(key)

    unlocked_boxes = list(set(unlocked_boxes))

    if len(unlocked_boxes) == len(boxes):
        return True
    return False



    #return unlocked_boxes







boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))