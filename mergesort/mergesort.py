import timeit


import matplotlib.pyplot as plt
import sys

from random import shuffle

def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def gerlistaaInvertida(tam):
    lista = list(range(1, tam + 1))
    return lista[::-1]


def desenhaGrafico(x, y, xl="Entradas", yl="Saídas", z='Tempo'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Lista aleatória - {} ".format(z))
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(z + ".png")


def intercala(lista,lista1,lista2):
    x=0
    y=0
    z=0
    while x < len(lista1) and y < len(lista2):
        if lista1[x] <= lista2[y]:
            lista[z]=lista1[x]
            x=x+1
        else:
            lista[z]=lista2[y]
            y=y+1
        z=z+1

    while x < len(lista1):
        lista[z]=lista1[x]
        x=x+1
        z=z+1

    while y < len(lista2):
        lista[z]=lista2[y]
        y=y+1
        z=z+1


def mergeSort(lista):
    if len(lista)>1:
        meio = len(lista)//2

        lista1 = lista[:meio]

        lista2 = lista[meio:]

        mergeSort(lista1)

        mergeSort(lista2)

        intercala(lista,lista1,lista2)

def timeit_func(data):
    func, x = data
    return (timeit.timeit("{}({})".format(func, x), setup="from __main__ import {}".format(func), number=1))


if __name__ == '__main__':
    z = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
    x = []
    for i in z:
        x.append(geraLista(int(i)))
    y = []

    for i in range(len(x)):
        print(len(x[i]))
        y.append(
            timeit.timeit("mergeSort({})".format(x[i]), setup="from __main__ import mergeSort",
                          number=2))

    desenhaGrafico(z, y)
