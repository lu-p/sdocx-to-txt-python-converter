# -*- coding: utf-8 -*-

import os

def listToFile(listOfStrings, fileName, totalFile):
# Append notes to a main file

    usefulName=os.path.splitext(fileName)[0]
    usefulName=os.path.basename(usefulName)

    count=0
    newLine=False
    with open(totalFile, "a", encoding='ANSI') as f:
        # f.write(usefulName)
        
        # Write date of notes from fileName
        # f.write(usefulName[:5] + " " + usefulName[10]+usefulName[11] + " "+ usefulName[8]+usefulName[9] + " " + "20"+usefulName[6]+usefulName[7]+"\n")
        
        for line in listOfStrings:
            for carattere in line:
                f.write(carattere)
                count+=1
                
                if count==90:
                    newLine=True
                
                if newLine==True and carattere.isspace()==True:
                    f.write("\n")
                    count=0
                    newLine=False
        f.write("\n\n")

