# encoding:utf-8
"""
工厂模式是一种创建对象的设计模式，
它通过工厂方法创建对象，根据客户端的需求动态生成不同的实例，
而无需将实例化的类暴露给客户端
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Draw Circle")


class Rectangle(Shape):
    def draw(self):
        print("Draw Rectangle")


class ShapeFactory:
    # 工厂方法: 根据传递的参数返回不同的对象实例
    def get_shape(self, shape_type):
        if shape_type == 'CIRCLE':
            return Circle()
        elif shape_type == 'RECTANGLE':
            return Rectangle()
        else:
            return None


class Client:
    def run(self):
        factory = ShapeFactory()

        circle = factory.get_shape('CIRCLE')
        circle.draw()

        rectangle = factory.get_shape('RECTANGLE')
        rectangle.draw()


client = Client()
client.run()
