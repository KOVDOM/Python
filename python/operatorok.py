# print("Hello World!")
# # "="" - értékadó operátor
# a=12
# b="1'2'"
# c='1"2"'
# a9=45
# _a9=65
# A_9=89
# kerdesekSzama=34
# print(a)
# print(b)
# print(c)
# print(a,b,c)
# #műveleti (arimetikai) operatorok +,-,*,/,% maradek(mod),// egesz(div), ** hatvanyozas hatvanyAlap**hatvanyKitevo
# a=1
# b=2
# c=3
# a,b,c=1,2,3
# print(a+b+c)
# a,b,c="alfa","beta","gamma"
# print(a+b+c)
# c=3
# print(a+b+str(c))
# print("{0}{1}{2}".format(a,b,c))
# a=25
# b=24
# a=67
# eredmeny=a-b-c
# print(eredmeny)
# e1=a+b*c
# e2=(a+b)*c
# print(e1,e2)
# e3=a/b-c
# e4=a/(b-c)
# print(e3,e4)
# d=10
# e=3
# mod=d%e
# div=d//e
# print(mod,div)
# hatvanyAlap=2
# hatvanyKitevo=8
# print(hatvanyAlap**hatvanyKitevo)
# print("első sor\n\tmásodik sor\nharmadik sor\nEzt eltüntetem\rEzzel a szöveggel")
# szoveg1="15"
# szam1=int(szoveg1)
# szam2=float(szoveg1)
# print(szam1,szam2)
# szam3=input("Kérem az első számot! ")
# szam3=int(szam3)
# print(szam3)
# szam4=int(input("Kérem a második számot!"))
# print("{0}+{1}={2}".format(szam3,szam4,szam3+szam4))
# ha=input("Kérem a hatványalapot! ")
# ha=(ha)
# hk=int(input("Kérem a hatványkitevőt!"))
# print("{0}^{1}={2}".format(ha,hk,ha**hk))
#egyszerű egyirányú elágazás (szelekció)
#összehasonlító operátorok <,>,<=,=>,==,!=
# szam5=int(input("Kérek egy számot! "))
# if (szam5<10):
#     print("A megadott szám értéke kisebb mint 10!")
# print("ez a szöveg...")
# #összetett két irányú feltétel
# szam6=int(input("Kérek egy számot! "))
# if (szam6%2==1):
#     print("A megadott szám páratlan!")
# else:
#     print("A megadott szám páros!")
# honap=int(input("Kérem a hónap számát! "))
# if (honap==1):
#     print("Január")
# else:
#     if (honap==2):
#         print("Február")
#     else:
#         if (honap==3):
#             print("Március")
#         else:
#             if (honap==4):
#                 print("Április")
#             else:
#                 if (honap==5):
#                     print("Május")
#                 else:
#                     if (honap==6):
#                         print("Június")
#                     else:
#                         if  (honap==7):
#                             print("Július")
#                         else:
#                             if (honap==8):
#                                 print("Augusztus")
#                             else:
#                                 if (honap==9):
#                                     print("Szeptember")
#                                 else:
#                                     if (honap==10):
#                                         print("Október")
#                                     else:
#                                         if (honap==11):
#                                             print("November")
#                                         else:
#                                             if (honap==12):
#                                                 print("December")
#                                             else:
#                                                 print("Nem megfelelő a hónap száma!")
# if (honap==1):
#     print("Január")
# elif (honap==2):
#     print("Február")
# elif (honap==3):
#     print("Március")
# elif (honap==4):
#     print("Április")
# elif (honap==5):
#     print("Május")
# elif (honap==6):
#     print("Június")
# elif (honap==7):
#     print("Július")
# elif (honap==8):
#     print("Augusztus")
# elif (honap==9):
#     print("Szeptember")
# elif (honap==10):
#     print("Október")
# elif (honap==11):
#     print("November")
# elif (honap==12):
#     print("December")
# else:
#     print("Nem megfelelő a hónap száma!")
# honapok={1:"Január",2:"Február",3:"Március",4:"Április",5:"Május",6:"Június",7:"Július",8:"Augusztus",9:"Szeptember",10:"Október",11:"November",12:"December"}
# #logikai operátorok and, or, not
# if (0<honap and honap<13):
#     print(honapok[honap])
# else:
#      print("Nem megfelelő a hónap száma!")
logikaiValtozo=True
print(logikaiValtozo)
if (logikaiValtozo):
    logikaiValtozo=False
else:
    logikaiValtozo=True
logikaiValtozo=not logikaiValtozo
print(logikaiValtozo)
szam1=int(input("Első szám!"))
szam2=int(input("Második szám!"))