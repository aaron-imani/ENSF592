from collections import defaultdict
d = defaultdict(list)
t = d['new key']
print(t)
# []

t.append('new value')
print(d)
# defaultdict(<class 'list'>, {'new key': ['new value']})