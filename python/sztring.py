print(ord("A"))
print(chr(65))
szoveg="Ez itt egy szöveg!"
lista=[]
for betu in szoveg:
    lista.append(ord(betu)+10)
for szam in lista:
    print(chr(szam+22500),end="")