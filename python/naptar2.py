napok={"hétfő":1,"kedd":2,"szerda":3,"csütörtök":4,"péntek":5,"szombat":6,"vasárnap":7}
nap=input("Melyik nap van a héten? ")
napSzama=napok[nap.lower()]
if (napSzama<6):
    print("Hétközben van.")
else:
    print("Hétvége")
print("{0}. nap".format(napSzama))