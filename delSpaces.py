# -*- coding: utf-8 -*-

 
def delSpaces(text):

    textOk=[]
    
    for line in text:
        lineOk=[]
        
        # for count in range(1,len(line)-1, 2):
        for count in range(1,len(line)):

            # Useful characters
            if not line[count].isprintable():
                continue
            
            if count>0 and line[count].isspace()==True and line[count-1].isspace()==True:
                continue
            
            
            lineOk.append("".join(line[count]))

        textOk.append("".join(lineOk))
        textOk.append("\n")
          
    return textOk

