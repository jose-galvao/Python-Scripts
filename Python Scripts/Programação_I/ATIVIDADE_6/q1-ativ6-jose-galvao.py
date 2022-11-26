def maximo(lista):
    maxi = lista[0]
    for i in range(len(lista)):
        if (lista[i] > maxi):
            maxi = lista[i]
    return maxi


def calcular_nivel(lista):
    nivel = maximo(lista)
    if (nivel < 10):
        return 1
    elif (nivel >= 10 and nivel < 20):
        return 2
    else:
        return 3


l = int(input())

while (l != 0):
    lvi = input().split(" ")
    lista = list(map(int, lvi))
    print(calcular_nivel(lista))
    l = int(input())
