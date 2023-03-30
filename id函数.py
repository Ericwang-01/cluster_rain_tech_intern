# encoding:utf-8
"""
-返回对象(object)的唯一标识码，该标识码是一个整数，且在对象的生命周期中是唯一且恒定的
用法
—id() 常被用来确定两个变量是否指向同一个对象
"""
x = 3
y = 3
z = 3
print(id(x))
print(type(x))
print(id(y))
print(id(z))