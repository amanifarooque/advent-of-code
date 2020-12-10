# evaluate invalid numbers in list
def validateNumbers(listNumbers, preambleLength):
    invalidNumbers = []
    for index, item in enumerate(listNumbers):
        if index > (preambleLength - 1):
            validInputs = listNumbers[(index-preambleLength):index]
            isValid = False

            for v in validInputs:
                for i in validInputs:
                    if v != i:
                        if item == i+v:
                            isValid = True
            
            if not isValid:
                invalidNumbers.append(item)
    return invalidNumbers

def findSet(listNumbers, number):
    answerSet = []
    total = 0

    for index, item in enumerate(listNumbers):
        total = sum(answerSet)

        if (index+1) < len(listNumbers):
            nextNumber = listNumbers[index+1]
        else:
            break

        answerSet.append(item)

        for index2, item2 in enumerate(listNumbers[nextNumber:]): 
            total = sum(answerSet)
            answerSet.append(item2)
            

            if total > number:
                answerSet = []
                total = 0
                break
            elif total == number:
                print("found in inner loop")
                break           
        if total == number:
            print("found in outer loop")
            break

    print("Answer Set " + str(answerSet) + ", Total: " + str(total))           
    return(answerSet)
    

    

    

# read file
inputFile = open("input.txt")
numbers = list(map(int, inputFile.read().strip().splitlines()))

keyNumber = validateNumbers(numbers, 25)[0]

left = 0
right = len(numbers)-1
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if sum(numbers[i:j]) == keyNumber:
            if i == j-1 : continue
            print(f"Part Two: {min(numbers[i:j]) + max(numbers[i:j])}")

