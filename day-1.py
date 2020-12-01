
# read text file input
inputFile = open("day-1-input.txt")
file_contents = inputFile.read()
numbersList = file_contents.splitlines()

# cast strings to integers
numbersList = list(map(int, numbersList)) 

# puzzle part 1
for item in numbersList:
    for item2 in numbersList:
        total = item + item2
        if total == 2020:
            number1 = item
            number2 = item2
            break

print ("Number 1: " + str(number1) + ", Number 2: " + str(number2) + " Answer: " + str(number1*number2))

# puzzle part 2
for item in numbersList:
    for item2 in numbersList:
        for item3 in numbersList:
            total = item + item2 + item3
            if total == 2020:
                number1 = item
                number2 = item2
                number3 = item3
                break

print ("Number 1: " + str(number1) + ", Number 2: " + str(number2) + ", Number 3: " + str(number3) + " Answer: " + str(number1*number2*number3))