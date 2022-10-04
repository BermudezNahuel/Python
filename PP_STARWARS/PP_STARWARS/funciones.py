import json
import re


def cargar_json(path:str) -> list:
    with open (path, "r") as archivo:
        diccio = json.load(archivo)
        lista = diccio["results"]
    return lista

lista_personajes = cargar_json("PP_STARWARS/PP_STARWARS/data.json")
copia_lista = lista_personajes[:]

def normalizar_datos(lista:list[dict], key:str) ->list:
    '''
    Castea los datos str a int de los diccionarios de la lista
    -lista: ingresar lista de personajes
    -key: ingresar una key del diccionario para comparar los personajes
    
    '''
    mensaje = ""
    for personaje in lista:
        personaje[key] = int(personaje[key])
    return lista
lista_copia = normalizar_datos(copia_lista,"height")
lista_copia = normalizar_datos(copia_lista,"mass")

def mostrar_lista(lista:list[dict]):
    '''
    Muestra la lista que se le pasa por parametro
    -lista: ingresar la lista que se desea mostrar por consola
    '''
    if lista:
        mensaje = ""
        for personaje in lista:
            mensaje += "{0:19} - {1} - {2} - {3}\n".format(personaje["name"],personaje["height"],personaje["mass"],personaje["gender"])
    print(mensaje)
    return mensaje



def ordenar_personajes(lista:list[dict], key:str) -> list:
    '''
    Esta funcion se encarga de ordenar los personajes a partir de un
    determinado parametro y luego devuelve una lista con estos.
    -lista: ingresar una lista de diccionarios
    -key: ingresar una key del diccionario para comparar los personajes
    '''
   
    swap = True
    while swap:
        swap = False
        for i in range(len(lista)-1):
            if lista[i][key] < lista[i+1][key]:
                swap = True
                lista[i], lista[i+1] = lista[i+1],lista[i]
    #print(lista)
    return lista

#mostrar_lista(ordenar_personajes(copia_lista,"height"),"height")

def listar_por_genero(lista:list,genero:str):
    '''
    Hace una lista con el genero indicado
    -lista: ingresar una lista
    genero: ingresar el gnero para realiazr la lista
    '''
    if lista:
        lista_genero = []
        for personaje in lista:
            if personaje["gender"] == genero:
                lista_genero.append(personaje)
    #print(lista_genero)
    return lista_genero

#listar_por_genero(lista_copia, "male")


def buscar_mas_alto(lista:list[dict], genero:str) -> str:
    #lista_genero = listar_por_genero(lista, genero)
    if lista:
        max = lista[0]
        for personaje in lista:
            if personaje["height"] > max["height"] : 
                max = personaje
    print(max)
    return max

def buscador_personajes(lista:list[dict], patron:str):
    '''
    Realiza una busqueda en la lista por el nombre de personaje y lo retorna
    -lista: ingresar una lista
    -patron: ingresar nombre del personaje
    '''
    if lista:
        lista_buscador = []
        for personaje in lista:
            if re.search(patron, personaje["name"]):
                lista_buscador.append(personaje)
                # mensaje = "{0} - {1} - {2} - {3}".format(personaje["name"],personaje["height"],personaje["mass"],personaje["gender"])
        return lista_buscador

def guardar_archivo(path:list, contenido):
    '''
    Crea un archivo csv y lo guarda
    path: direccion y nombre del archivo
    contenido:ingresar los datos a guardar
    '''
    with open(path, "w+") as archivo:
        archivo.write(contenido)
        print("El archivo se gaurdo con exito")
