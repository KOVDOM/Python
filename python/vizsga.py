tovabb=True
while(tovabb):
    nev=input("Add meg a vizsgázó nevét! ")
    pontszam=int(input("Add meg a pontszámát! "))
    if(pontszam>=48):
        tovabb=False
        print("{0} vizsgája sikeres volt!".format(nev))
    else:
        print("{0} vizsgája sikertelen volt!".format(nev))
