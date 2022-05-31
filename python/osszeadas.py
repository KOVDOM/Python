#Összeadás eljárás
def osszeadasEljaras(formalisParameter1,formalisParameter2):
    print("A két szám összege",formalisParameter1+formalisParameter2)

#Összeadás függvény
def osszeadasFuggveny(formalisParameter1,formalisParameter2):
    visszateresiErtek=formalisParameter1+formalisParameter2
    return visszateresiErtek

szam1=int(input("Kérem az első számot: "))
szam2=int(input("Kérem a második számot: "))
szam3=int(input("Kérem a harmadik számot: "))
print("A két szám összege",szam1+szam2)


aktualisParameter1=szam1
aktualisParameter2=szam2
aktualisParameter3=szam3
#Összeadás eljárás meghívása
osszeadasEljaras(aktualisParameter1,aktualisParameter2)
#Összeadás eljárás meghívása
eredmeny=osszeadasFuggveny(aktualisParameter1,aktualisParameter2)
print("A két szám összege:",eredmeny)
eredmeny=osszeadasFuggveny(eredmeny,aktualisParameter3)
print("A három szám eredménye: ",eredmeny)