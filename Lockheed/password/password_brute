import string
import random

arr = string.ascii_letters
total = 0
myString = ""
while total != 1000:
    myString = ""
    total = 0
    while len(myString) != 10:
        myString += random.choice(arr)
    
    for c in myString:
       total += ord(c)
    if ord(myString[1]) != 83:
        total = 0
        
print(myString)