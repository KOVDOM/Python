def kerulet(a):
    return 4*a
a=int(input("Ad meg a négyzet oldalát: "))
kerulet=kerulet(a)
print("A négyzet kerülete: ",kerulet)

def terulet(a):
    return a*a
terulet=terulet(a)
print("A négyzet területe: ",terulet)

def kerulet2(x,y):
    return 2*(x+y)
x=int(input("Ad meg a téglalap oldalát: "))
y=int(input("Ad meg a téglalap másik oldalát: "))
kerulet2=kerulet2(x,y)
print("A téglalap kerülete: ",kerulet2)

def terulet2(x,y):
    return x*y
terulet2=terulet2(x,y)
print("A téglalap területe: ",terulet2)