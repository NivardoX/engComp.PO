import timeit
from random import shuffle

import matplotlib.pyplot as plt


def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def geraListaInvertida(tam):
    lista = list(range(1, tam + 1))
    return lista[::-1]


def desenhaGrafico(x, y, y2, xl="Entradas", yl="Saídas", z='Tempo'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Lista aleatória - {} ".format(z))
    ax.plot(x, y2, label="Lista invertida - {} ".format(z))
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(z+".png")


def insertion_sort(alist):
    iterations = 0
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1
            iterations += 1

        alist[position] = currentvalue
    return iterations

def timeit_func(data):
    func, x = data
    return (timeit.timeit("{}({})".format(func, x), setup="from __main__ import {}".format(func), number=1))


if __name__ == '__main__':
    z = [10000, 20000, 50000, 100000]
    x = []
    x2 = []
    for i in z:
        x.append(geraLista(int(i)))
        x2.append(geraListaInvertida(int(i)))
    y = []
    y2 = []

    for i in range(len(x)):
        y.append(
            timeit.timeit("insertion_sort({})".format(x[i]), setup="from __main__ import insertion_sort", number=1))
        y2.append(
            timeit.timeit("insertion_sort({})".format(x2[i]), setup="from __main__ import insertion_sort", number=1))

    desenhaGrafico(z, y, y2)

    y = []
    y2 = []

    for i in range(len(x)):
        y.append(insertion_sort(x[i]))
        y2.append(insertion_sort(x2[i]))

    desenhaGrafico(z, y, y2, z='Quantidade de swaps')
