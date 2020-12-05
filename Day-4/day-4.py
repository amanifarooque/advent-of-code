import json
import re
import csv

# Part 1 define function to check dict-like string for keys
def checkKeys(string, keys):
    for k in keys:
        if k not in string:
            return False
    return True


# Part 2 define function to turn string to dict
def stringToDict(string):
    output = {}
    key_values = string.replace("{", "").replace("},", "").split(",")

    for v in key_values:
       x = v.split(":")
       output[x[0]] = str(x[1])

    return output


# null checking for dict key
def checkKey(dict, key):
    if key in dict:
        return str(dict[key])
    else:
        return ""

def fixType(string):
    if string:
        if string.isdecimal() and not(string.startswith("0")):
            return int(string)
        else:
            return string
    return None

# function to evaluate rules
def evaluateValues(dict, keys, exportRow):
    temp = {}
    for k in keys:
        if k == "pid":
            temp[k] = checkKey(dict, k)
        else:
            temp[k] = fixType(checkKey(dict, k))
    exportRow.update(temp)

    if temp["byr"] is not None and 1920 <= temp["byr"] <= 2002:
        print("BYR Passes")
    else:
        print("BYR Fails")
        return False

    if temp["iyr"] is not None and 2010 <= temp["iyr"]  <= 2020:
        print("IYR Passes")
    else:
        print("IYR Fails")
        return False

    if temp["eyr"] is not None and 2020 <= temp["eyr"]  <= 2030:
        print("EYR Passes")
    else:
        print("EYR Fails")
        return False

    if temp["hgt"] is not None:
        try:
            if 'cm' in temp["hgt"]:
                print("Evaluating in CM")
                if 150 <= int(temp["hgt"].replace("cm", "")) <= 193:
                    print("HGT Passes")
                else:
                    print("HGT Fails")
                    return False  
            elif "in" in temp["hgt"]:
                print("Evaluating in IN")
                if 59 <= int(temp["hgt"].replace("in", "")) <= 76:
                    print("HGT Passes")
                else:
                    print("HGT Fails")
                    return False
            else:
                print("Invalid Dimension, HGT Fails")
        except:
            return False

    if temp["hcl"] is not None:
        if bool(re.match(r"^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$", temp["hcl"])):
            print("HCL Passes")
        else: 
            print("HCL Fails")
            return False

    eyeColor= [ "amb",  
    "blu", 
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth"
    ]

    if temp["ecl"] in eyeColor:
        print("ECL Passes")
    else: 
        print("ECL Fails")
        return False  

    print(temp["pid"])
    if bool(re.match(r"\d{9}$", temp["pid"])):
        print("PID Passes")
    else: 
        print("PID Fails")
        return False

    # if all checks are passed
    print("all checks passed")
    exportRow["passed?"] = "True"
    
    return True

# read text file input into array of dicts
inputFile = open("input.txt")
file_contents = "[{" + inputFile.read().strip() + "}]"
file_contents  = file_contents.replace('\n\n', '},{').replace(" ", ",").replace("\n", ",").replace('},', '},\n').replace('}]', '').replace('[', '')
documents = file_contents.splitlines()

keys = [
"byr",
"iyr",
"eyr",
"hgt",
"hcl",
"ecl",
"pid"
]



validDocs = 0

# for d in documents:
#     print("Evaluating: " + d)
#     if checkKeys(d, keys):
#         validDocs+=1

export = []
columns = ["row", "passed?"] + keys

for d in documents:
    record = {}
    record["row"] = d

    print("Evaluating: " + d)
    if (checkKeys(d, keys)):
        if (evaluateValues(stringToDict(d), keys, record)):
            validDocs+=1
        print(validDocs)
    else:
        print("Keys not Present")

    export.append(record)

print(validDocs)

with open('debug.csv', "w") as csvfile:
    w = csv.DictWriter(csvfile, columns)
    w.writeheader()
    w.writerows(export)
csvfile.close()