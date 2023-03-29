# encoding:utf-8
import pprint
data = {'a': 12, 'b': {'x': 87, 'y': {'t1': 21, 't2': 34}}}
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)