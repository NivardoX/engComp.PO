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


def shellSort(lista):


    intervalo = len(lista) // 2

    while intervalo > 0:
        for index in range(intervalo, len(lista)):
            pivo = lista[index]
            aux_index = index
            while aux_index >= intervalo and lista[aux_index - intervalo] > pivo:
                lista[aux_index] = lista[aux_index - intervalo]
                aux_index = aux_index - intervalo
            lista[aux_index] = pivo

        intervalo //= 2
if __name__ == '__main__':
    z = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
    x = []
    for i in z:
        x.append(geraLista(int(i)))
    y = []



    for i in range(len(x)):

        print(len(x[i]))
        y.append(
            timeit.timeit("shellSort({})".format(x[i]), setup="from __main__ import shellSort",
                          number=4))
    desenhaGrafico(z, y)
