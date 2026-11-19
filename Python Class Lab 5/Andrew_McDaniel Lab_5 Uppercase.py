# Andrew Mcdaniel
# python 2026 
# lab 5 - 11/19/26

# open the text file for reating then writes to the outputfile the for loop makes all the lines uppercase
with open("C:\\Users\\mcdan\\OneDrive\\Desktop\\Python Class\\Python Class Lab 5\\regular.txt","r" ) as textFile, open("C:\\Users\\mcdan\\OneDrive\\Desktop\\Python Class\\Python Class Lab 5\\uppercase.txt", "w") as outFile:
    for line in textFile:
        outFile.write(line.upper())


