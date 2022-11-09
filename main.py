import os
import tools

if os.path.isdir("logs") == False:
    try:
        os.mkdir("logs")
        print("logs folder successfully created!")
        
    except Exception as e:
        print("An error has occured! Err: " + e)


print("Welcome to the LogChecker made by SleepySpeller on GitHub!\nWhat would you like to do?\n1. Download the files from an FTP Server and then scan them\n2. Scan the existing logs from a folder (logs must be extracted from the zip file)")

answer = input("Type here > ")

if answer == "1":
    
    print("Downloading logs")
    tools.Functions.downloadLogs()
    print("Extracting logs...")
    tools.Functions.extractLogs()
    print("Done! Running the search tool!")
    tools.Functions.search()
elif answer == "2":
    print("Running our search tool...")
    tools.Functions.search()
