import random

a=[]
b=[]
kulonbsegA=[]
kulonbsegB=[]

for i in range(10):
    a.append(random.randrange(0,101))
    b.append(random.randrange(0,101))

print("A halmaz: ",a)
print("B halmaz: ",b)

for i in range(10):
    if(a[i] not in b):
        kulonbsegA.append(a[i])

print("A halmaz különbsége: ",kulonbsegA)

for i in range(10):
    if(b[i] not in a):
        kulonbsegB.append(b[i])

print("B halmaz különbsége: ", kulonbsegB)