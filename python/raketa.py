visszaSzamlalas=int(input("Hány órás vissza számlálást terveztünk? "))
kesleltetes=0
for i in range(visszaSzamlalas,0,-1):
    print("Visszaszámlálás: {0}".format(i))
    #print("Visszaszámálás: "+str(i))
    kerdes=input("Fel kell függeszteni a visszaszámlálást (i/n)? ")
    if (kerdes.lower()=="i"):
        kesleltetes=kesleltetes+1
print("A rakéta a visszaszámlálást követően ennyi órával indult: {0}".format(visszaSzamlalas+kesleltetes))
        