# PART 2 - DATA STRUCTURES

# 1. Opening a File - before we can read the contents of the file we must tell python which file we are going to work with and what we will be doing with the file. This is done with the: open() function
# Open() returns a "file handle" - a variable used to perform operations on the file
# Similar to "File -> Open" in a Word Processor 
# handle = open("filename", "mode(read or write)"") - if we leave without mode then it's read by default
# filename is a string 

# The newline Character (\n) - indicate when the line ends and to get it must use Print(). It is one character not two. 

stuff = "Johnas\nChami"
stuff 
print(stuff)
len(stuff)

# 2. Read a File 
# A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence 
# We can use the FOR statement to iterate through a sequence 

xfile = open("mbox.txt")
for cheese in xfile:
    print(cheese)

# Counting Lines in a file 
fhand = open("mbox.txt")
count = 0
for line in fhand:
    count = count + 1 
print("Line Count:", count)

# Reading the *Whole* File 
fhand = open("mbox-short.txt")
inp = fhand.read()
print(len(inp))

# Searching through a File
fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("From:") :
        print(line)   # here print() will leave a space because of default \n 

# Remove newline with strip() from the string library. Newline is like a whitespace
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:") :
        print(line)  

# Skipping with CONTINUE
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:") :
        continue
    print(line)

# Using IN to select lines
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not "uct.ac.za" in line :
        continue
    print(line) 
   
# Prompt for File Name
fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("Subject: ") :
        count = count + 1
print("There were", count, "subject lines in", fname)

# Bad File Names
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
    
count = 0
for line in fhand:
    if line.startswith("Subject: ") :
        count = count + 1
print("There were", count, "subject lines in", fname)












