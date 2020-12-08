def runProgram(inputRules, accumulator = 0):
    i = 0
    visitedIndices = []
    infiniteProgram = False

    while (i < len(inputRules)):
        operator = inputRules[i][0]
        value = inputRules[i][1]

        if (operator == "acc"):
            accumulator+=value
            i+=1

        if (operator == "nop"):
            i+=1

        if (operator == "jmp"):
            i+=value

        if (i in visitedIndices):
            infiniteProgram = True
            break
        
        visitedIndices.append(i)    
    return [accumulator, infiniteProgram]

# read text file input into an array
inputFile = open("input.txt")
file_contents = inputFile.read().strip().splitlines()

operations = []
accumulator = 0

for f in file_contents:
    operations.append([f.split(" ")[0], int(f.split(" ")[1].replace("+", ""))])

print(runProgram(operations))

for index, item in enumerate(operations): 
    if item[0] == 'jmp': 
        testOperations = list(operations)
        testOperations[index] = ["nop", 0]
        output = runProgram(testOperations)
        if output[1] == False:
            print(output)

for index, item in enumerate(operations): 
    if item[0] == 'nop': 
        testOperations = list(operations)
        testOperations[index] = ["jmp", 0]
        output = runProgram(testOperations)
        if output[1] == False:
            print(output)


