# Camel case
#!/bin/python3

import sys


s = input().strip()
tempstr="";
wordsList=[]

for x in s:
    if (x.isupper()):
        # Upper case letter found print the string
        wordsList.append(tempstr)
        tempstr="";
        tempstr += x
    else:
        tempstr += x
if (tempstr !=""):
    wordsList.append(tempstr)
print(len(wordsList))