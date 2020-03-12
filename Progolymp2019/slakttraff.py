mn = input().split()
n = int(mn[0])
m = int(mn[1])

minGemensam = -1

tree = [int(i) for i in input().split()]
bord = [int(i) for i in input().split()]

bordParents=[]
for i in range(len(bord)):
  o = bord[i]
  
  bordParents.append([])
  while o != 0:
    bordParents[i].append(o)
    o = tree[o-1]
  bordParents[i].append(0)
    

d=set(bordParents[0])
for i in range(1,len(bordParents)):
  d=d&set(bordParents[i])


mL = []
mC = 0
for i in bordParents:
  if len(i)>mC:
    mC = len(i)
    mL = i

indices = list(d)
for i in range(len(indices)):
  indices[i]=mL.index(indices[i])

mi = min(indices)
minGemensam = list(d)[indices.index(mi)]


print(minGemensam)
