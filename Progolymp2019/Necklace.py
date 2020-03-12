necklace = input()


b = 0

len1 = len(necklace)
len2 = int(len(necklace)/2)

for i in range(len2):
    if necklace[i] == "B":
        b+=1

maxB = b


for i in range(len2):
    if necklace[i] == "B":
        b-=1

    if necklace[i+len2] == "B":
        b+=1

    if b > maxB:
        maxB = b

for i in range(len2, len(necklace)):
    if necklace[i % len1] == "B":
        b-=1

    if necklace[(i+len2)%len1] == "B":
        b+=1

    if b > maxB:
        maxB = b

print(maxB)
