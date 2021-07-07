# -*- coding: utf-8 -*-

import os, shutil, zipfile,sys

from fileToList import fileToList
from delSpaces import delSpaces
from listToFile import listToFile


# %% Create folder
new_extension='.zip'

folder_src='sdocxFiles'
folder_dest1='zippedFiles'

print("Zip time!")

# Create folder
try:
    os.mkdir(folder_dest1)
    print("Folder "+ folder_dest1 +" created")
    
except FileExistsError:
    print("Warning: folder "+ folder_dest1 +" already exists")



# %% Copy and change extension
try:
    for file in os.listdir(folder_src):
        
        pre, ext = os.path.splitext(file)
        shutil.copy(os.path.join(folder_src,file), os.path.join(folder_dest1,file))
        os.rename(os.path.join(folder_dest1,file), os.path.join(folder_dest1,pre + new_extension))
    print("Files copied in folder " + folder_dest1)
    print("File extension changed to " + new_extension)

except FileNotFoundError:
    print("ERROR: folder "+ folder_src + " does not exist or it's empty")
    sys.exit()

except  FileExistsError:
    print("Warning: file already exist in folder "+ folder_dest1)
    
    # Remove a useless file
    for item in os.listdir(folder_dest1):
        if item.endswith(".sdocx"):
            os.remove(os.path.join(folder_dest1,item))

    


# %% Create another folder

folder_extr='notePnote'

print("\nTxt time!")

# Create folder
try:
    os.mkdir(folder_extr)
    print("Folder "+folder_extr+" created")
except FileExistsError:
    print("Warning: folder "+folder_extr+" already exists")

# %%
# Extract interesting files
try:
    for file in os.listdir(folder_dest1):
        pre, ext = os.path.splitext(file)
        with zipfile.ZipFile(os.path.join(folder_dest1,file), 'r') as zipObj:
            # Extract a single file from zip
            zipObj.extract('note.note', path=folder_extr)
            
            os.rename(os.path.join(folder_extr,'note.note'), os.path.join(folder_extr,pre+'.note' ))    # os.path.join(folder_extr,pre, '.txt')

    print("note.note files copied in folder " + folder_extr)
        
except FileNotFoundError:
    print("ERROR: folder "+ folder_dest1 + " does not exist or it's empty")
    sys.exit()
    
except  FileExistsError:
    print("Warning: files already exist in folder "+ folder_extr)
    
    # Remove a useless file
    for item in os.listdir(folder_extr):
        if item=="note.note":
            os.remove(os.path.join(folder_extr,item))



# %% Rearrange interesting files

print("\nRearranging time!")

totalFile='allNotes.txt'

if os.path.isfile(totalFile)==True:
    print("ERROR: File "+totalFile+" already exists")
    sys.exit()

for file in os.listdir(folder_extr):
    
    # File stored in a list
    text=fileToList(os.path.join(folder_extr,file))

    # Remove useless spaces
    testoR=delSpaces(text)
    
    # Append each list to a file
    listToFile(testoR, os.path.join(folder_extr,file), totalFile)


print("Done")




