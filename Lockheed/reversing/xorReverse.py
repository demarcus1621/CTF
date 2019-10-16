array = [106, 255, 184, 238, 0, 32, 77, 255, 37, 60, 23, 101, 47]
compareArray = [57, 180, 225, 195, 69, 108, 14, 182, 8, 11, 39, 87, 25]
tempString = ""
for i in range(len(array)):
    tempString += chr(array[i] ^ compareArray[i])

print tempString
