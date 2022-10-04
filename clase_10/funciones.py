import csv
import re
import json


def leer_json(nombre_archivo):
    with open(nombre_archivo,"r") as archivo:
        lista = json.load(archivo)
        lista = lista['heroes']
        return (lista)

lista_personajes = leer_json("clase_10\data_stark.json")


def validar_dato(respuesta: str, patron:str) -> int:
    if respuesta:
        if re.match(patron, respuesta):
            return respuesta
    return -1


#validar_dato("asd", "asd|desc")


def validar_len_lista(lista:list[dict], tamaño: str) -> int:
    if lista:
        tamaño = int(tamaño)
        if tamaño < len(lista) and tamaño > 0:
            print(f'Tamaño correcto: {tamaño}')
            return tamaño
    print(f'Tamaño maximo superado hay {len(lista)} heroes')
    return len(lista)


def mostrar_lista(lista:list[dict], key:str = "fuerza")->None :
    if lista:
        print("\n")
        mensaje = ""
        contador = 0
        for heroe in lista:
            if key in heroe.keys():
                contador += 1
                mensaje += f'{contador} - Nombre: {heroe["nombre"]} | Identidad: {heroe["identidad"]} | {key.capitalize()}: {heroe[key]}\n'
        print(mensaje)
        print("\n")
        return mensaje

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
            if((order == "desc" and lista[i][key] < lista[i_min_max][key]) or 
                (order == "asc" and lista[i][key] > lista[i_min_max][key])):
                i_min_max = i
        retorno = i_min_max
    return retorno


def funcion_sort(lista:list,key:str,order:str="asc")->list:
    lista_a_ordenar = lista.copy() # lista[:]
    lista_ordenada = []
    while(len(lista_a_ordenar)>0):
        index_min_max = buscar_min_max(lista_a_ordenar,key,order)
        elemento = lista_a_ordenar.pop(index_min_max)
        lista_ordenada.append(elemento)
    return lista_ordenada

#funcion_sort(lista_personajes, "altura", "desc")

'''
def funcion_sort(lista:list,key:str,order:str="desc")->list:
    
    Se encarga de ordenar una lista de diccionarios en oraden ascedente
    o descendente, segun requiera el ussuario. El orden los realiza a traves 
    de un parametro que es una clave del diccionario. Siempre y cuando esta clave sea
    comparable o medible. Luego retorna una lista ordenada
    
    lista_ordenada = []
    while(len(lista)>0):
        index_min_max = buscar_min_max(lista,key,order)
        elemento = lista.pop(index_min_max)
        lista_ordenada.append(elemento)
    print(lista_ordenada)
    return lista_ordenada

'''

def suma_valores (lista_heroes:list, clave:str) -> int:
    acumulador = 0
    for heroes in lista_heroes:
        if len(heroes) > 0 and clave in heroes.keys():
            acumulador += heroes[clave]
    return acumulador


def contador_heroes ( lista_heroes:list) ->int:
    acumulador_heroes = 0
    for heroe in lista_heroes:
        if len(heroe) > 0:
            acumulador_heroes += 1
    return acumulador_heroes

def calcular_promedio(lista_heroes:list, clave:str) -> float:
    dividendo = suma_valores(lista_heroes, clave)
    divisor = contador_heroes(lista_heroes)
    promedio = dividendo/divisor
    mensaje = f'{clave.capitalize()} : promedio'
    print(mensaje)
    return promedio


#calcular_promedio(lista_personajes, 'altura')

def mostrar_abajo_arriba_promedio(lista_heroes:list, clave:str, dato:str) ->list:
    promedio = calcular_promedio(lista_heroes, clave)
    promedio_heroe = ""
    lista = []
    for heroes in lista_heroes:
        if clave in heroes.keys() and len(heroes) > 0 and dato == "mayor":
            if heroes[clave] > promedio:
                lista.append(heroes)
                #promedio_heroe += f"Nombre: {heroes['nombre']} | {clave.capitalize()}: {heroes[clave]}\n"
        if clave in heroes.keys() and len(heroes) > 0 and dato == "menor":
            if heroes[clave] < promedio:
                lista.appen(heroes)
                #promedio_heroe += f"Nombre: {heroes['nombre']} | {clave.capitalize()}: {heroes[clave]}\n"
    print(lista)

#mostrar_abajo_arriba_promedio(lista_personajes, "altura", "abajo")

def buscar_inteligencia(lista_heroe:list[dict], tipo:str) ->list:
    '''
    Busca comparando que inteligencia es igual a la ingresada por el usuario
    y luego devuelve una lista con los heroes que poseen ese tipo de inteligencia

    lista_heroes: ingresar lista de heroes
    tipo: ingresar tipo de inteligencia
    '''
    if lista_heroe:
        lista = []
        for heroes in lista_heroe:
            if len(heroes) > 0 and type(heroes) == dict:
                if tipo == heroes['inteligencia']:
                    lista.append(heroes)
        print(lista)
        return lista
    return -1

#buscar_inteligencia(lista_personajes, "good")

def guardar_archivo(nombre_archivo: str, contenido) -> csv:
    '''
    Toma un contenido ingresado y los guarda como archivo tipo csv
    -Nombre: ingresar una ruta y el nombre del archivo
    -Contenido: ingresar el contenido que se quiera almacenar
    '''
    flag = False
    with open(nombre_archivo, "w+") as archivo:
        archivo.write(contenido)
        flag = True
    if flag:
        print("\nel archivo se gaurdo correctamente\n")
    else:
        print("el archivo no se guardo")


                    
