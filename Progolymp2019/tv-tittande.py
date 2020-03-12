nk = input().split()
k = int(nk[0])
n = int(nk[1])

serie = [int(i) for i in input().split()]

kalas = []

for i in range(k):
    kalas.append([int(i) for i in input().split()])

pr = []

for i in kalas:
    s = [i[0]]

    l = i[1]
    for o in i[2:]:
        s.append([serie[o-1], o-1])

    pr.append(s)



watched = {}
for i in pr:
    for o in i[1:]:
        watched[o[1]] = -o[0]
    

can = True
day = 0
for i in range(len(pr)):
    if not can:
        break
    avHrs = (pr[i][0]-day)*10

    for o in pr[i][1:]:
        h = watched[o[1]]
        d = 0

        if avHrs + h < 0:
            can = False
            break
        else:
            d = -h
            avHrs -= d

        watched[o[1]] += d

    if avHrs > 0:
        
        j = i + 1
        while avHrs > 0 and j < len(pr):
            for o in pr[j][1:]:
                h = watched[o[1]]
                if h < 0:

                    if avHrs + h < 0:
                        watched[o[1]] += avHrs
                        avHrs = 0
                    else:
                        d = -h
                        avHrs -= d

                        watched[o[1]] += d
            j += 1


    day = pr[i][0] + 1
        
print("Ja" if can else "Nej")
