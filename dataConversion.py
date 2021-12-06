#Takes in the txt file, reads the lines in the txt file, and stores everything into a JSON.

import json
import os

def convert(ctxt, cjson):
    # Creating a Python Dictionary
    computerInfo = {}
    # Opens the text file
    file = open(ctxt, "r")
    lines = file.readlines()[4:]  # Skips the first 4 lines

    cNum = 1
    for line in lines:
        comp = "Device " + str(cNum)
        cNum = cNum + 1
        x = line.split(" ") # Seperates by a single space
        a = comp
        b = {"MAC Address": x[-3], "IP": x[-1][:-1], "Status": "Online"}
        computerInfo[comp] = b

    # print(computerInfo)
    # print(computerInfo['Computer 2']['IP'])

    # Creates a JSON File of the dictionary 'computerInfo'
    with open(cjson, 'w') as fp:
        json.dump(computerInfo, fp)
    print(f"Converted into {cjson}!")
    file.close()
    fp.close()

#If the REPEAT.txt exists, convert to JSON
if os.path.exists("REPEAT.txt"):
    print("\nREPEAT.txt exists!")
    ctxt = "REPEAT.txt"
    cjson = "REPEAT.json"
    convert(ctxt, cjson)
#If REPEAT.txt does not exist, create the MASTER JSON which will be used for comparison with the REPEAT JSON for device availability
else:
    print("\nREPEAT.txt does not exist!")
    ctxt = "MASTER.txt"
    cjson = "MASTER.json"
    convert(ctxt, cjson)
