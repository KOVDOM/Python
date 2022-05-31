napSzama=int(input("Hanyadik nap van a héten? "))
napok={1:"Hétfő",2:"Kedd",3:"Szerda",4:"Csütörtök",5:"Péntek",6:"Szombat",7:"Vasárnap"}
if (napSzama<6):
    print("Hétközben van.")
else:
    print("Hétvége van.")
print(napok[napSzama])