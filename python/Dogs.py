import classDog

kilep=True
dogs=[]
while (kilep):
    nev=input("Kérem a kutya nevét: ")
    if (nev!=""):
        fajta=input("Kérem a kutya fajtáját: ")
        nem=bool(input("Kérem a kutya nemét: "))
        if (nem=="False"):
            nem=False
        else:
            nem=True
        dog=classDog.Dog(nev,fajta,nem)
        dogs.append(dog)
    else:
        kilep=False
for dog in dogs:
    print(dog.nev,dog.fajta,dog.nemSzovegesen())