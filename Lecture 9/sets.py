# Without using set

# def has_duplicates(t):
#     d = {}
#     for x in t:
#         if x in d:
#             return True
#         d[x] = True
#     return False

def has_duplicates(t):
    return len(set(t)) < len(t)

# Without using sets

# def uses_only(word, available):
#     for letter in word:
#         if letter not in available:
#             return False
#     return True

def uses_only(word, available):
    return set(word) <= set(available)

def avoids(word, forbidden):
    return len(set(word) - set(forbidden)) == len(set(word))

d = ['Alex', 'Sam', 'Alex']
s = set(d)
# {'Sam', 'Alex'}

print(has_duplicates(d))
# True

print(uses_only('alex','alexanderjhdfhldherynbsdf'))
# True
print(uses_only('alex','alph'))
# False

print(avoids('Alex', 'Sam'))
# True
print(avoids('Alex', 'Saul'))
# False