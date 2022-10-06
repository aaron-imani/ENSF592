class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    # The simple version (Before Type-based dispatch)

    # def __add__(self, other):
    #     seconds = self.to_int() + other.to_int()
    #     return int_to_time(seconds)
    
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    # This method can be removed because we have defined __str__ to tell python how to convert 
    # a Time object into a string. The value can be used for printing the object.
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def add_time(self, other):
        seconds = self.to_int() + other.to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.to_int() > other.to_int()

    def to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


start = Time()
start.hour = 9
start.minute = 45
start.second = 00

start.print_time()
# 09:45:00

# Note: since increment is a pure function, it doesn't modify start.
# Rather, it returns a new Time object.
end = start.increment(1337)
end.print_time()
# 10:07:17

print(end.is_after(start))

time = Time(9, 45)
# The print statement will use the return value from the __str__ method.
print(time)
#09:45:00

duration = Time(1, 45)
# The print statement will cause the __add__ and the __str__ methods to be called respectively.
print(start+duration)
# 11:30:00

# This print statement will use the type-based dispatch as we are trying to add an integer to start.
print(start + 1337)
# 10:07:17