import re
file = open("regex_sum_588840.txt") #or "regex_sum_588840.txt"
file = file.read()
y = re.findall('[0-9]+', file)
sum = 0
for i in y:
    num = int(i)
    sum = sum + num
print(sum)