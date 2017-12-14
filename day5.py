f = open("Inputs/day5", "r")
x = f.readlines()
x = list(map(int, list(map(str.strip, x))))

part1 = False # Set this to False if running part 2

i = 0
step = 0
while i < len(x):
    a = 1
    if not part1 and x[i] >= 3:
        a = -1
    x[i] += a
    i += x[i]-a
    step += 1
print(step)
