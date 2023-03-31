# encoding:utf-8


class Account(object):
    def __init__(self, account, password, balance):
        self.account = account
        self.password = password
        self.balance = balance

    def __str__(self):
        return f"您的账户是{self.account},密码是{self.password},余额为{self.balance}"