import datetime

kezdet = datetime.datetime.now()
for x in range(100):
    print(x)
veg = datetime.datetime.now()
print(kezdet)
print(veg)
print(veg-kezdet)