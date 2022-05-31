tovabb=True
while(tovabb):
    nev=input("Adja meg a felhasználónevét! ")
    jelszo=input("Adja meg a jelszavát! ")
    if (nev=="bori99" and jelszo=="Szivecske<3"):
        tovabb==False
        print("Belépés engedélyezve!")
    else:
        print("Belépés megtagadva!")
