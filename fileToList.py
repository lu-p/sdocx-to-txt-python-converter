# -*- coding: utf-8 -*-

import sys


def fileToList(fileName):

    try:
        testoFile=[]
        with open(fileName, "r", encoding='cp1252', errors='replace') as f:
            for line in f:
                testoFile.append(line)
                
        return testoFile
    
    except FileNotFoundError:
        print("ERROR: File "+ fileName +" does not exist")
        return sys.exit()
    
