#1. nagyobb.py feladat 
a=int(input("Adj meg egy számot! ")) 
b=int(input("Adj meg egy másik számot! "))
if a < b :
    print("A nagyobb érték ",b)    
if a > b :
    print("A nagyobb érték ",a)
if a == b :
    print("A két szám egyenlő!") 


#1.2 szavak.py feladat  
c=input("Adj meg egy szót! ")
d=input("Adj meg egy másik szót! ")
if (len(c) < len(d)) :
    print("A hosszabb szó: ",d)
if (len(c) > len(d)) :
    print("A hosszabb szó: ",c)
if (len(c) == len(d)) :
    print("A két szó egyforma hosszú. ")

#1.3 Nyitvatartás
e=int(input("Hány óra van most? "))
qwrt=16
if e<16 and e>8 :
    print("A bolt nyitva van.")
    qwrt=qwrt-e
    print("Ennyi idő van még odaérni ",qwrt)
else :
    print("A bolt zárva van.")

#1.4 Rakéta
indul=int(input("Hány órás visszaszámlálást tervezünk? "))
felfuggesztve=0
f=input("Fel kell-e függeszteni a visszaszámlálást(i/n)?")
for x in range(indul,0,-1):
    print("Visszaszámlás: ",x)
    valasz=input("Fel kell-e függeszteni a visszaszámlálást(i/n)?")
    
    if valasz=="i":
        felfuggesztve+=1
print("A rakéta a visszaszámlálást követőenennyi órával elindult: ",indul+felfuggesztve)


#1.5 jelszo
nev=input("Adja meg felhasználónevét! ")
jelszo=input("Adja meg jelszavát! ")
if (nev=="bori99") and (jelszo=="Szivecske<3") :
    print("Belépés engedélyezve.")
else :
        print("Belépés megtagadva.")
