
#Írjon programot, mely elszámol 0-tól 1000-ig!
for i in range(1, 1001): 
    print(i)

#Írjon programot, mely elszámol 100-tól 800-ig!
for i in range(100, 801): 
    print(i)

#Írjon programot, mely kiírja a képernyőre az első tíz természetes számot!
for i in range(1, 11): 
    print(i)

#Alakítsa át az előző programot úgy, hogy az csak a páros számokat írja a képernyőre!
for i in range(0, 12, 2): 
    print(i)
    if (i%2==1):
        print(i)
   
#Írjon programot, mely kiírja a képernyőre a hárommal osztható számokat 100-ig!
for i in range(0, 100): 
    #print(i)
    if (i%3==0):
        print(i)


#Írj programot, ami beolvas egy számot, majd kiírja a kétszeresét!
szam1=int(input("Adjon meg egy számot:"))
b=szam1
szorzat=b*2
print(szorzat)

#Írjon programot ami kiírja a képernyőre az első 5 egész szám összegét!
szam1=1
szam2=2
szam3=3
szam4=4
szam5=5
eredmeny=szam1+szam2+szam3+szam4+szam5

print(eredmeny)
osszeg=0
for i in range(1,6,1):
    print(i)
    osszeg=osszeg+i

#Készítsen programot, mely kiírja 1-10-ig a számok négyzetét.
szam1=1*1
print(szam1)
szam2=2*2
print(szam2)
szam3=3*3
print(szam3)
szam4=4*4
print(szam4)
szam5=5*5
print(szam5)
szam6=6*6
print(szam6)
szam7=7*7
print(szam7)
szam8=8*8
print(szam8)
szam9=9*9
print(szam9)
szam10=10*10
print(szam10)

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
    


#Írjon programot, mely kiírja a képernyőre a páros számokat 1-től 100-ig.
for i in range(0, 101, 2): 
    print(i)
    if (i%2==1):
        print(i)

#Olvass be két számot, írd ki a négyzetüket!
szam1=int(input("Kéreek egy szabadon választott számot! "))
szam2=int(input("Mivel egy szám kevés ezért kérek még egy szabadon választott számot! "))
eredmeny=szam1**szam2
print(eredmeny)

#Írjon programot, mely kiírja a képernyőre a páros számokat 50-től 10-ig.
for i in range(50, 9, -2): 
    print(i)