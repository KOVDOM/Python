import random

#print(random.randrange(1,100))#1-99
#print(random.randint(0, 100))#1-100

i=0
while(i<5):
    vsz=random.randrange(100,200)
    if(vsz%2==0):
        i+=1
        print(vsz)