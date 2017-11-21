

#def vocab():
uniques = []
text = input("Enter text")
words = text.split(' ')
for each in words:
    if each not in uniques:
        uniques.append(each)
print(uniques)

char_to_int = dict((c, i) for i, c in enumerate(words))
print(char_to_int)

int_to_char = dict((i, c) for i, c in enumerate(words))
print(int_to_char)

