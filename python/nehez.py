import allat

kilepes=True
Allatfajok=[]

while(kilepes):
    fajnev=input("Add meg az állat nevét! ")
    if(fajnev!=""):
        tomeg=int(input("Hány kilogramm tömege egy példánynak! "))
        faj=allat.Allatfaj(fajnev,tomeg)
        Allatfajok.append(faj)
    else:
        kilepes=False
print("A(z) {0} tömege {1}kg.".format(faj.fajnev,faj.tomeg))

