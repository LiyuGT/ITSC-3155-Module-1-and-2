row = int(input('Enter a row num from 1 to 5: '));
col = int(input('Enter a col num from 1 to 5: '));

a = [[0 for x in range(5)] for x in range(5)]
a[row -1][col-1] = 1
#print(a)

for i in range(len(a)) : 
    for j in range(len(a[i])) : 
        print(a[i][j], end=" ")
    print()


#Used an online resource for the matrix format: https://www.quora.com/How-do-I-write-a-code-to-find-the-common-terms-between-2-arrays-in-Python
