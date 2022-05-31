def hatvany(alap,kitevo,eredmeny):
    print(eredmeny)
    if (kitevo==1):
        return eredmeny
    return hatvany(alap,kitevo-1,eredmeny*alap)

def fibonacci(elemSzam):
    if(elemSzam<=1):
        return elemSzam
    elem=fibonacci(elemSzam-1)+fibonacci(elemSzam-2)
    print(elem,end=",")
    return elem

def fibonacciIteracio(elemSzam):
    elozoSzam=0
    elozoElozoSzam=0
    szam=1
    print(szam,end=",")
    for i in range(elemSzam-1):
        elozoElozoSzam=elozoSzam
        elozoSzam=szam
        szam=elozoElozoSzam+elozoSzam
        if (i<elemSzam-2):
            print(szam,end=",")
        else:
            print(szam)

    return szam

def fibonaccilista(elemSzam):
    elemek=[0,1]
    for i in range(elemSzam-2):
        elemek.append(elemek[i]+elemek[i+1])
    return elemek



alap=2
kitevo=10
sz=hatvany(alap,kitevo,alap*1)
print(sz)
fibonacciIteracio(10)
print(fibonaccilista(10))
for i in range(10):
    print(fibonacci(i))