import timeit
from random import shuffle, randint
import random

import matplotlib.pyplot as plt
import sys


def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def geraListaInvertida(tam):
    lista = list(range(1, tam + 1))
    return lista[::-1]


def desenhaGrafico(x, y, xl="Entradas", yl="Saídas", z='Tempo'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Lista aleatória - {} ".format(z))
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
    plt.savefig(z + ".png")


def quickSort(lista, inicio, fim):
    if inicio < fim:
        pivo = randint(inicio, fim)
        temp = lista[fim]
        lista[fim] = lista[pivo]
        lista[pivo] = temp

        p = partition(lista, inicio, fim)
        quickSort(lista, inicio, p - 1)
        quickSort(lista, p + 1, fim)


def partition(lista, inicio, fim):
    pivo = randint(inicio, fim)

    lista[fim], lista[pivo] = lista[pivo], lista[fim]

    pivo_index = inicio - 1
    for index in range(inicio, fim):
        if lista[index] < lista[fim]:
            pivo_index = pivo_index + 1
            lista[pivo_index], lista[index] = lista[index], lista[pivo_index]

    temp = lista[pivo_index + 1]
    lista[pivo_index + 1] = lista[fim]
    lista[fim] = temp

    return pivo_index + 1


def timeit_func(data):
    func, x = data
    return (timeit.timeit("{}({})".format(func, x), setup="from __main__ import {}".format(func), number=1))


if __name__ == '__main__':
    z = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000, 5000000,10000000]
    x = []
    for i in z:
        x.append(geraListaInvertida(int(i)))
    y = []

    for i in range(len(x)):
        print(len(x[i]))
        y.append(
            timeit.timeit("quickSort({},{},{})".format(x[i], 0, len(x[i]) - 1), setup="from __main__ import quickSort",
                          number=3))
    desenhaGrafico(z, y)
