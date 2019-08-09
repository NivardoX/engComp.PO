import timeit
from random import shuffle

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
    plt.savefig(z + ".png")


def partition(lista, l, elemento_topo):
    i = (l - 1)
    x = lista[elemento_topo]

    for j in range(l, elemento_topo):
        if lista[j] <= x:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[elemento_topo] = lista[elemento_topo], lista[i + 1]
    return (i + 1)


def quickSort(lista, l, elemento_topo):
    tam = elemento_topo - l + 1
    pilha = [0] * (tam)

    top = -1

    top = top + 1
    pilha[top] = l
    top = top + 1
    pilha[top] = elemento_topo

    while top >= 0:

        elemento_topo = pilha[top]
        top = top - 1
        l = pilha[top]
        top = top - 1

        pivo = partition(lista, l, elemento_topo)

        if pivo - 1 > l:
            top = top + 1
            pilha[top] = l
            top = top + 1
            pilha[top] = pivo - 1

        if pivo + 1 < elemento_topo:
            top = top + 1
            pilha[top] = pivo + 1
            top = top + 1
            pilha[top] = elemento_topo


def timeit_func(data):
    func, x = data
    return (timeit.timeit("{}({})".format(func, x), setup="from __main__ import {}".format(func), number=1))


if __name__ == '__main__':
    z = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
    x = []
    for i in z:
        x.append(geraListaInvertida(int(i)))
    y = []

    for i in range(len(x)):
        y.append(
            timeit.timeit("quickSort({},{},{})".format(x[i], 0, len(x[i]) - 1), setup="from __main__ import quickSort",
                          number=2))

    desenhaGrafico(z, y)
