kilep = False
while True:
                    szo1=input("Kérlek írj be egy szót!")
                    if(szo1==""):
                                        break
                    else:
                                betu=input("Kérlek adj meg egy betűt!")
                                betu1=0
                                for b_etu in szo1:
                                                    if(b_etu==betu):
                                                                        betu1+=1
print("A(z)"+betu+" betű a(z) "+szo1+" szóban "+str(betu1)+"x szerepel")