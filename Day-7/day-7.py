
def findBag(bagColor, bagDict):
    return [c for c in bagDict if bagColor in bagDict[c]]

def findBagRecursive(bagColor, bagDict):
    validBags = {bagColor}
    additionalBags = True

    while additionalBags:
        additionalBags = False
        for bag in list(validBags):
             for parentBag in findBag(bag, bagDict):
                 if parentBag not in validBags:
                     validBags.add(parentBag)
                     additionalBags = True

    return validBags - {bagColor}

def countAllBags(bagColor, bagDict):
    bagCount = 0
    for bag, count in bagDict[bagColor].items():
        bagCount += count + count * countAllBags(bag, bagDict)
    return bagCount
    



# read text file input into arrays
inputFile = open("input.txt")
file_contents = inputFile.read().strip()
rules = file_contents.splitlines()

rulesDict = {}

for r in rules:
    parentBag = r.split("contain")[0].strip().replace(" bags", "")
    childBagList = r.split("contain ")[1].replace(".", "").split(", ")
    childBags = {}
    for bag in childBagList:
        if bag != "no other bags":
            childBags[bag[2:(len(bag))].replace(" bags", "").replace(" bag", "")] = int(bag[0])

    rulesDict[parentBag] = childBags

print(rulesDict)


# acceptableBags = findBagRecursive("shiny gold", rulesDict)
# print(len(acceptableBags))

print(countAllBags("shiny gold", rulesDict))


