#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    function used to check if we have
    opened all boxes.
    the function collects all boxes opened
    to a set unlocked
    final checks if unlocked == the num of boxes
    """
    n = len(boxes)
    unlocked = set([0])  # Start with box 0 unlocked
    keys = [0]  # Start by exploring box 0

    # Continue until there are no more keys to use
    while keys:
        current_box = keys.pop()  # Get a box to explore
        for key in boxes[current_box]:
            if key < n and key not in unlocked:
                unlocked.add(key)  # Mark this box as unlocked
                keys.append(key)   # Add the box to explore its keys

    # If the number of unlocked boxes equals
    # the total number of boxes, return True
    return len(unlocked) == n
