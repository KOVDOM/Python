class teglalap:

    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    
    def __str__(self):
        return "'a' oldal: {0}cm\n'b' oldal: {1}cm".format(self.a,self.b)

    def kerulet(self,mertekEgyseg):
        return str((self.a+self.b)*2)+" "+mertekEgyseg
    
    def terulet(self,mertekEgyseg):
        return str(self.a*self.b)+" "+mertekEgyseg