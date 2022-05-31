import jatekosokinit

#adatok.append(jatekosokinit.jatekos(jatekosok,pontszam,email))
#adatok=[]


kilepes=True

for i in range(3):
    jatekosok=input("Adja meg a játékos nevét! ")
    pontszam=int(input("Mennyi az elért pontszám! "))
    email=input("Mi a játékos email címe! ")
if pontszam<30:
    kilepes=False