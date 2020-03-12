nmg = input().split()
n = int(nmg[0])
m = int(nmg[1])
g = int(nmg[2])

rullisar = []

for i in range(n):
    rullisar.append([int(i) for i in input().split()])

print(rullisar)
