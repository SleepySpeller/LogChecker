import os
from ftplib import FTP
import gzip
import re

class Functions():
    def __init__(self):
        pass
    
    def extractLogs():
        files = os.listdir("logs")
        for item in files:
            if item == "latest.log":
                continue
            with gzip.open("logs/"+item, 'rb') as f:
                try:
                    file_content = f.read()
                except Exception:
                    print("Failed to extract " + item + ", skipping...")
                    continue
                with open("logs/"+item[:-3], 'wb') as f:
                    f.write(file_content)
            os.remove("logs/"+item)
            
    def downloadLogs():
            address = input("What's the address to the server?")
            username = input("What's the username on the FTP Server?")
            password = input("What's the password for the FTP Server?")
        
            try:
                ftp = FTP(address)
            except ConnectionRefusedError as e:
                print("An error has occured! The connection cannot be established becase the target machine refused it")  
                os.system("pause")
                quit
            except ConnectionResetError:
                print("An error has occured! The connection has been reset.")
                os.system("pause")
                quit
            except ConnectionError as e:
                print("An unknown connection error has occured!\n More info: " + e)
                os.system("pause")
                quit
            
            ftp.login(user=username, passwd=password)

            ftp.encoding = "utf-8"
            ftp.cwd("/logs")
            dirLogs = ftp.nlst("/logs")
            
            for item in dirLogs:
                with open("logs/" + item, "wb") as file:
                    ftp.retrbinary(f"RETR {item}", file.write)
                    
                if os.path.isfile("logs/" + item[:-3]):
                    print("Found an log with the same name, replacing it with the new one...")    
                    os.remove("logs/" + item[:-3])
            ftp.quit()            
            
    def search():
            username = input("What's the username of the player?")
            commands = input("What commands would you like to search for? (put , between commands, leave empty for default)")

            rgx = f".*(?:{username}).*(?:"
            o = 0
            i = 0

            if commands == "":
                rgx = f".*(?:{username}).*(?:\/gmsp|\/gmc|\/gamemode|\/give|\/summon|\/fly|\/enchant|\/heal|\/effect).*"
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

            folderList = os.listdir("logs")
            gmcCounter = 0

            for logname in folderList:
                openfile = open("logs/"+ logname)
                
                results = re.findall(rgx, openfile.read())
                
                if results != []:
                    for line in results:
                        print(line)
                    gmcCounter += len(results)
                
            print(f"{username} has used illegal commands " + str(gmcCounter) + " times!")
            os.system("pause")