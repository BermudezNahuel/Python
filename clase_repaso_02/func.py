import json
import re

def cargar_json(path:str)->list:
    with open(path,"r") as file:
        dicc = json.load(file)
        print(dicc)
    return dicc["paulina"]

cargar_json("clase_repaso_02/data_paulina.json")

def mostrar(lista:list):
    print("\n")
    for elemento in lista:
        print("{0} - {1} - {2}".format(elemento["views"],elemento["length"],elemento["title"]))
    print("\n")


def buscar_min_max(lista:list,key:str,order:str)->int:
    '''
    Busca un minimo en una lista de elementos dict con clave [key]
    Recibe una lista de elementos dict con clave -key- y la clave 
    Retorna el indice del elemnto minimo o -1 en caso de error
    '''
    retorno = -1
    if(len(lista) > 0):
        i_min_max = 0
        for i in range(len(lista)):
            if(order == "down" and lista[i][key] < lista[i_min_max][key])or (order == "up" and lista[i][key] > lista[i_min_max][key]):
                i_min_max = i
        retorno = i_min_max
    return retorno

def nahuel_sort(lista:list,key:str,order:str="up")->list:
    lista_a_ordenar = lista.copy() # lista[:]
    lista_ordenada = []
    while(len(lista_a_ordenar)>0):
        index_min_max = buscar_min_max(lista_a_ordenar,key,order)
        elemento = lista_a_ordenar.pop(index_min_max)# pop() -> elimina un elemento y lo devuelve
        lista_ordenada.append(elemento)
    return lista_ordenada

def nahuel_sort_improve(lista:list,key:str,order:str="up")->list:
    lista_ordenada = lista.copy() # lista[:]
    for i in range(len(lista_ordenada)):
        index_min_max = buscar_min_max(lista_ordenada[i:],key,order) + i
        lista_ordenada[i],lista_ordenada[index_min_max]  = lista_ordenada[index_min_max],lista_ordenada[i]
    return lista_ordenada

def buscar(lista:list,patron:str):
    print("\n")
    for elemento in lista:
        match = re.search(patron,elemento["title"],re.IGNORECASE)
        if(match):
            titulo = elemento["title"]
            palabra = "\033[0;31m" + match.group(0) + "\033[0;m"
            titulo = titulo.replace(match.group(0),palabra)
            print("{0} - {1} - {2}".format(elemento["views"],elemento["length"], titulo))
    print("\n")

def exprotar_csv(lista:list,path:str):
    with open(path,"w") as file:
        for elemento in lista:
            file.write("{0},{1},{2}\n".format(elemento["views"],elemento["length"], elemento["title"]))





