import hiresek_alap

hiresNok=[]
for i in range(3):
    nev=input("Add meg egy híres nő nevét! ")
    foglalkozas=input("Add meg a foglakozását! ")
    nemzetiseg=input("Add meg a nemzetiségét (a/n)! ")
    hiresNok.append(hiresek_alap.HiresNo(nev,foglalkozas,nemzetiseg))

for egyHiresNo in hiresNok:
    print("{0} {1} egy híres {2}".format(egyHiresNo.megszolitas(),egyHiresNo.nev,egyHiresNo.foglalkozas))
