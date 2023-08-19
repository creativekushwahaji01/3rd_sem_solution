row=int(input('Enter number of rows\t'))
for i in range(1,row):
	for j in range(65,65+i):
		print(chr(j),end='')
	print('')
