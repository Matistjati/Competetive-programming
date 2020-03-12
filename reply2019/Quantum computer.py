t = int(input())

with open('output.txt', 'w') as output:
    for TEST in range(1, t+1):
        n = 0
        xSize, ySize = [int(i) for i in input().split()]
        x, y = [int(i) for i in input().split()]
        n = int(input())
        portals =  [None for a in range( n )]

        for o in range(n):
            portals[o] = [True]
            portals[o].extend([int(i) for i in input().split()])
            
        
        dist = 0
        b=[True, x,y]
        ind = n-1
        for o in range(n+1):
            minDist = 690000000
            best = [1000000,1000000]
            for i in range(len(portals)):
                if not portals[i][0]:
                    continue

                d = abs(b[1]-portals[i][1])+abs(b[2]-portals[i][2])
                if d < minDist or (d == minDist and ((portals[i][1]<best[0]) or (portals[i][1]==best[0] and portals[i][2]<best[1]))):
                    minDist = d
                    ind = i
                    best = [portals[i][1],portals[i][2]]

            if minDist != 690000000:
                dist += minDist
            b = [True, portals[ind][3],portals[ind][4]]
            portals[ind][0] = False
        
        output.write('Case #' + str(TEST) + ": " + str(dist%100003)+"\n")

    
