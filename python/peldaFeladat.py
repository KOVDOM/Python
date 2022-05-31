print("Hány számról van szó? ", end="")
N=int(input())
I=1
Db=0
while(I<=N):
    szam=int(input())
    if(szam>10):
        Db=Db+1
    I=I+1
print("A 10-nél nagyobb számok száma: {0}".format(Db))