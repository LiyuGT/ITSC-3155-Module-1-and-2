lists = []
word = str(input('Enter a string: '));
lists = list(word)
#print(lists)
listSplit = [lists[x:x+3] for x in range(0, len(lists), 3)]
print(listSplit)


#referenced line 6 from: https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists