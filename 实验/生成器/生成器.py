# encoding:utf-8
"""
函数，返回一个可迭代对象
和列表比较，一次性计算然后返回值
和普通函数用return返回值比较， yield写在生成器函数内部


"""


def simple_generator():

    yield 1
    yield 2
    yield 3
    yield 4


for value in simple_generator():
    print(value)


values = [1, 2, 3, 4]
print(values)