# encoding:utf-8
"""
为不存在的键提供默认值
避免向dict一样抛出KeyError的异常
"""
from collections import defaultdict

colors = defaultdict(int)  # 默认键值的数据类型是int
colors["green"] = 3  # 常规赋值
print(colors["orange"])  # 不存在的键会附默认值0
print(colors["red"])
print(colors)
print(type(colors))