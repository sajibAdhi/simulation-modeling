# ks test inputting directly value of data

data, ratioPlus, ratioMinus, dPlus, dMinus = [], [], [], [], []
totalData = 0
Dobs = 0

#get file object
f = open("data-set.txt", "r")

while(True):
	#read next line
	line = f.readline()
	#if line is empty, you are done with all lines in the file
	if not line:
		break
	totalData += 1
	#you can access the line
	data.append(float(line.strip()))

#close file
f.close


print("All data :", sorted(data))

for datum in range(totalData):
    ptr = datum + 1

    ratioPlus.append(float(ptr/totalData))
    ratioMinus.append(float(datum/totalData))

    dPlus.append(ratioPlus[datum] - data[datum])
    dMinus.append(data[datum] - ratioMinus[datum])

dPlusMax = max(dPlus)
dMinusMax = max(dMinus)
print(f"D plus max: {dPlusMax}")
print(f"D minus max: {dMinusMax}")

dObs = max(dPlusMax, dMinusMax)
print(f"D obs: {dObs}")

dCritical = float(input("Enter D critical: "))

if dObs <= dCritical:
    print("Test result is Accepted")
else:
    print("Test result is Rejected")
