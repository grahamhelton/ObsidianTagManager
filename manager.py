#! /bin/python3.8
import os
import sys
from colorama import init, Fore
# COLORS
green = Fore.GREEN
reset = Fore.RESET
gray = Fore.LIGHTBLACK_EX
cyan = Fore.CYAN
magenta = Fore.MAGENTA

testFolder = "./testVault/"
def tag():
    # Get Path
    os.chdir(testFolder)
    # For each file in dir, open and prompt user
    for filename in os.listdir():
        taglist = []
        fileRead = open(filename, "r+")
        print(f"{green}{filename.title()} {reset}".center(100,"-"))
        print(fileRead.read())
        print(f"{green}{filename.title()} opened, would you like to add tags? y/n{reset}".center(100,"-"))
        edit = input()
        if "y" in edit:
            # Gets tags to add to file
            tagInput =  input("What tags would you like to add to this?\n")
            # Splits string into words
            tagList = tagInput.split(" ")
            # Iterate a list
            print(f"{cyan}Added tags to bottom of file {reset}\n")
            fileAppend = open(filename, "a")
            for tag in tagList:
                fileAppend.write(" #" + tag)
            fileAppend.close()

# If input contains -t, execute the adding of tags
if "-t" in sys.argv:
    tag()
elif "-s" in sys.argv:
    print("This will be a tag search feature")
else:
    print(f"Currently the only supported arugment is -t for adding tags {cyan}./manger.py -t{reset}")












# Use pandoc to convert from docx to MD
# pandoc -f docx -t gfm GS\ Paper.docx -o file.md

