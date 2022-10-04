import json
import re

def leer_poke(path:str):
    with open (path,"r") as archivo:
        diccio = json.load(archivo)
        lista = diccio["pokemones"]
    return(lista)

lista_pokemones = leer_poke("C:/Users/Nahuel/Documents/TUP/P y L 1/programacion-y-laboratorio-1/Simulacro_pokemon/pokedex.json")
#print(lista_pokemones)

def validar_lista_len(lista:list[dict], respuesta:int):
    if lista:
        if respuesta > 0 and respuesta < len(lista):
            return respuesta
    print("Ingrese un valor valido")
    return 0 


def validar_dato(respuesta:str, patron:str) -> str:
    if re.match(patron,respuesta, re.IGNORECASE):
        respuesta = respuesta.lower()
        return respuesta
    print("Ingrese un valor valido")
    return "N/A"

def mostra_poke(lista:list[dict], key:str = "tipo") ->list:
    if lista:
        mensaje = ""
        titulo = " ID -    NOMBRE    - {0}".format(key.upper())
        for poke in lista:
            mensaje += "{0:03} - {1:12} - {2}\n".format(poke["id"],poke["nombre"].capitalize(),poke[key])
        print(titulo)
        print(mensaje)
    return mensaje


def crear_lista_guardar(lista:list[dict], key:str = "tipo") ->list:
    lista_para_guardar = []
    for poke in lista:
        diccio = {}
        diccio["id"] = poke["id"]
        diccio["nombre"] = poke["nombre"]
        diccio["poder"] = poke["poder"]
        lista_para_guardar.append(diccio)
    return lista_para_guardar

#lista_poke2 = crear_lista_guardar(lista_pokemones,"poder")

def ordenar_poke(lista:list[dict],key:str, orden:str):
    if orden == "N/A" :
        return False
    swap = True
    while swap:
        swap = False
        for i in range(len(lista)-1):
            if (orden == "desc" and lista[i][key] < lista[i+1][key]) or (orden == "asc" and lista[i][key] > lista[i+1][key]):
                swap = True
                lista[i] , lista[i+1] = lista[i+1], lista[i]
    lista = crear_lista_guardar(lista,key)
    #print(lista)
    return lista

#ordenar_poke(lista_poke2, "poder")

def suma_habilidades(lista:list[dict], key:str)->list:
    acumulador = 0
    for poke in lista:
        acumulador += len(poke[key])
    return acumulador

def contador_pokemones(lista:list[dict]):
    contador = 0
    for poke in lista:
        contador += 1 
    return contador

def realizar_promedio(lista:list[dict], key:str):
    dividendo = suma_habilidades(lista,key)
    divisor = contador_pokemones(lista)
    if divisor > 0:
        promedio = dividendo/divisor
        return promedio
    print("Error al calcular el promedio")

def buscar_promedio_menor_mayor(lista:list[dict], key:str, orden:str) -> list:
    promedio = realizar_promedio(lista,key)
    lista_promedio = []
    for poke in lista:
        if (orden == "mayor" and len(poke[key]) > promedio) or (orden == "menor" and len(poke[key]) < promedio):
            lista_promedio.append(poke)
    return lista_promedio

#copia = lista_pokemones[:]
#buscar_promedio_menor_mayor(copia,"tipo", "menor")

def listar_tipo_poke(lista:list[dict]):
    lista_tipos = []
    for poke in lista:
        for tipo in poke["tipo"]:
            lista_tipos.append(tipo)
    set_tipo = set(lista_tipos)
    patron = "|"
    patron = patron.join(set_tipo)
    return patron

#copia = lista_pokemones[:]

#listar_tipo_poke(copia)

def buscador_tipo(lista:list[dict], valor:str) ->list:
    lista_tipos = []
    for poke in lista:
        for elemento in poke["tipo"]:
            if re.search(valor, elemento):
                lista_tipos.append(poke)
    return lista_tipos

#buscador_tipo(copia,"lucha")

def guardar_archivo(path:str, contenido:str):
    with open (path, "w+") as archivo:
        archivo.write(" ID -    NOMBRE    \n")
        archivo.write(contenido)
        

