import math

x = 10
y = math.log(x) if x > 0 else float('nan')
print(y)

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

class SampleClass:
    def __init__(self, name, contents=None):
        self.name = name
        self.pouch_contents = [] if contents == None else contents