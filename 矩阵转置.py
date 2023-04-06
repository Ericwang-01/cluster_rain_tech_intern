# encoding:utf-8
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# def tran(matrix_var):
#     return [
#         [matrix_var[row][col]
#          for row in range (0, height)
#          for col in range(0, width)]
#     ]
# 初始化矩阵


# 输出原始矩阵
for row in matrix:
    print(*row)

# 转置矩阵
transpose = []
for i in range(len(matrix[0])): #  进入col
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])# col 不动，如找这一列中每一行的元素
    transpose.append(row)

# 输出转置后的矩阵
print('转置后:')
for row in transpose:
    print(*row)