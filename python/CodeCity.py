forrasFajl =open("/Users/Admin/Desktop/python/CodeCity.txt", "r")
for sor in forrasFajl:
    #print(sor.strip())
    mezok=sor.strip().split(" ")
    uzenet="YES"
    i=0
    while uzenet=="YES" and i<len(mezok)-1:
        if (abs(int(mezok[i])-int(mezok[i+1]))!=1):
            uzenet="NO"
        i+=1


    #for adat in mezok:
        #print(adat)
    print(uzenet)


forrasFajl.close()
