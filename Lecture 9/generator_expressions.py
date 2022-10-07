g = (x**2 for x in range(5))
print(g)
# <generator object <genexpr> at 0x7f4c45a786c0>

print(next(g))
# 0
print(next(g))
# 1

for val in g:
    print(val)
# 4
# 9
# 16

next(g)
# StopIteration

sum(x**2 for x in range(5))
# 30