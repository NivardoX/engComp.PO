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

def bucket_sort(lista):

    def quickSort(lista, inicio, fim):
        if inicio < fim:
            pivo = randint(inicio, fim)
            temp = lista[fim]
            lista[fim] = lista[pivo]
            lista[pivo] = temp

            p = partition(lista, inicio, fim)
            quickSort(lista, inicio, p - 1)
            quickSort(lista, p + 1, fim)

        return lista

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


    maior = max(lista)

    tam = len(lista)

    size = maior/tam

    baldes = [[] for _ in range(tam)]

    for i in range(tam):
        j = int(lista[i]/size)
        if j != tam:
            baldes[j].append(lista[i])
        else:
            baldes[tam - 1].append(lista[i])

    for i in range(tam):
        quickSort(baldes[i],0,len(baldes[i])-1)

    result = []


    for i in range(tam):
        result = result + baldes[i]

    return result

if __name__ == '__main__':

    z = [10000, 20000, 30000, 40000, 50000, 100000, 200000]
    x = []
    for i in z:
        x.append(geraLista(int(i)))
    y = []

    for i in range(len(x)):
        print(len(x[i]))
        y.append(
            timeit.timeit("bucket_sort({})".format(x[i]), setup="from __main__ import bucket_sort",
                          number=1))
    desenhaGrafico(z, y)
