# encoding:utf-8
"""
from easy to complexity
from concrete to abstraction
"""

# do some operation in nine row
j = 1
while j < 10:
    # print nine * in one row
    i = 1
    while i <= j:  # j determine how much * in a line
        print(f"{i} x {j} = {i*j}\t", end='')
        i += 1

    print()
    j += 1

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
transpose = []

# do some operation in other two colum
for j in range(len(matrix[0])):
    row = []

    # take first colum number ,put in row list
    for i in range(len(matrix)):
        row.append(matrix[i][j])

    transpose.append(row)
print(transpose)

