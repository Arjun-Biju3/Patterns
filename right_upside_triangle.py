num = int(input("Enter the number of lines needed:"))
for i in range(num,0,-1):
    print(" " * (num-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
    
'''
output:
*****
 ****
  ***
   **
    *
'''