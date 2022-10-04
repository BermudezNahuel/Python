import csv
import re
import json


def leer_json(path:str):
    with open(path,"r") as archivo:
        dicc_json = json.load(archivo)
        lista = dicc_json["heroes"]
    return lista

lista_personajes = leer_json("C:/Users/Nahuel/Documents/TUP/P y L 1/programacion-y-laboratorio-1/clase_10/data_stark.json")
'''
print(lista_personajes)

mensaje = ""
contador = 0
key = "fuerza"
for heroe in lista_personajes:
    contador += 1
    mensaje += f"{contador} - Nombre: {heroe['nombre']} | {key.capitalize()}: {heroe[key]}\n"
print(mensaje)
'''


def validar_dato(respuesta:str, patron:str) -> str:
    '''
    Recibe un dato y los valida con un patron, si este encaja lo devuelve
    respuesta: dato a evaluar
    patron: ingresar patron para evaluar el dato
    '''
    if re.match(patron,respuesta):
        return respuesta
    print("Ingrese un valor valido")

def validar_len_lista(lista:list, respuesta:str)-> int:
    '''
    Valida el largo de una lista y devuelve el valor ingresado. Si el valor no es correcto devuelve un
    mensaje de error
    -lista: ingresar lista de heroes
    :respuesta: ingresar valor
    '''
    respuesta = int(respuesta)
    if lista:
        if respuesta <= len(lista) and respuesta > 0:
            return respuesta
    print(f"Ingrese un valor correcto entre 1 y {len(lista)}")

def validar_dict(diccionario:dict, key:str):
    '''
    Valida que el diccionario no este vacio y que la key exista dentro del mismo.
    Si se cumplen las dos condiciones devuelve un True, sino un False
    -diccionario: ingresar un diccionario
    -key: ingresar una clave
    '''
    retorno = False
    if type(diccionario) == dict and len(diccionario) > 0 and key in diccionario.keys():
        retorno = True
    return retorno

def mostrar_lista(lista:list[dict], key:str = "fuerza") ->str:
    '''
    Recorre una lista e imprime los elementos formateados de acuerdo a la key ingresada. 
    Luego restorna un str con esa informacion
    -lista: ingresar nombre de una lista de diccionarios
    -key: ingresar una key para mostrar en la lista. Por defecto imprime la key "fuerza"
    '''
    mensaje = ""
    contador = 0
    for heroe in lista:
        if validar_dict(heroe,key):
            contador += 1
            mensaje += f"{contador:2d} - Nombre: {heroe['nombre']:20} | {key.capitalize()}: {heroe[key]}\n"
    print(mensaje)
    return mensaje


def buscar_min_max(lista: list[dict], key:str, tipo:str) -> int:
    '''
    Se encargar de buscar cual es el heroe que posee el minimo o maximo valor de una determina
    clave. Luego retorna el indice del lugar que ocupa ese heroe dentro de la lista.
    -lista: ingresar lista de heroes
    -key: ingresar clave a comparar
    -tipo: ingresar el tipo de valor que desea encontrar ascendente o descendente
    '''
    min_max = 0
    if lista:
        for i in range(len(lista)):
            if ((tipo == "asc" and lista[i][key] < lista[min_max][key]) 
                or (tipo == "desc" and lista[i][key] > lista[min_max][key])):
                min_max = i
    return min_max

def ordenar(lista:list[dict], key:str, tipo:str = "asc"):
    '''
    Ordena los datos de una lista de menor a mayor o viceversa segun se indique
    -lista: ingresar lista de heroes
    -key: ingresar clave a comparar
    -tipo: ingresar tipo de orden mayor a menor o viceversa
    '''
    lista_a_ordenar = lista.copy()
    lista_ordenada = []
    while len(lista_a_ordenar) > 0: 
        #Va a recorrer la lista_a_ordenar y por cada vuelta elimina un elemento de esta
        index_min_max = buscar_min_max(lista_a_ordenar,key, tipo)
        #Almaceno en una varaible el index de elemento con la key de mayor o menor valor
        index_lista = lista_a_ordenar.pop(index_min_max)
        #Utilizo .pop() para eliminar ese elemento y almacenarlo en una variable
        lista_ordenada.append(index_lista)
        #Agrego el elemento eliminado por pop() a una nueva lista
    return lista_ordenada

def suma_valores(lista_heroes:list[dict], key:str):
    acumulador = 0
    contador = 0
    for heroe in lista_heroes:
        if validar_dict(heroe, key):
            acumulador += heroe[key]
            contador += 1
        else:
            print("Hay un error en la base de datos")
    return acumulador

def contador_heroes(lista_heroes:list[dict], key:str = "nombre"):
    '''
    Cuenta la cantidad de heroes en total de la lista
    -lista: ingresar lista de heroes
    -key: ingresar clave a comparar
    '''
    contador = 0
    for heroe in lista_heroes:
        if validar_dict(heroe,key):
            contador += 1
    return contador

def calcular_promedio(list_heroes:list[dict], key:str):
    '''
    Calcula el promedio de una key de la lista heroes
    -lista: ingresar lista de heroes
    -key: ingresar clave a promediar
    '''
    dividendo = suma_valores(list_heroes, key)
    divisor = contador_heroes (list_heroes)
    promedio = dividendo/divisor
    return promedio

def buscar_promedio_menor_mayor(lista_heroes:list[dict], key:str, tipo:str):
    '''
    A partir del promedio de una key de los heroes devuelve una lista con los
    heroes por encima o por debajo del promedio
    -lista: ingresar lista de heroes
    -key: ingresar clave para el promedio
    -tipo: ingresar valor por encima o por debajo del promedio
    '''
    promedio = calcular_promedio(lista_heroes, key)
    lista_menor_mayor = []
    for heroe in lista_heroes:
        if validar_dict(heroe,key):
            if (tipo == "menor" and heroe[key] < promedio) or (tipo == "mayor" and heroe[key] > promedio):
                lista_menor_mayor.append(heroe)
    lista_menor_mayor = ordenar(lista_menor_mayor, key)
    return lista_menor_mayor


def buscador(lista_heroes:list) ->list:
    '''
    Busca un patron de inteligencia de cada heroe y crea una lista con este
    -lista: ingresar lista de heroes
    '''
    patron = input("Ingrese tipo de inteligencia:\n-good\n- average\n- high\n")
    lista_busqueda = []
    for elemento in lista_heroes:
        if re.search(patron,elemento["inteligencia"],re.IGNORECASE):
            lista_busqueda.append(elemento)
    return lista_busqueda


def guardar_archivo(nombre_archivo:str, contenido):
    '''
    Crea y guarda un archivo csv a partir de un contenido obtenido de una lista
    -nombre_archivo: ingresar un nombre y ruta para el archivo.csv
    -contenido: ingresar una lista de diccionarios
    '''
    retorno = False
    with open (nombre_archivo,"w+") as archivo:
        archivo.write("Nombre              |Identidad                    |Altura    |Peso   |Fuerza |Inteligencia\n")
        for h in contenido:
            archivo.write("{0:20}|{1:29}|{2:10}|{3:7}|{4:7}|{5:12}\n".format(h['nombre'],h['identidad'],h['altura'],h['peso'],h['peso'],h['fuerza'],h['inteligencia']))
            retorno = True
    if retorno:
        print("Se guardo el archivo con exito")
    else:
        print("Hubo un error al intentar gaurdar el archivo")


