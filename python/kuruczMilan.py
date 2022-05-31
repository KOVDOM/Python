import random

szam1=random.randrange(1,31)
szam2=random.randint(31,60)

print(szam1, szam2)
if (szam1*2>szam2):
                    print("Az első szám kétszerese nagyobb, mint a második szám.")
elif (szam1*2<szam2):
                    print("Az első szám kétszerese kisebb, mint a második szám.")
else:
                    print("Az első szám kétszerese egyenlő, mint a második szám.")