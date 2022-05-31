import random

def kiir(osszterheles):
    terheles=osszterheles/60
    print(osszterheles)
    if terheles>20:
        print("A terhelés túl nagy!")
    elif terheles>10 and terheles<20:
        print("A terhelés megfelelő!")
    else :
        print("A terhelés kicsi!")

csatlakozasokSzama=int(input("Hányszor csatlakozik percenként? (0-50): "))
osszterheles=csatlakozasokSzama*random.randrange(1,30)
print(kiir(osszterheles))

