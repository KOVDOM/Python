import random

a=[]
b=[]
unio=[]

for i in range(10):
    a.append(random.randrange(0,101))
    b.append(random.randrange(0,101))

print(a)
print(b)

unio=a+b
print(unio)