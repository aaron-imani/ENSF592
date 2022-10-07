def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)

word = 'barcelona'
forbidden1 = 'myth'
forbidden2 = 'alex'

print(avoids(word,forbidden1))
# True

print(avoids(word,forbidden2))
# False