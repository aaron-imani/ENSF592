from collections import Counter
count = Counter('parrot')
print(count)
# Counter({'r': 2, 't': 1, 'o': 1, 'p': 1, 'a': 1})

print(count['d'])
# 0

for val, freq in count.most_common(3):
    print(val, freq)
# r 2
# p 1
# a 1