kompisN = int(input())
barn = []
for i in range(kompisN):
  barn.append(input())

relationN = int(input())
relationer = []
for i in range(relationN):
  relationer.append(input())

grupper = []

for i in relationer:
  grupper.append(i.split())

changed = True
for i in range(200):
    if not changed:
        break
    changed = False
    i = 0
    while i < len(grupper):
      o=0
      setI = set(grupper[i])
      while o < len(grupper):

        if i==o:
          o+=1
          continue
        if len(setI & set(grupper[o])) > 0:
          grupper[i].extend(x for x in grupper[o] if x not in grupper[i])
          changed = True
          del grupper[o]
          break
        o+=1

      i+=1

# Hantera esamma stackare
for i in barn:
  contains = False
  for o in grupper:
    if i in o:
      contains = True
      break

  if not contains:
    grupper.append([i])


print(len(grupper))
