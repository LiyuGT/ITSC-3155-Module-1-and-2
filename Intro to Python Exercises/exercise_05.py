
list1 = []
list2 = []
clist = []
x = 1
y = 1
z = 1
while x <= 5:
    num1 = int(input('Enter a number for the first list: '));
    list1.append(num1)
    x = x + 1
while y <= 5:
    num2 = int(input('Enter a number for the second list: '));
    list2.append(num2)
    y = y + 1
print("First List: " + str(list1))
print("Second List: " + str(list2))

clist = set(list1).intersection(set(list2))
#referenced online resource for line 19: https://www.quora.com/How-do-I-write-a-code-to-find-the-common-terms-between-2-arrays-in-Python
print("Common List: " + str(clist))