import random

emberek=["Adrián","David","Milán","Tamás","Szabolcs","Dávid","Ádám","Norbert","K. Tamás","Levente","Balázs"]
hol=["Sajószentpéter","NAV-nál","kórházban","a WC-n","Diósgyőrben","iskololában","otthon","cigánysoron","tanár úr óráján","aluljáróban"]
mit=["megkéselte","eladta","megette","meghalt, de túlélte","feldarabolta","megtanulta","bedrogozta","eltekerte","becsúsztatta","tövig bekapta","megcsókolta"]

emberekSzama=len(emberek)
helyszinekSzama=len(hol)
cselekvesekSzama=len(mit)
ki=random.randrange(0,emberekSzama)
kivel=random.randrange(0,emberekSzama)
merre=random.randrange(0,helyszinekSzama)
cselekves=random.randrange(0,cselekvesekSzama)
print("{0} {1} {2} {3}".format(emberek[ki],hol[merre],emberek[kivel],mit[cselekves]))