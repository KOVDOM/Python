class Dog:

    def __init__(self,nev="",fajta="",nem=None):
        self.nev=nev
        self.fajta=fajta
        self.nem=nem

    def nemSzovegesen(self):
        if (self.nem):
            return "kan"
        else:
            return "szuka"