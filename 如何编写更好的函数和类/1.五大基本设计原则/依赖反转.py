# encoding:utf-8
'''
# 依赖反转原则
高层模块不应该依赖于底层模块，而应该依赖于抽象
Animal类不依赖于任何具体的移动策略，而是依赖于一个抽象的移动策略
Animal类定义了move接口，而Bird类实现了这个接口
'''


class Animal:
    def __init__(self, move_strategy):
        self.move_strategy = move_strategy

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def move(self):
        # 方法不再是具体的实现，而是使用在Bird类中指定的抽象移动策略
        # Animal类不依赖于任何具体的移动策略，而是依赖于一个（BirdMoveStrategy类定义的）抽象的移动策略
        self.move_strategy.move(self)


class BirdMoveStrategy:
    def move(self, a):
        print(f"{a.name} is flying.")


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        print()
        super().__init__(BirdMoveStrategy())
        self.name = name
        self.age = age
        self.wingspan = wingspan


mybird = Bird("mybird", 2, 4)


print(mybird.move_strategy)
print(type(mybird.move))

mybird.sleep()
mybird.move()