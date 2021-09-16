#! /bin/python3.8
import os
from colorama import init, Fore
# COLORS
green = Fore.GREEN
reset = Fore.RESET
gray = Fore.LIGHTBLACK_EX

testFolder = "./testVault/"

# Use pandoc to convert from docx to MD
# pandoc -f docx -t gfm GS\ Paper.docx -o file.md

# Get Path
os.chdir(testFolder)
# For each file in dir, open and prompt user
for filename in os.listdir():
    taglist = []
    fileRead = open(filename, "r+")
    print(fileRead.read())
    edit = input(filename + " opened, do you want to add tags? Y/N")
    if "y" in edit:
        # Gets tags to add to file
        tagInput =  input("What tags would you like to add to this?")
        # Splits string into words
        tagList = tagInput.split(" ")
        # Iterate a list
        print(f"{green}     Adding tags to bottom of file {reset}", end = "\r")
        fileAppend = open(filename, "a")
        for tag in tagList:
            fileAppend.write(" #" + tag)

        fileAppend.close()


