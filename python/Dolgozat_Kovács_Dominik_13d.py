print("Kovács Dominik 1/13.D dolgozat 2021.11.29.")
#10. feladat
print("Írjon programot, mely elszámol 100-tól 800-ig!")
for x in range(100,801):
    print(x)

#24. feladat
print("Írjon programot, mely kiírja a képernyőre a páratlan számokat 80-tól 20-ig.")
for x in range(79,20,-2):
    print(x)

#21. feladat
print("Olvasd be egy négyzet oldalát, írd ki a kerületét, területét!")
print("Adja meg a négyzet oldalát: ")
a=int(input())
Kerulet=4*a
print("A négyzet kerülete: " )
print(Kerulet)
Terulet=a*a
print("A négyzet területe: " )
print(Terulet)

#18. feladat
print("Írjon programot, mely kiírja a képernyőre a páros számokat 1-től 100-ig.")
for x in range(1,101):
    if x%2==0:
        print(x)

#20. feladat
print("Írjon programot, mely kiírja a képernyőre a páros számokat 50-től 10-ig.")
for x in range(50,9,-2):
    print(x)
