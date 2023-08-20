row=int(input("enter number of rows\t:"))
for i in range(row,0,-1):
    for j in range(65+i,65,-1):
        print(chr(64+i), end="")
    print('')
