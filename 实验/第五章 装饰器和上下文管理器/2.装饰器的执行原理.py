# encoding:utf-8
"""
-本质是一个可调用的对象
-接收一个函数作为参数，返回一个新的函数
-从而实现在不更改原函数代码的情况，对其进行增强
"""


def my_decorator(func):
    def wrapper():
        print("New function added ,before the function is called")
        func()
        print("New function added, after the function is called")
    # 返回wrapper函数， 替代被装饰的原始函数
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")

say_hello()