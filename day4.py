f = open("Inputs/day4", "r")
x = f.readlines()

# Part 1
count=0
for line in x:
    if len(line.strip().split(" ")) == len(set(line.strip().split(" "))):
        count += 1
print(count)

# Part 2
count=len(x)
for line in x:
    l = list(map(set, line.strip().split(" ")))
    for i in l:
        if l.count(i) != 1:
            count -= 1
            break
print(count)
