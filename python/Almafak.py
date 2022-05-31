forrasFile= open("/Users/Admin/Desktop/python/alamafak.txt", "r")
esetekSzama=int(forrasFile.readline().strip())
for i in range(esetekSzama):
    elsoSor=forrasFile.readline().strip()
    elsoSorAdatai=elsoSor.split(' ')
    ladaKapacitas=int(elsoSorAdatai[0])
    ladakSzama=int(elsoSorAdatai[1])
    almafakSzama=int(elsoSorAdatai[2])
    ladakKapacitasa=ladaKapacitas*ladakSzama
    #print(ladakSzama,ladaKapacitas,almafakSzama)
    masodikSor=forrasFile.readline().strip()
    termesek=masodikSor.split(' ')
    osszTermes=0
    for i in range(almafakSzama):
        osszTermes+=int(termesek[i])
    #print(osszTermes)
    if (ladakKapacitasa<osszTermes):
        print("impossible")
    else:
        felhasznaltLadakSzama=osszTermes//ladaKapacitas
        if (osszTermes % ladaKapacitas!= 0):
            felhasznaltLadakSzama+=1
        print(felhasznaltLadakSzama)