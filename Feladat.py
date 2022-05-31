nevek=[]
f=open("nevek.txt","r")
for x in f:
    nevek.append(x.strip())
print(nevek)
f.close
nev=input("Kérem a felhasználónevet: ")
jelszo=input("Kérem a jelszvadat: ")
for x in range(0,len(nevek),2):
    if nevek[x]==nev:
        if nevek[x+1]==jelszo:
            print("Sikeres bejelentkezés!")
            start=input("Elindítod-e a rakétát? igen/nem ")
            if(start=="igen"):
                print("Sikeres robbanás!")
            else:
                print("Mindenki megmenekült!")
    else:
        print("Sikertelen bejelentkezés!")