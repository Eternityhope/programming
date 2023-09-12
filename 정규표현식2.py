import re
try:
    fhand = open("C:\mbox.txt")
except:
    print("File cannot be opened")
    exit()
count = 0 
for line in fhand:
    line = line.rstrip()
    if re.search('^From:.+@',line):
        print(line)
        count = count + 1
print("total %d lines printed" % count)