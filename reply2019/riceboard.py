t = int(input())

def dab(r,n,m):
    s = 0
    for i in range(n):
        s+=pow(r,i,m)
    return s%m


with open('output.txt', 'w') as output:
    for TEST in range(1, t+1):
        r,n,m = [int(i) for i in input().split()]
        val = dab(r,n*n,m)
        output.write('Case #' + str(TEST) + ": " + str(val)+"\n")
    
