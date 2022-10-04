

import json
import re


def construir_lista(nombre_archivo):
    with open(nombre_archivo,"r") as archivo:
        lista_dic = json.load(nombre_archivo)
    return

'''
def buscar_minimo(lista:list)->int: #busco de devulva la pasicion me permite volver a encontrar el elemento
    
    Busca un minimo en una lista de elementos diccionario con clave
    Retorna el indice del elemento encontrado o -1 en caso de error
    
    lista: con elementos dict
    
    retorno = -1
    if( len(lista) > 0 ) :
        i_min = 0
        for i in range(1,len(lista)):
            if lista[i] < lista[i_min]:
                i_min = i
        retorno = i_min
    return retorno
'''

def buscar_min_max(lista:list, key: str, order:str)->int: #busco de devulva la pasicion me permite volver a encontrar el elemento
    '''
    Busca un minimo en una lista de elementos diccionario con clave
    Retorna el indice del elemento encontrado o -1 en caso de error
    
    lista: con elementos dict
    '''
    retorno = -1
    if( len(lista) > 0 ) :
        i_min_max = 0
        for i in range(len(lista)):
            if ((order == "down" and lista[i][key] < lista[i_min_max][key]) or 
                (order == "up" and lista[i][key] > lista[i_min_max][key])):
                i_min_max = i
        retorno = i_min_max
    return retorno




def funcion_sort(lista:list, key:str, order:str="up")->list:
    lista_a_ordenar = lista[:]
    lista_ordenada = []
    while(len(lista_a_ordenar) > 0):# cuando a la lista a ordenar se queda sin elemento sale del while
        index_min_max = buscar_min_max(lista_a_ordenar, key,order)
        #lista_ordenada.append(lista_a_ordenar.pop(index_minimo))
        elemento = lista_a_ordenar.pop(index_min_max)#elimino el elemento de esa lista
        lista_ordenada.append(elemento)#agrego el elemento a la lista

#funcion sort mejorada

def funcion_sort_mejorada(lista:list, key:str, order:str="up")->list:
    lista_ordenada = lista[:]
    index_min_max = buscar_min_max(lista, key, order)

    for i in range(len(lista_ordenada)):
        index_min_max = buscar_min_max(lista_ordenada[i:], key , order) + i # busco el indice del minimo y lo guardo en la variable
        print("minimo: ", index_min_max)
        lista_ordenada[i], lista_ordenada[index_min_max] = lista_ordenada[index_min_max], lista_ordenada[i]

def buscar(lista:list,patron:str):
    print("\n")
    for elemento in lista:
        if (elemento["title"]):
            re.search("comer", elemento["title"],re.IGNORECASE)


'''
validaciones se pueden usar en el examen

validar que sea un numero
validar que sea un string
validar que sea un float
validar que sea un numero positivo
validar letras en minuscula
validar letras en mayuscula
validar primera letra de cada palabra



'''
        