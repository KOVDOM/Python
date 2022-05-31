emberek=["Adrián","David","Milán","Tamás","Szabolcs","Dávid","Ádám","Norbert","K. Tamás","Levente","Balázs"]
for i in range(len(emberek)-1,0,-1):
    maxIndex=i
    for j in range(0,i-1):
        if (emberek[j]>emberek[maxIndex]):
            maxIndex=j
    tmp=emberek[i]
    emberek[i]=emberek[maxIndex]
    emberek[maxIndex]=tmp
    for ember in emberek:
        print(ember)
    print("--------"+str(i))        