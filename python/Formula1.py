class versenyzo:

    def __init__(self,versenyzoNeve="",nagydijakSzama=0,nyertNagydijakSzama=0):
        self.versenyzoNeve=versenyzoNeve
        self.nagydijakSzama=nagydijakSzama
        self.nyertNagydijakSzama=nyertNagydijakSzama
    
    def __str__(self):
        return self.versenyzoNeve+" "+str(self.nagydijakSzama)+" "+str(self.nyertNagydijakSzama)

class versenyzok:

    def __init__(self,lista=[]):
        self.lista=[]

    def versenyzokHozzaad(self, versenyzo):
        self.lista.append(versenyzo)

    def versenyzokListazasa(self):
        for versenyzo in self.lista:
            print(versenyzo)

versenyzo1=versenyzo("Bela",3,4)
Versenyzok=versenyzok()
Versenyzok.versenyzokHozzaad(versenyzo1)
Versenyzok.versenyzokListazasa()
