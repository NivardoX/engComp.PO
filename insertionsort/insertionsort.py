from multiprocessing.pool import ThreadPool
from random import randint, shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
def geraLista(tam):
    lista = list(range(1,tam+1))
    shuffle(lista)
    return lista
def insertion_sort(alist):
    iterations = 0
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
        iterations += 1

        alist[position]=currentvalue
    return iterations
def bubblesort(lista):
    iterations = 0
    for element in lista:
        for element_index in range(len(lista) - lista.index(element) - 1):
            if lista[element_index] > lista[element_index+1]:
                lista[element_index],lista[element_index+1] = lista[element_index+1],lista[element_index]
                iterations += 1
    return iterations

def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas",z='Tempo'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = z)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()

def timeit_func(data):
    func,x = data
    return (timeit.timeit("{}({})".format(func,x),setup="from __main__ import {}".format(func),number=1))



if __name__ == '__main__':
    z = [10000,20000,50000,100000]
    x = []
    for i in z:
        x.append(geraLista(int(i)))
    print(len(x))
    y =[]

    # pool = ThreadPool(4)
    # results = pool.map(timeit_func,[('insetion_sort',i) for i in z] )

    for i in range(len(x)):
        y.append(timeit.timeit("insertion_sort({})".format(x[i]),setup="from __main__ import insertion_sort",number=1))

    desenhaGrafico(z,y)

    y = []

    for i in range(len(x)):
        y.append(insertion_sort(x[i]))

    desenhaGrafico(z,y, z='Quantidade de swaps')

