# encoding:utf-8
"""
接口即抽象类基类
在实现类中必须覆盖（重写）掉抽象类的所有方法；否则：TypeError: Can't instantiate abstract class Dog with abstract method move
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def speak(self):
        print("wooof")

    # def move(self):
    #     print("run")


class Cat(Animal):
    def speak(self):
        print("miaow")

    def move(self):
        print("jumping")

dog = Dog()
# dog.speak()
# dog.move()

cat = Cat()
cat.speak()
cat.move()