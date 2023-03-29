# encoding:utf-8


def to_upper(func):
    def wrapper():
        text = func()
        return text.upper()
    return wrapper


@to_upper
def welcome():
    return "welcome"


def hello():
    print("hello")


res = welcome()
print(res)

result = hello()
# print(result)