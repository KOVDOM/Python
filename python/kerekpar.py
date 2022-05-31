class kerekparos:
                    def __init__(self, nev, helyezes):
                                        self.nev= nev
                                        self.helyezes= helyezes

versenyzo=[]
for x in range(5):
                    nev=input("Adja meg egy kerékpáros nevét: ")
                    helyezes=int(input("Hányadik helyen végzett a 2021-es Giro'd Italia-n? "))
                    asd=kerekparos(nev,helyezes)
                    versenyzo.append(asd)

for item in versenyzo:
                    print(item.nev,item.helyezes," helyen vézett a 2021-es Giro'd Italia-n.")