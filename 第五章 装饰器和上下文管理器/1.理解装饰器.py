# encoding:utf-8


def to_upper(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return text.upper()
    return wrapper


def add_prefix(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        result = " ".join([text, "larry page"])
        return result
    return wrapper


# 多个装饰器，从内到外执行
# @add_prefix
# @to_upper
# def welcome():
#     return "welcome"

@add_prefix
@to_upper
def say(greet):
    return greet


res = say("may i help you")
print(res)

