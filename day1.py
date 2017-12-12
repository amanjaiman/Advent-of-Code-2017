f = open("Inputs/day1", "r")
x = f.readline()

sum = 0

# Part 1
for a,b in zip(x, x[1:]+x[0]):
    if a == b:
        sum += int(a)
print(sum)

sum = 0

# Part 2
for a,b in zip(x, x[len(x)//2:]+x[:len(x)//2]):
    if a == b:
        sum += int(a)
print(sum)
