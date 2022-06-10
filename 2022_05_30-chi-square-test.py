# chi square test inputting directly value of Oi
totalData = 0
Oi = []
N = 0
Dobs = 0

userOrFile = input("Enter 'user' to input values manually or 'file' to input values from a file: ")

if userOrFile == 'user':
    totalData = int(input("Enter total data: "))

    for ptr in range(totalData):
        tempOi = float(input(f"Enter Oi for class no {ptr + 1}: "))
        Oi.append(tempOi)
        N += tempOi
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
        Oi.append(float(line.strip()))
        N+= float(line.strip())

    #close file
    f.close

print("All Oi :", Oi)
Ei = N / totalData

for datum in Oi:
    Dobs += pow((datum - Ei), 2) / Ei

print("D obs is: ", Dobs)

Dcritical = float(input("Enter D critical: "))

if Dobs <= Dcritical:
    print("Test result is Accepted")
else:
    print("Test result is Rejected")
