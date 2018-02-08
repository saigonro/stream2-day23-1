import re
import collections


with open('1155-0.txt') as f:
    text = f.read().lower()

words = re.findall('\w+', text)
big_words = [ word for word in words if len(word) >= 5 ]
print(len(big_words))

print(collections.Counter(big_words).most_common(10))