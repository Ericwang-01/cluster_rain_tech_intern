# encoding:utf-8
'''
使得对私有属性的访问和修改像访问和修改普通属性一样
'''
class MyClass:
    def __init__(self, pub, pri):
        self.pub = pub
        self.__pri = pri

    @property
    def pri(self):
        return self.__pri

    @pri.setter
    def pri(self, value):
        self.__pri = value


obj = MyClass("public", "private")

print(obj.pub)  # 输出: "public"
# print(obj.__pri) #报错 AttributeError: 'MyClass' object has no attribute '__pri'

print(obj.pri)  # 输出: "private"
obj.pri = "new private"
print(obj.pri)  # 输出: "new private"




