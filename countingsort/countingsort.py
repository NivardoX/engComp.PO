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

def counting_sort(lista):
    aux_list = [0] * (max(lista) + 1)
    for item in lista:
        aux_list[item] += 1
    i = 0
    lista.clear()
    for item_index in range(len(aux_list)):
        lista.extend([item_index+1]*aux_list[item_index])

if __name__ == '__main__':

    z = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
    x = []
    for i in z:
        x.append(geraLista(int(i)))
    y = []



    for i in range(len(x)):
        counting_sort(x[i])
        print(len(x[i]))
        y.append(
            timeit.timeit("counting_sort({})".format(x[i]), setup="from __main__ import counting_sort",
                          number=1))
    desenhaGrafico(z, y)
