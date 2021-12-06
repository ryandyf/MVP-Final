#compare the master json file to the REPEAT json file
#if a new IP is in the scanned JSON file and not the master, it needs to be added. (Just do append)

import json

#open the two JSON files
masterFile = open("MASTER.json")
newFile = open("REPEAT.json")

#Convert them into variables
masterData = json.load(masterFile)
newData = json.load(newFile)


#set everything to offline here
#Loop through the master file and turn everything off
for i in masterData:
    masterData[i]["Status"] = "Offline"

#Create tracker boolean
tracker = False

#Loop through the new data inputs, then loop through the master inputs to compare
#If compare is true, then that device is online.
#If compare doesn't exist, the device is offline.
#If the newData has a new device, it gets added to the master JSON
for i in newData:
    tracker = False
    #print(newData[i])
    for x in masterData:
        if newData[i]["MAC Address"] == masterData[x]["MAC Address"]:
            masterData[x]["Status"] = "Online"
            tracker = True
            break
    if tracker == False:
        masterData[("Device " + str(len(masterData) + 1))] = newData[i]


#Dump the updated master back into the same file
with open('MASTER.json', "w") as file:
    json.dump(masterData, file)
masterFile.close()
newFile.close()
file.close()
