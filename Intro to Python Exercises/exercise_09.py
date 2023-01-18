words = []
x = 1
while x <= 5:
    w = str(input('Enter a word: '));
    words.append(w)
    x = x+1

print("Words: " + str(words))
print("One String: " + ' '.join(words))

#reference "join()" from: https://sites.pitt.edu/~naraehan/python3/split_join.html