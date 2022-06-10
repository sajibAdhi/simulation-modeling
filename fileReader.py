#get file object
f = open("data-set.txt", "r")
dataSize = 0
while(True):
	#read next line
	line = f.readline()
	#if line is empty, you are done with all lines in the file
	if not line:
		break
	dataSize += 1
	#you can access the line
	print(line.strip())

#close file
f.close