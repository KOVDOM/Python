def beszur (szo, betu):
                    vissza=""
                    for b in szo:
                                  vissza+=b+betu
                    return vissza

for i in range(3):
                    szo=input("Kérlek írj be egy szót! ")
                    betu=input("Kérlek írj be egy betűt! ")
                    print(beszur(szo, betu))