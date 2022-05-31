

#2.3 Mondatok feladat
import random
def nevelo(szo):
    maganhangzo="aáeéiíoóöőuúüű"
    if szo[0].lower() in maga
def jelzo():
    return random.choice(['piros','nagy','könnyed'])
for x in range(3):
    print("Adjon meg három főnevet!")
    fn=input(str(x+1)+". főnév: ")
    print(nevelo(fn),fn,jelzo())





#2 vizsga  feladat
def sikerese(pontszam):
    if(pontszam<48):
        return False
    else:
        return True
while(True):
    nev=input("Add meg a vizsgázó nevét! ")
    if nev:
        pontszam=int(input("Add meg a vizsgázó pontszámát "))
        if sikerese(pontszam):
            print(nev," vizsgálya sikeres!")
        else:
            print(nev," vizsgálya sikertelen!")
    else:
         break

#2.2 film feladat
def oraperc(ido):
    ora=ido//60
    perc=ido%60
    return str(ora)+'óra '+str(perc)+'perc'
for x in range(3):
    filmcim=input("Add meg egy film címét! ")
    ido=int(input("Hány perces a film? "))
    print("A(z)",filmcim," című film ",oraperc(ido)," hosszú.")