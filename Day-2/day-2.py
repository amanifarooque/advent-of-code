# read text file input
inputFile = open("input.txt")
file_contents = inputFile.read()
passwords = file_contents.splitlines()

validPasswords1 = 0
validPasswords2 = 0

for p in passwords:
    # set vars
    passedRuleOne = 0
    passedRuleTwo = 0
    ruleRange = []
    ruleChar = ""

    # parse rules
    rule = p.split(":")[0]
    ruleRange = rule.split(" ")[0].split("-")
    ruleRange = list(map(int, ruleRange)) 
    ruleChar = rule.split(" ")[1]

    password =  p.split(":")[1].strip()

    # Part 1
    if ruleRange[0] <= password.count(ruleChar) <= ruleRange[1]:
        validPasswords1+=1
        print("Password " + password + " passes rule " + str(rule))
    else:
        print("Password " + password + " does not pass rule " + str(rule))

    # Part 2
    if password[(ruleRange[0]-1)] == ruleChar:
        passedRuleOne = 1 
    if password[(ruleRange[1]-1)] == ruleChar: 
        passedRuleTwo = 1

    if (passedRuleOne + passedRuleTwo) == 1:
        validPasswords2+=1
        print("Part 2: Password " + password + " passes rule " + str(rule) + "\n")
    else:
        print("Part 2: Password " + password + " does not pass rule " + str(rule)+ "\n")

# Part 1 Answer is 418
print(str(validPasswords1) + " valid passwords for Part 1.")

# Part 2 Answer is 616
print(str(validPasswords2) + " valid passwords for Part 2.")



