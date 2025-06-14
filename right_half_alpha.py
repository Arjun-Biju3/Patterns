num = int(input("Enter the number of lines needed:"))
for i in range(num):
    print(" " * (num - i),end="")
    for j in range(i+1):
        print(chr(65 + j),end="")
    print()
    
'''
output:
     A
    AB
   ABC
  ABCD
 ABCDE
'''