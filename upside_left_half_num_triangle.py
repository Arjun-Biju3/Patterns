num = int(input("Enter the number of lines needed:"))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j," ",end="")
    print()

'''
output:
1  2  3  4  5  
1  2  3  4
1  2  3
1  2
1
'''