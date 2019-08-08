from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

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



if __name__ == '__main__':

    z = [10000,20000,50000,100000]
    x = []
    for i in z:
        x.append(geraLista(i))

    y =[]
    for i in range(len(x)):
        y.append(timeit.timeit("bubblesort({})".format(x[i]),setup="from __main__ import bubblesort",number=1))

    desenhaGrafico(z,y)

    y = []

    for i in range(len(x)):
        y.append(bubblesort(x[i]))

    desenhaGrafico(z,y, z='Quantidade de swaps')
