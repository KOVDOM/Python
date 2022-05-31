import random
emberek=["Adrián","David","Milán","Tamás","Szabolcs","Dávid","Ádám","Norbert","K. Tamás","Levente","Balázs"]
for ember in emberek:
    print("{0}: {1}".format(ember,random.randrange(1,6)))
emberek.sort(reverse=True)
for ember in emberek:
    print(ember)
print(max(emberek))
print(min(emberek))