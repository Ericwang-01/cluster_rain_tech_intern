# encoding:utf-8
"""
私有属性（只能在类内部访问的属性）
    1.构造
    2.访问
    3.修改
1,两种方法的对比
"""


class Student(object):
    # 不能将属性直接暴露出来，防止随意修改成绩，检查非期望值
    def __init__(self, name, __score):
        self.name = name
        self.__score = __score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value


xiaoming = Student("xiaoming", 100)

name = xiaoming.name
print(name)

score = xiaoming.score
print(score)