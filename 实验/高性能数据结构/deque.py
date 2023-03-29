# encoding:utf-8
from collections import deque
'''
创建队列和栈的时候考虑
'''
double_end_queue = deque("dhjasfdljhf")
# iterate over the deque element
# double_end_queue.pop()
double_end_queue.append('a')
for item in double_end_queue:
    print(item.upper(), end='')

