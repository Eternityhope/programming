number = []

import re
try:
    fhand = open("c:/mbox.txt")
except:
    print("File cannot be opened")
    exit()
count = 0 
for line in fhand:
    line = line.rstrip()
    if re.search('New Revision:',line):
        #print(line)
        count = count + 1
        texts = line.split()
        text = texts[-1]
        number.append(text)

int_list = map(int,number)
sum_list = sum(int_list)
avr = sum_list / count


print("total %d lines are matched" % count)
print("Average: %.4f" % avr)