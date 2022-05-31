import random

sajat=[]
for i in range(1,6):
    szam=int(input("Kérem a(z) {0}. számot: ".format(i)))
    sajat.append(szam)
db=0
sorsoltSzamok=[]
while (db<5):
    gsz=random.randrange(1,91)
    if (gsz not in sorsoltSzamok):
        sorsoltSzamok.append(gsz)
        db=db+1
for elem in sajat:
    print(elem, end=", ")
print(" ")
for elem in sorsoltSzamok:
    print(elem,end=", ")
print("")
talalatokSzama=0
for i in range(5):
    if (sajat[i] in sorsoltSzamok):
        talalatokSzama+=1
print(talalatokSzama)