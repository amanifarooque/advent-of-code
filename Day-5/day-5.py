import math

def returnRange(indicator, range):
    if indicator in ["F", "L"]:
       range[1] = math.floor((range[0]+range[1])/2)
    elif indicator in ["B", "R"]:
       range[0] = math.ceil((range[0]+range[1])/2) 
    return range

def findSeats(L):
    start, end = L[0], L[-1]
    return sorted(set(range(start, end + 1)).difference(L))

# read text file input
inputFile = open("input.txt")
file_contents = inputFile.read()
puzzle = file_contents.splitlines()

testInput = [
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL"
]

# initialize variables
highestSeat = 0
seatIds = []

for item in puzzle:    
    rowRange = [0,127]
    columnRange = [0,7]

    for char in item[0:7]:
        rowRange = returnRange(char, rowRange)
    for char in item[7:10]:
        columnRange = returnRange(char, columnRange)

    seatId = (rowRange[0]*8) + columnRange[0]

    if seatId > highestSeat:
        highestSeat = seatId
    
    seatIds.append(seatId)

## Part 1
print(highestSeat)

## Part 2
seatIds.sort()
print(findSeats(seatIds))