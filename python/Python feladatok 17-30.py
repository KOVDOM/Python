#Készítsen programot, mely kiírja 1-től a számok négyzetét, amig az kisebb mint 1000.
print("Készítsen programot, mely kiírja 1-től a számok négyzetét, amig az kisebb mint 1000.")
for x in range(100):
    print(x*x)
negyzet=0
i=1
while (negyzet<1000):
    print(negyzet)
    negyzet=i*i
    i+=1

#Olvass be két számot, írd ki a négyzetüket!
print("Olvass be két számot, írd ki a négyzetüket!")
print("Adj egy számot: ")
a=int(input())
print("Adj még egy számot: ")
b=int(input())
osszeg=a**b
print(osszeg)

#Írjon programot, mely kiírja a képernyőre a páros számokat 50-től 10-ig.
print("Írjon programot, mely kiírja a képernyőre a páros számokat 50-től 10-ig.")
for x in range(50, 9, -2):
    print(x)

#Olvasd be egy négyzet oldalát, írd ki a kerületét, területét!
print("Olvasd be egy négyzet oldalát, írd ki a kerületét, területét!")
print("Add meg a negyzet oldalát: ")
a=int(input())
K=4*a
print("Kerület:")
print(K)
T=a*a
print("Terület:")
print(T)

#Olvasd be egy téglalap oldalait, írd ki a kerületét, területét!
print("Olvasd be egy téglalap oldalait, írd ki a kerületét, területét!")
print("Írd be a téglalap egyik oldlát: ")
a=int(input())
print("Írd be a téglalap másik oldlát: ")
b=int(input())
print("A téglalap kerülete: ")
K=2*(a+b)
print(K)
print("A téglalap területe: ")
T=a*b
print(T)

#Írjon programot, mely kiírja az első 10 db páros szám összegét a képernyőre!
print("Írjon programot, mely kiírja az első 10 db páros szám összegét a képernyőre!")
list=[2,4,6,8,10,12,14,16,18,20]
print(sum(list))


#Írjon programot, mely kiírja a képernyőre a páratlan számokat 80-tól 20-ig.
print("Írjon programot, mely kiírja a képernyőre a páratlan számokat 80-tól 20-ig.")
for i in range(81, 10, -1):
    if(i%2!=0):
        print(i)
   

#Készítsen programot, mely beolvas 3 db számot a billentyűzetről, majd meghatározza a számok átlagát.
print("Készítsen programot, mely beolvas 3 db számot a billentyűzetről, majd meghatározza a számok átlagát.")
print("Adjon meg 3 számot! ")
szam1=int(input())
szam2=int(input())
szam3=int(input())
atlag=(szam1+szam2+szam3)/3
print(atlag)

#Írjon programot, mely kiírja a képernyőre a páratlan számokat 1-től 90-ig.
print("Írjon programot, mely kiírja a képernyőre a páratlan számokat 1-től 90-ig.")
x=1
for x in range(1, 91, 2):
    print(x)

#Írjon programot, mely kiírja a képernyőre a páratlan számokat 60-tól 15-ig.
print("Írjon programot, mely kiírja a képernyőre a páratlan számokat 60-tól 15-ig.")
x=1
for x in range(61, 14, -2):
    print(x)

#Írjon programot, mely kiírja a képernyőre a páros számokat 70-tól 25-ig.
print("Írjon programot, mely kiírja a képernyőre a páros számokat 70-tól 25-ig.")
x=0
for x in range(72, 24, -2):
    print(x)

#Írj programot, mely beolvas egy pozitív egész számot, és kiírja az egész számokat egymás alá a képernyőre eddig a számig!
print("Írj programot, mely beolvas egy pozitív egész számot, és kiírja az egész számokat egymás alá a képernyőre eddig a számig!")
print("Adjon egy számot: ")
x=int(input())
i = 0
while i < x:
  i += 1
  print(i)
  

#Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!
print("Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!")
print("Ad meg az eslő számot: ")
a=int(input())
print("Ad meg a második számot: ")
b=int(input())
if a>b :
    print(a)
else :
    print(b)