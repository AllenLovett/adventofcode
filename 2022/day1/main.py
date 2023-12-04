# Coding challenge #1
f = open("list.txt", "r")
elves = []
elves_total = []
inventory = f.read().split('\n\n')
for i in range(len(inventory)):
    elves.append(inventory[i].replace('\n',','))

for elf in elves:
    calories = elf.split(',')
    for x in range(len(calories)):
        calories[x] = int(calories[x])
    elves_total.append(sum(calories))

elves_total.sort(reverse=True)
top_3 = slice(3)
print(f'Top elf calories: {elves_total[0]}' )
print(f'Top 3 elves calories: {sum(elves_total[top_3])}')
# Pt 1 Answer is 72478
# Pt 2 Answer is 210367