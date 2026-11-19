# Andrew Mcdaniel
# python 2026 
# lab 5 - 11/19/26

def temp_coversion_table():
    #this opens to document that the temp conversion chart will be outputed to
    with open("C:\\Users\\mcdan\\OneDrive\\Desktop\\Python Class\\Python Class Lab 5\\tempConvert.txt", "w") as outfile:
        #this will pritn out the top guide line
        outfile.write(f"{'fahrenheit':>10}{'celsius':>10}\n")
        # this loop will out put the temp in fahrenheit and it's celsius coversion up to three decimals
        for f in range(-300, 213):
            c = (f - 32) *5 / 9
            # writes directly into the out file
            outfile.write(f"{f:10.3f}{c:10.3f}\n")

# runs the function
temp_coversion_table()