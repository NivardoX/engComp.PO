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
    plt.savefig(z + ".png")

def radix_sort(lista):
    exponencial = 1
    maior = max(lista) if len(lista) > 2 else 0


    bckts = [ [] for i in range(10)]


    while maior // exponencial > 0:
        for i in lista:
            bckts[(i//exponencial)%10].append(i)


        del lista[:]


        for i in range(len(bckts)):


            lista.extend(bckts[i])
            bckts[i] = []

        exponencial *= 10
    return lista

if __name__ == '__main__':

    z = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
    x = []
    for i in z:
        x.append(geraLista(int(i)))
    y = []

    for i in range(len(x)):
        print(len(x[i]))
        y.append(
            timeit.timeit("radix_sort({})".format(x[i]), setup="from __main__ import radix_sort",
                          number=2))
    desenhaGrafico(z, y)
