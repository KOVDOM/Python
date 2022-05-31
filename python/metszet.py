import random

a=[]
b=[]
metszet=[]

for i in range(10):
    a.append(random.randrange(0,101))
    b.append(random.randrange(0,101))

print(a)
print(b)

for i in range(10):
    if(a[i] in b):
        metszet.append(a[i])

print(metszet)