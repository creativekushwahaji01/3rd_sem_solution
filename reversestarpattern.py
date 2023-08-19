row=int(input("enter number of rows\t:"))
for i in range(row+1,0,-1):
    for j in range(i,0,-1):
        print("*", end="")
    print('\n')
