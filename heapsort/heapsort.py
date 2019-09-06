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

def heap_sort( alist ):

    def descer( alist, primeiro, ultimo ):
        maior = 2 * primeiro + 1
        while maior <= ultimo:
            if ( maior < ultimo ) and ( alist[maior] < alist[maior + 1] ):
                maior += 1

            if alist[maior] > alist[primeiro]:
                troca( alist, maior, primeiro )
                primeiro = maior;
                maior = 2 * primeiro + 1
            else:
                return

    def troca( A, x, y ):
        A[x],A[y] = A[y],A[x]



    tam = len( alist ) - 1
    menor_pai = tam / 2

    for i in range ( int(menor_pai), -1, -1 ):
        descer( alist, i, tam )

    for i in range ( tam, 0, -1 ):

        if alist[0] > alist[i]:
            troca( alist, 0, i )

            descer( alist, 0, i - 1 )




if __name__ == '__main__':

    z = [1000000, 2000000, 4000000, 500000,1000000, 2000000]
    x = []
    for i in z:
        x.append(geralista(int(i)))
    y = []

    for i in range(len(x)):
        print(len(x[i]))
        y.append(
            timeit.timeit("heap_sort({})".format(x[i]), setup="from __main__ import heap_sort",
                          number=2))
    desenhaGrafico(z, y)
