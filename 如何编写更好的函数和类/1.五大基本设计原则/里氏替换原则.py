# encoding:utf-8
"""
基类可以被子类替换，而不会影响程序的正确
Bird类继承了Animal类中的所有属性和方法，并且添加了一个新的方法fly。因此，可以在程序中使用Bird对象代替Animal对象，而不会影响程序的正确性
"""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def move(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)  # 继承父类的属性
        self.wingspan = wingspan  #

    def fly(self):
        print(f"{self.name} is flying.")
