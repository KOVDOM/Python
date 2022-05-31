kilep=False
while(not kilep):
    filmCime=input("Add meg a film címét: ")
    if(filmCime!=" "):
        filmHossza=int(input("Hány perces a film: "))
        ora=filmHossza//60
        perc=filmHossza%60
        hossz=str(ora)+" óra"+str(perc)+" perc"
        print("A(z) {0} című film {1} hosszú.".format(filmCime,hossz))
    else:
        break