import re

def checkChars(string, allowedChars):
    charsPresent = []
    for c in allowedChars:
        if c in string:
            charsPresent.append(c)
    return charsPresent

# read text file input into arrays
inputFile = open("input.txt")
file_contents = "[" + inputFile.read().strip() + "]"
file_contents  = file_contents.replace('\n\n', ']\n[').replace("\n", ",").replace('],', ']\n')
responses = file_contents.splitlines()
# print(responses)


## Part 1
# totalResponses = 0
# for r in responses:
#     uniqueResponses = re.sub('[^a-zA-Z0-9 \n\.]', '', "".join(set(r)))
#     totalResponses+= len(uniqueResponses)
#     print(uniqueResponses + ": " + str(len(uniqueResponses)))

# print(totalResponses)


## Part 2
totalResponses = 0

for r in responses:
    answers = re.sub('[^a-zA-Z0-9, \n\.]', '', r).split(",")
    print(answers)

    allowedChars = answers[0]

    for a in answers:
        allowedChars = checkChars(a, allowedChars)
    
    totalResponses+=len(allowedChars)
    
print(totalResponses)
