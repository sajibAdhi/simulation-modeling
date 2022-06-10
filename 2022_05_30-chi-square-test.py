import math

# chi square test inputting directly value of Oi
totalData = 0
nums = []

userOrFile = input("Enter 'user' to input values manually or 'file' to input values from a file: ")

if userOrFile == 'user':
    totalData = int(input("Enter total data: "))

    for ptr in range(totalData):
        tempOi = float(input(f"Enter Oi for class no {ptr + 1}: "))
        nums.append(tempOi)
else:
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
        tempOi = float(line.strip())
        nums.append(tempOi)

    #close file
    f.close


totalClass = round(math.log(totalData) / math.log(2))
print("Total class: ", totalClass)

rangeValue = round((max(nums) - min(nums)) / totalClass, 3)
print("Range difference: ", rangeValue)

# calculate all classes ranges
classRanges = {}
firstStart = min(nums)
firstEnd = round(firstStart + rangeValue, 3)

classStart = [firstStart]
classEnd = [firstEnd]

for ptr in range(1, totalClass + 1):
    classStart.append(firstEnd)
    firstEnd += rangeValue
    firstEnd = round(firstEnd, 3)
    classEnd.append(firstEnd)

classRanges = {'start': classStart, 'end': classEnd}

flag = 0
oiList = []

# calculate oi for each class
print()
print("Class \t\t   | \tOi")
print("_______________|_____________")
for start in classRanges['start']:
    oi = 0
    for ptr in range(totalData):
        if start <= nums[ptr] < classRanges['end'][flag]:
            oi += 1
    print(f"{start} - {classRanges['end'][flag]}  | {oi}")
    oiList.append(oi)
    flag += 1

# calculate chi square
Dobs = 0

for datum in oiList:
    Dobs += pow((datum - totalClass), 2) / totalClass

print("D obs is: ", round(Dobs, 4))

Dcritical = float(input("Enter D critical: "))

if Dobs <= Dcritical:
    print("Test result is Accepted")
else:
    print("Test result is Rejected")