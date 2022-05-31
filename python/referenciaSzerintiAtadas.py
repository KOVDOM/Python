def listaAtalakit(bemenetiLista):
    atmenetiLista=bemenetiLista
    for elem in bemenetiLista:
        atmenetiLista.append(elem)
    #bemenetiLista.append(6)
    atmenetiLista.clear()


lista=[1,2,3,4,5]
print(lista)
listaAtalakit(lista)
print(lista)