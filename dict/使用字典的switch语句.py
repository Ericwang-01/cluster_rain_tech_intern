# encoding:utf-8
"""
有多个选项时，不要用多个ifelse  用字典键值对的方式，链接选项和对应的函数
"""
def fun1(x):
    print("1",x)


def fun2(x):
    print("2",x)

def fun3(x):
    print("3",x)


func_dict = {
    "第一个函数": fun1,
    "第二个函数": fun2,
    "第三个函数": fun3
}


def call_func_by_dict(func_name,x):
    func_dict[func_name](x)

call_func_by_dict("第二个函数",5)