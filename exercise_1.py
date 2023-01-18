
word = input("Enter a String: ")
lists = ([*word])
lists.remove(" ")
print(lists)

lower = []
upper = []
i = 0
while i < len(word) -1:
    if lists[i].islower():
        lower.append(lists[i])
    else: 
        upper.append(lists[i])
    i = i+1

print("lower: " + ''.join(lower))
print("upper: " + ''.join(upper))

print(''.join(lower)+''.join(upper))