w = input()

curr = ["",0,0]
i = 0

consonants = "bcdfghjklmnpqrstvwxz"

while True:
    if i >= len(w):
        break

    if w[i].lower() == curr[0].lower() and w[i].lower() in consonants:
        curr[1]+=1
        
    elif curr[1]>2:
        w = w[:curr[2]]+w[curr[1]+curr[2]-2:]
        i = curr[2]+1
        curr[1] = -1
    else:
        curr = [w[i].lower(), 1, i]
    i+=1

if curr[1]>2:
    w = w[:curr[2]]+w[curr[1]+curr[2]-2:]
    i = curr[2]+1
    curr[1] = -1
print(w)
    
