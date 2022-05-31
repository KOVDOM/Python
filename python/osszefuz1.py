import random

a=[]
b=[]
osszes1=[]

for i in range(10):
    a.append(random.randrange(0,101))
    b.append(random.randrange(0,101))

print(a)
print(b)

for i in range(len(a)):
    if(a[i] not in osszes1):
        osszes1.append(a[i])
for i in range(len(b)):
    if(b[i] not in osszes1):
        osszes1.append(b[i])

    
print(osszes1)