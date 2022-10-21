import re
import os

username = input("What's the username of the player?")
location = input("What's the directory name of the logs?")
commands = input("What commands would you like to search for? (put , between commands, leave empty for default)")

rgx = f".*(?:{username}).*(?:"
o = 0
i = 0

if commands == "":
    rgx = f".*(?:{username}).*(?:\/gmsp|\/gmc|\/gamemode|\/give|\/summon|fly|\/enchant|\/heal).*"
else:
    rgxlist = commands.split(",")
    
    i = len(rgxlist)-1

    for command in rgxlist:
        if o < i:  
            rgx = rgx + f"\/{command}" + "|"
            o += 1
        elif o == i:
            rgx = rgx + f"\/{command}"
        
    
    rgx = rgx + ").*"

folderList = os.listdir(location)
gmcCounter = 0

for logname in folderList:
    openfile = open("logs/" + logname)
    
    results = re.findall(rgx, openfile.read())
    
    if results != []:
        for line in results:
            print(line)
        gmcCounter += len(results)
    
print(f"{username} has used illegal commands " + str(gmcCounter) + " times!")
os.system("pause")

    
