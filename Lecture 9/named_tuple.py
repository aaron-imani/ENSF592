from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
print(Point)
# <class '__main__.Point'>

p = Point(1, 2)
print(p)
Point(x=1, y=2)

print((p.x, p.y))
# (1, 2)
print((p[0], p[1]))
# (1, 2)

x, y = p
print((x, y))
# (1, 2)

class Pointier(Point):
    """Add more methods here"""