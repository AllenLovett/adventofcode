import re
f = open("input.txt", "r")

coordinates = f.read().split("\n")
totals = []
for entry in coordinates:
    totals.append(int(str(re.findall('\d', entry)[0])+str(re.findall('\d', entry)[-1])))
print(sum(totals))