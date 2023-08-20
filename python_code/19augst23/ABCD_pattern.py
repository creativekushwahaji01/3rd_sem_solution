row=int(input("enter number of rows\t:"))
for i in range(0,row+1):
    for j in range(0,i):
        print(chr(65+j),end="")
    print('')
