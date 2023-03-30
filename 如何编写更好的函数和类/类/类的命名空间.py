# encoding:utf-8
"""
命名空间，是一个字典实例，用来存储类的变量和方法
*实验目的
    —查看类的命名空间
    ('__module__', '__main__')
    变量和函数
    ('MONEY', 100)
    ('__init__', <function Person.__init__ at 0x00000226BE31C280>)
    ('info_print', <function Person.info_print at 0x00000226BE31C310>)
    魔法方法
    ('__dict__', <attribute '__dict__' of 'Person' objects>)
    ('__weakref__', <attribute '__weakref__' of 'Person' objects>)
    ('__doc__', None)
"""


class Person:
    MONEY = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info_print(self):
        print(f"{self.name, self.age}")


print("查看Person类的命名空间:", Person.__dict__)
for item in Person.__dict__.items():
    print(item)


wang = Person("wangyuchao", 25)

wang.info_print()
print("查看实例的命名空间：", wang.__dict__)