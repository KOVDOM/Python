#maganHangzok="aáeéiíuúűüoóöő"
#if("é" in maganHangzok):
 #   print("dvdvdfd")

#maganHangzok="aáeéiíuúűüoóöő"
#szav=input("Kérlek adj meg egy szót: ")
#if(szav in maganHangzok):
#   print("Az")
#else:
#   print("A")

import random

def jelzo():
    return random.choice(["kicicsi","nagy","piros","kék"])

def nevelo(adat):
    maganHangzok="aáeéiíuúűüoóöő"
    if(adat[0].lower() in maganHangzok):
        return "Az"
    else:
        return "A"

fonev=input("Kérek adj meg egy főnevet: ")
print(nevelo(fonev)+" "+fonev+" "+jelzo()+".")