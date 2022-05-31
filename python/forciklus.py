#for (int i=0;i<5;i=i+1)
for i in range(5):
    print(i)
else:
    print("Lefutott a for ciklusom!")
print(i)

for _ in range(4):
    print("Hello!")

for i in range(5,10):
    print(i)

for i in range(10,20,2):
    print(i)

for i in range(20,10,-2):
    print(i)

for i in range(99,0,-3):
    print(i)
else:
    print("Vége")

for i in range(99,0,-1):
    if (i%3==0):
        print(i)

for i in range(0,1001):
    if (i%3==0 and i%7==0):
        print(i)

s=0
for i in range(1,11):
    s=s+i
    #s+=i
    print(s)

mettol=int(input("Mettől: "))
meddig=int(input("Meddig: "))
lepesSzam=int(input("Lépésszám: "))
for i in range(mettol,meddig,lepesSzam):
    print(i)


print("ooooooooooooooooooooo")
print("ooooooooooooooooooooo")
print("ooooooooooooooooooooo")
print("---------------------")
for i in range(5):
    print("oooooooooooooooooooo")
print("----------------------------------------")
for i in range(5):
    for j in range(20):
        print("o",end="")
    print("")
print("--------------------------------------")
for i in range(5):
    for j in range(20):
        if (i==0 or i==4):
            print("o",end="")
        elif(j==0 or j==19):
            print("0", end="")
        else:
            print(" ", end="")
    print("")

print("----------------------------------------")
print("ooooooooooooooooooooo")
print("o                   o")
print("o                   o")
print("o                   o")
print("ooooooooooooooooooooo")
print("----------------------------------------")

nev="Puda Ádám"
nevHossza=len(nev)
for i in range(nevHossza):
    print(nev[i])

for betu in nev:
    print(betu)

for i in range(5):
    if (i==1):
        continue
    if (i==3):
        break
    print(i)