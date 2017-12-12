f = open("Inputs/day2", "r")
x = f.readlines()
# Part 1
sum = 0
for line in x:
    a = list(map(int, line.strip().split("\t")))
    sum += (max(a)-min(a))
print(sum)

# Part 2
sum = 0
for line in x:
        a = list(map(int, line.strip().split("\t")))
        a.sort(reverse=True)
        for i in range(0, len(a)-1):
            for j in range(i+1, len(a)):
                if a[i]//a[j] == a[i]/a[j]:
                    sum += (a[i]//a[j])
                    break
print(sum)
