import copy
from xml.dom import minicompat
from xml.etree.ElementInclude import LimitedRecursiveIncludeError

lista = [1,2,3,7,8,4]

def buscar_minimo(lista_a_buscar):
    minimo = 0
    for i in range(len(lista_a_buscar)):
        if lista_a_buscar[i] < lista_a_buscar[minimo]:
            minimo = i
        return minimo

def nahuel_sort(lista_a_ordenar):
    lista_recibida = lista_a_ordenar[:]
    lista_ordenada = []
    while (len(lista_recibida)) > 0:
        minimo = buscar_minimo(lista_recibida)
        pass

def ivan_sort(lista_a_ordenar):
    lista_recibida = lista_a_ordenar[:]
    flag_swap = True

    while(flag_swap == True):
        flag_swap = False
        for i in range(len(lista_recibida)-1):
            '''
            buffer = lista_recibida[i]
            lista_recibida[i] = lista_recibida[i+1]
            lista_recibida[i+1] = buffer
            '''
            lista_recibida[i], lista_recibida[i+1] = lista_recibida[i+1], lista_recibida[i]
            flag_swap = True
        return lista_recibida



def qsort (lista_a_ordenar):
    lista_recibida = lista_a_ordenar[:]
    lista_der = []
    lista_izq = []
    pivot = lista_a_ordenar[0]
    if(len(lista_a_ordenar) <= 1 ):
        return lista_a_ordenar
    else:
        for elemento in lista_recibida[1:]:
            if(elemento > pivot):
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)

    '''
    lista_izq= ivan_sort(lista_izq)
    lista_izq.append(pivot)
    lista_der= ivan_sort(lista_der)
    '''
    lista_izq = qsort(lista_izq)
    lista_izq.append(pivot)
    lista_der = qsort(lista_der)

    return lista_izq + lista_der

'''
from random import randint as rint

    desde = 1
    hasta = 25
    numeros = [rint(desde,hasta) for i in range(hasta)]

    print(f'Sin ordenar:\n {numeros}')

    numeros.sort() #permite ordenar la lista en forma ascendente  numeros.sort(reverse=True) -> ordena la lista en orden descendente

'''
lista_numeros = [1,2,3,8,7,5,9,45,323]

def burbujeo(lista_numeros:list):
    lista_copiada = lista_numeros[:]

    #iterar cada lemento
        #comparalo con que tiene mas adelante, derecha

    len_lista = len(lista_copiada)
    for indice in range(len_lista-1): #
        for indice_siguiente in range(len_lista-1-indice): #
            print(f'indice arriba: {indice}')
            print(f'indice abajo: {indice_siguiente} {len_lista[indice_siguiente]}')

burbujeo(lista_numeros)








