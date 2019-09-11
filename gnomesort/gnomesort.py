import timeit
from random import shuffle, randint
import random

import matplotlib.pyplot as plt
import sys


def geralista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def geralistaInvertida(tam):
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

def gnome_sort(alist):
    size = len(alist)
    i = 0


    while i < size:
        if i == 0:

            i = 1


        if alist[i] >= alist[i - 1]:
            i = i + 1


        else:
            alist[i], alist[i - 1] = alist[i - 1], alist[i]
            i = i - 1



if __name__ == '__main__':

    z = [100000, 200000, 400000, 500000,1000000, 2000000]
    x = []
    for i in z:
        x.append(geralista(int(i)))
    y = []

    for i in range(len(x)):
        print(len(x[i]))
        y.append(
            timeit.timeit("gnome_sort({})".format(x[i]), setup="from __main__ import gnome_sort",
                          number=2))
    desenhaGrafico(z, y)
