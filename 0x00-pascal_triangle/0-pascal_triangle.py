#!/usr/bin/python3

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
