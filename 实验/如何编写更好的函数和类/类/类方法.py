# encoding:utf-8
"""
-类方法的特点：
    定义
    *定义时一定有参数cls,表示调用该方法的类
    *定义时使用@classmethod将普通函数转变成类方法
    用途
    *操作类级别的信息
    访问和修改类变量，但不能访问实例变量
    类和实例都可以调用，也可以访问类变量
"""


class MyClass:
    count = 0

    @classmethod
    # 类方法要加装饰器@classmethod
    def add_counter(cls):
        # 类变量，要通过cls参数访问
        cls.count += 1


instance = MyClass()
print("通过实例名访问类变量", instance.count)
# 通过类名访问类变量
class_var = MyClass.count
print(class_var)

MyClass.add_counter()
print("通过类名调用类方法:", MyClass.count)


instance.add_counter()
print("通过实例名调用类方法:", instance.count)

