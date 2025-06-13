num = int(input("Enter the number of lines needed:"))
for j in range(1,num+1):
    for x in range(1,j+1):
        print(f'{x} ',end="")
    print()
    
'''
output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''