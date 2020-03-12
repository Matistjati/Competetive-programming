nk = input().split()
k = int(nk[0])
n = int(nk[1])

serie = [int(i) for i in input().split()]

kalas = []

for i in range(k):
    kalas.append([int(i) for i in input().split()])

w = set()

for i in kalas:
    j = 2
    while j < len(i):
        if i[j] in w:
            del i[j]
            j-=1
        else:
            w.add(i[j])

        j += 1


pr = []

for i in kalas:
    s = [i[0]]

    l = i[1]
    su = 0
    for o in i[2:]:
        su += serie[o-1]
        s.append([serie[o-1], o-1])
    s.insert(1,su)
    pr.append(s)



can = True
d = 0
h=0
for i in pr:
    h += (i[0]-d)*10
    d = i[0]+1

    if h < i[1]:
        can = False
        break
    else:
        h -= i[1]            
    

print("Ja" if can else "Nej")
    
