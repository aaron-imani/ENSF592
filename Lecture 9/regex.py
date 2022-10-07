import re

sample_text = ["The Simplest Python Exam Ever.",
               "Python 3.0.", "Good Job Python!"]

for text in sample_text:
    print(re.findall(r'^.+Python (.*)\.$',text))

# ['Exam Ever']
# []
# []

text = 'Just another day in paradise.'
words = text.split()
for word in words:
    if re.search(r'^.[^an].*', word):
        print(word)
# Just

text = 'The book is expensive.'
splitted = re.split('\s', text, 1)
print(splitted)
# ['The', 'book is expensive.']