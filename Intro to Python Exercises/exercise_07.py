input1 = "start"
nums = []
even = []
while input1 != "QUIT": 
    input1 = str(input('Enter a number or QUIT to quit: '));
    if input1.isdigit():
         nums.append(int(input1))
         if (int(input1) %  2) == 0:
            even.append(int(input1))

print("All Nums: " + str(nums))
print("Even Nums: " + str(even))
