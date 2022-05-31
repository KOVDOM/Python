a=int(input("A háromszög a oldala: "))
b=int(input("A háromszög b oldala: "))
c=int(input("A háromszög c oldala: "))
if (a+b>c and a+c>b and b+c>a):
    print ("Igen!")
else:
    print("Nem!")