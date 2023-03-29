# encoding:utf-8
def func():
    print("这个函数没有设返回值，默认为None")
    return "我是返回值"


result = func()
# 1.result是None，不能被调用
print(result)