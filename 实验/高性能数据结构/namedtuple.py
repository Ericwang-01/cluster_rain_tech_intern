# encoding:utf-8
"""
生成一个类
    args:typename, field_names
    如何访问实例的属性
        ·field_names参数是一个用于指定字段名称的字符串或者可迭代对象。在创建namedtuple对象时，会将字段名称作为属性名，用于访问该对象的属性值。
"""""
from collections import namedtuple
# 创建Student类
Student = namedtuple("Student", ["id", "name", "age", "gender"])
# 实例化
xiaoming = Student("001", "xiaoming", "25", "male")
print(xiaoming.id, xiaoming.name, xiaoming.age, xiaoming.gender)

lst_var = [1,2,3,3,4]
set_var = set(lst_var)  #
print(set_var)
print(type(set_var))