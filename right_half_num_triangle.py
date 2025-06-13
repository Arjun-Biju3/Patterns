num = int(input("Enter the number of lines needed:"))
for i in range(1,num+1):
    print(" " * (num - i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
    
'''
output
    1
   12
  123
 1234
12345
'''