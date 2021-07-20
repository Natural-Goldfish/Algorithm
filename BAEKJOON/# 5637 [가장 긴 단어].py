import sys
import re

text = ''
while text[-6:] != 'E-N-D\n' :
    text += sys.stdin.readline()
text = re.sub(r'[^a-zA-Z-]+', ' ', text)
word_list = sorted(list((word, len(word), index) for index, word in enumerate(text.split(' '))), key=lambda x : (-x[1], x[2]))
print(word_list[0][0].lower())

