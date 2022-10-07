from named_tuple import Point

def printall(*args, **kwargs):
    print(args, kwargs)

printall(1, 2.0, third='3')
# (1, 2.0) {'third': '3'}

d = dict(x=1, y=2)
print(Point(**d))
# Point(x=1, y=2)