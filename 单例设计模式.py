# encoding:utf-8
"""
前置知识
-设计模式：对于某一特定问题，前人总结的成熟解决方案
-单例：类实例化的对象只有一个内存地址
-__new__方法由object基类提供的内置静态方法
    -在内存中为对象分配空间、
    -返回对象引用（地址）
    -python解释器获得对象引用后，将引用的第一个参数传递给__init__方法（对self赋值）
    -__init__方法在实例化对象的时候自动执行，__new__在__init__之前执行
实验目的
-如何在实例化对象时，只返回一个内存地址
    -重写__new__方法，返回第一个对象的引用
    -这样，我们就改写了从基类中的继承的__new__方法（返回每一个实例化对象的地址）
-如何让init（目标语句）只执行一次
    —静态变量__flag
    —初始False，目标语句执行后赋值True,在目标语句的前面加if not __flag 防止其再次被执行
"""


class Player:

    __instance = None
    __flag = False

    def __new__(cls, *args, **kwargs):

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        if not Player.__flag:
            print("init执行了")
            Player.__flag = True


video = Player()
print(video)


music = Player()
print(music)