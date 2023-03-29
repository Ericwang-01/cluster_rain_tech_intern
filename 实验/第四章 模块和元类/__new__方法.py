# encoding:utf-8
from abc import abstractmethod, ABCMeta


class UserAbstract(metaclass=ABCMeta):
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        given_data = args[0]
        # 验证数据
        if not isinstance(given_data, str):
            raise ValueError(f"Please provide string:{given_data}")
        return obj


class User(UserAbstract):
    def __init__(self, name):
        self.name = name

user = User('wang')