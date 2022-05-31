def oraperc(filmHossza):
    ora=filmHossza//60
    perc=filmHossza%60
    hossz=str(ora)+" óra "+str(perc)+" perc"
    return hossz

i=0
while(i<3):
    filmCime=input("Add meg a film címét: ")
    filmHossza=int(input("Hány perces a film: "))
    i=i+1
    print("A(z) {0} című film {1} hosszú.".format(filmCime,oraperc(filmHossza)))