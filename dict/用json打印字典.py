# encoding:utf-8
import json
data = {'a': 12, 'b': {'x': 87, 'y': {'t1': 21, 't2': 34}}}
res = json.dumps(data, indent=4)
res1 = json.dumps(data, sort_keys=True, indent=4)
print(res)
print(res1)
