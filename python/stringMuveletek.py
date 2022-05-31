szoveg="   Ez itt egy mondat.  "
szam="1232121t42"   
emberekLista=["Adrián","David","Milán","Tamás","Szabolcs","Dávid","Ádám","Norbert","K. Tamás","Levente","Balázs"]

print(szoveg.capitalize())  #Első betűt cseréli le nagyra
print(szoveg.capitalize().center(80))   #közepétől eltolja jobbra (megadott értékkel)
print(szoveg.endswith("mondat."))   #megnézi mi a mondat vége
print(szoveg.find("itt"))       #hanyadik karaktertől keződik (index szerint)
print(szoveg.isalnum())
print(szam.isalnum())
print(szoveg.isalpha())
print(szoveg.islower())
print(",".join(emberekLista))
print(szoveg.lstrip()+szam)
print(szoveg.lstrip().rstrip()+szam)
print(szoveg.upper())
print(szoveg.lower())
print(szoveg.replace("egy","1"))
print(szoveg.rfind("egy"))
print(szoveg.split(' '))
print(szoveg.strip()+"vége")
print(szoveg.startswith("  Ez"))
print(szoveg.swapcase())
print(szoveg.title())

szo1="egy"
szo2="egy"
if(szo1==szo2):
    print("azonos a két szám")
else:
    print("a két szó eltérő")
print(szo1==szo2)

#tuple
emberekTuple=("Adrián","David","Milán","Tamás","Szabolcs","Dávid","Ádám","Norbert","K. Tamás","Levente","Balázs")
emberekLista.append("TakInfo")
emberekLista[0]="Adrienn"
print(",".join(emberekLista))
print(";".join(emberekTuple))
print(emberekTuple[0])