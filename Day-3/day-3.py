# read text file input
inputFile = open("input.txt")
file_contents = inputFile.read()
puzzle = file_contents.splitlines()

# define function to check slope given list & x/y inputs
def checkSlope(list, x, y):
    xCoordinate = 0
    treeCount = 0
    rowLength = len(list[0])
    for index, item in enumerate(list):
        if index > 0 and (index % y == 0):
            xCoordinate+=x
            r = xCoordinate % rowLength

            # print("Index: " + str(index) + ", Line: " + str(item) + ", X: " + str(x) + ", R: " + str(r) + ", Char at R: " + str(item[r]))
            if item[r] == "#":
                treeCount+=1
    return treeCount

# list of slopes for part 2
slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

answer = 1
numTrees = 0

for s in slopes:
    numTrees = checkSlope(puzzle, s[0], s[1])
    print("Slope " + str(s) + ": " + str(checkSlope(puzzle, s[0], s[1])))
    answer *= numTrees

print(answer)

