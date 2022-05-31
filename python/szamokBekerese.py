kilepes=True
szam=input("Kérem a bekérendő számot: ")
while kilepes:
    if szam!="":
        szam=int(szam)
        szam2=int(input("Kérem a második számot: "))
        print(szam,szam2)
    else:
        break