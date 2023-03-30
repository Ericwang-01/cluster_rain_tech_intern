# encoding:utf-8
"""
一个列表生成另一个列表
"""
data = [1, "a", 0, False, True]
filtered_data = filter(None, data)
# filtered_data = [item for item in data if filter(None,data) ]
for i in filtered_data:
    print(i)
print(filtered_data)
