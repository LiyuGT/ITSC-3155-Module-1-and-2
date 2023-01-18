num = int(input('Enter a number: '));
sum = 0
list = []
x = 1
while x <= num:
    num2 = float(input('Enter a number ' + str(x) + ': '));
    sum = sum + num2
    list.append(num2)
    x = x + 1
print(list)
ave = sum/num
print('Average: ' + str(ave))

