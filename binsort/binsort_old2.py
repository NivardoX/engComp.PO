from random import shuffle
import timeit


import matplotlib.pyplot as plt
bit_len = 5
def verfica(lista):
    return lista.count(lista[0]) == len(lista)
def binsort(output,bin_lista,index):
    if len(bin_lista) == 0:
        return None
    elif len(bin_lista) == 1:
        return bin_lista[0]
    elif verfica(bin_lista):
        return bin_lista

    # if bin_lista.count(bin_lista[0]) == len(bin_lista):
    #     return bin_lista


    lista1 = []
    lista2 = []
    for num in bin_lista:
        if not (num & (1 <<(bit_len - index))):
            lista1.append(num)
        else:
            lista2.append(num)
    # print(lista1)
    # print(lista2)
    out = binsort(output,lista1,index+1)
    if out is not None:
        if isinstance(out,list):
            for z in out:
                output.append(z)
        else:
            output.append(out)
    out2 = binsort(output,lista2,index+1)


    if out2 is not None:
        if isinstance(out2, list):
            for z in out2:
                output.append(z)
        else:
            output.append(out2)
def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def desenhaGrafico(x, y, xl="Entradas", yl="Saídas", z='Tempo'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Lista aleatória - {} ".format(z))
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(z + ".png")


if __name__ == '__main__':
    # bin_lista = []
    # lista = (geraLista(1000000))
    # bit_len = (max(lista)).bit_length()
    # output = []
    # binsort(output,bin_lista,0)
    # # print(output)
    # print([int("".join(str(x) for x in test_list), 2) for test_list in output])

    # z = [100000, 200000, 300000, 400000, 500000]
    # bit_len = (max(z)).bit_length()
    #
    # x = []
    # for i in z:
    #     x.append(geraLista(int(i)))
    # y = []
    #
    # for lista in x:
    #     lista2 = []
    #     print(len(lista))
    #     for i in lista:
    #         lista2.append([((1 if (i & (1 << j)) > 0 else 0)) for j in range(bit_len - 1, -1, -1)])
    #
    #     y.append(
    #         timeit.timeit("binsort({},{},{})".format(output,lista2,0), setup="from __main__ import binsort",
    #                       number=1))
    #
    # desenhaGrafico(z, y)

    output =[]
    bin_lista =[]
    lista = (geraLista(2000))
    bit_len = (max(lista)).bit_length()
    # for i in lista:
    #     bin_lista.append([((1 if (i & (1 << j)) > 0 else 0)) for j in range(bit_len - 1, -1, -1)])

    binsort(output, lista, 0)
    print(output)
    # print([int("".join(str(x) for x in test_list), 2) for test_list in output])
