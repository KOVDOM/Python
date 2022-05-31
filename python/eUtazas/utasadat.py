class utasadat:

        def __init__(self,megallo=0,fDatum="",kartyaID=0,tipus="",eDatum=""):
            self.megallo=megallo
            self.fDatum=fDatum
            self.kartyaID=kartyaID
            self.tipus=tipus
            self.eDatum=eDatum

        def __str__(self):
            return "{0} {1} {2} {3} {4}".format(self.megallo,self.fDatum,self.kartyaID,self.tipus,self.eDatum)