#!/usr/bin/python3
"""
Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer

"""


def pascal_triangle(n):
    pascal_lsit = []
    if (n <= 0):
        return pascal_lsit
    else:
        for i in range(n):
            row = [1] * (i + 1)

            if (i == 0):
                pascal_lsit.append(row)
            elif (i == 1):
                pascal_lsit.append(row)
            else:
                # transform the row
                for j in range(1, i):
                    row[j] = pascal_lsit[i - 1][j - 1] + pascal_lsit[i - 1][j]
                pascal_lsit.append(row)
        return pascal_lsit
