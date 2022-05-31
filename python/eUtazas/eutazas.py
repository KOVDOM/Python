import fuggveny
import utasadat

#1. feladat
fajl=open("eutazas/utasadat.txt","r")
utazasiAdatok=[]
for sor in fajl:
    mezok=sor.strip().split(' ')
    egyUtasadat=utasadat.utasadat(int(mezok[0]),mezok[1],int(mezok[2]),mezok[3],mezok[4])
    utazasiAdatok.append(egyUtasadat)
fajl.close()
#2. feladat
print("2. feladat")
print("A buszra {0} utas akart felszállni. ".format(len(utazasiAdatok)))
#3. feladat
nemUtazhatott=0
for adat in utazasiAdatok:
    if (adat.tipus=="JGY" and adat.eDatum=="0"):
        nemUtazhatott+=1
    if (adat.fDatum[0:8]>adat.eDatum and adat.tipus!="JGY"):
        nemUtazhatott+=1
print("3. feladat")
print("A buszra {0} utas nem szállhatott fel.".format(nemUtazhatott))
#4. feladat
megalloSzama=utazasiAdatok[0].megallo
utasokSzama=0
legtobbUtas=0
legtobbUtasMegallo=megalloSzama
for adat in utazasiAdatok:
    if(adat.megallo==megalloSzama):
        utasokSzama+=1
    else:
        if (utasokSzama>legtobbUtas):
            legtobbUtas=utasokSzama
            legtobbUtasMegallo=megalloSzama
        utasokSzama=1
        megalloSzama=adat.megallo
print("4. feladat")
print("A legtöbb utas ({0} fő) a {1}. megállóban próbált felszállni.".format(legtobbUtas,legtobbUtasMegallo))
a="12345678"
print(int(a[0:4]))
print(a[4:6])
print(a[6:8])
#7.feladat
fajl=open("email.txt","w")
for adat in utazasiAdatok:
    if (adat.tipus!="JGY"):
        elteltNapokSzama=fuggveny.Napokszama(int(adat.fDatum[0:4]),int(adat.fDatum[4:6]),int(adat.fDatum[6:8]),int(adat.eDatum[0:4]),int(adat.eDatum[4:6]),int(adat.eDatum[6:8]))
        if (elteltNapokSzama<=3):
            fajl.write(str(adat.kartyaID)+"\n")
fajl.close()
    

