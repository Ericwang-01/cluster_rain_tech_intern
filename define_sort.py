# encoding:utf-8
"""
sorted的参数
1，iterable 要进行排序的可迭代对象，如列表、元组、集合
2，key 参数需要接受一个函数作为参数，这个函数会在比较时被调用
"""

users = [{"first_name": "zhangsan", "num": 1}, {"first_name": "lisi", "num": 2}]


def get_user_name(user):  # 作为参数传递的是users列表中的元素，而不是整个users列表本身
    return user["first_name"].lower()


def get_sorted_dictionary(users):
    if not isinstance(users, list):
        raise ValueError("Not a correct dictionary")
    if not len(users):
        raise ValueError("Empty dictionary")
    user_by_name = sorted(users, key=get_user_name)
    return user_by_name


if __name__ == '__main__':

    # print(sorted(users, key=get_user_name))  # key 函数在每个元素上执行，以从元素中提取用于排序的值

    print(get_sorted_dictionary(users))
