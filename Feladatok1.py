#1. feladat Írjunk egy számot ami kiirja 1 és 100 között kiírja a számokat
#a feladat
print("Az 1 és 100 között 3-al oszthatók:")
for x in range (0,100,3):
    print(x)
 
#c feladat
print("A páros számok 1 és 100 között:")
x=0
for x in range(0,100):
    if((x%3 == 0) and (x%2 == 0)):
             print(x)

#d feladat
print("3-al nem osztható osztható páros számok:")
r=0
for r in range(0,101):
    if((r%3 !=0) and (r%2==0)):
            print(r)

#3-mal oszthatók feladat
y=0
z=0
print("valami")
for x in range(1,101):
    if ((x%3 == 0) and (x!=0)):
            print(x)
            y+=1
            z=z+x
print(y)
print(z)



#b MARADÉKOS OSZTÁS:
print("MARADÉKOS OSZTÁS:")
x=0
for x in (0,101):
    if (x%2 !=0):
          print(x)
