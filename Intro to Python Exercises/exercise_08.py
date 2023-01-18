x = 1
lists = []
lists1 = []
dup = []
notdup = []
while x <= 10:
    num = int(input('Enter a number ' + str(x) + ': '));
    lists.append(num)
    x = x+1

print("Original List: " + str(lists))

for i in lists:
    if i not in lists1:
        lists1.append(i)
    else:
        dup.append(i)

notdup = list(set(lists) - set(dup))
print("Nums that appear once: " + str(notdup))


#resource for the for loop: https://www.educative.io/answers/how-to-find-duplicates-from-a-list-in-python 