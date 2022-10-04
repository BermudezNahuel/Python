'''
from desafio_01 import listado_personajes_masculinos
from desafio_01 import listado_personajes_femeninos
from desafio_01 import altura_max_heroe_masculino
from desafio_01 import altura_max_heroe_femenino
from desafio_01 import calcular_heroe_mas_bajo_masculino
from desafio_01 import calcular_heroe_mas_bajo_femenino
from desafio_01 import promedio_altura_masculino
from desafio_01 import promedio_altura_femenino
from desafio_01 import calcular_color_ojos
from desafio_01 import calcular_color_pelo
from desafio_01 import calcular_tipos_inteligencia
from desafio_01 import listar_heroes_por_color_ojo
from desafio_01 import listar_heroes_por_color_pelo
from desafio_01 import listar_nombre_por_inteligencia
'''


import csv
import re
import json
import valid


#1.1
def imprimir_menu_desafio_05(info:str):
    '''
    Toma un dato, valida si es un string y luego lo imprime
    info: valor que debe ser un string
    '''
    if type(info) == str:
        print(info)

#1.2

def stark_menu_principal_desafio_5():
    menu =  '''
            A - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
            B - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
            C - Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
            D - Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
            E - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
            F - Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
            G - Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
            H - Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
            I - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
            J - Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            K - Determinar cuántos superhéroes tienen cada tipo de color de pelo.
            L - Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
            M - Listar todos los superhéroes agrupados por color de ojos.
            N - Listar todos los superhéroes agrupados por color de pelo.
            O - Listar todos los superhéroes agrupados por tipo de inteligencia

            '''
    imprimir_menu_desafio_05(menu)
    eleccion = input("Ingrese opcion elegida(A,B,C,D,E,S)").upper()
    if re.match('[A-O,Z]',eleccion):
        #print(eleccion)
        return eleccion

    else:
        #print("mal")
        return -1


def stark_marvel_app_5():
    opcion = stark_menu_principal_desafio_5()
    while True:
        match opcion:
            case "A":
                pass
            case "B":
                pass
            case "C":
                pass
            case "D":
                pass
            case "E":
                pass
            case "F":
                pass
            case "G":
                pass
            case "H":
                pass
            case "I":
                pass
            case "J":
                pass
            case "K":
                pass
            case "L":
                pass
            case "M":
                pass
            case "N":
                pass
            case "O":
                pass


def leer_archivo(nombre_archivo):
    dic_json = {}
    with open (nombre_archivo, "r") as archivo:
        dic_json = json.load(archivo)
        lista_json = list(dic_json["heroes"])
    #print(dic_json)
    return lista_json

lista_personajes = leer_archivo("clase_08\desafio_05\data_stark.json")

def sanitizar_entero(numero_str: str):
    numero_str = numero_str.strip()
    if len(re.findall("[0-9]+", numero_str)) > 0:
        num = int(re.findall('[-+]?\d+', numero_str)[0])
        if num > 0:
            return int(num)
        else:
            return -2
    elif len(re.findall("[a-zA-Z]+", numero_str)) > 0:
        return -1
    else:
        return -3
def sanitizar_flotante(numero_str):
    numero_str = numero_str.strip()
    if len(re.findall("[0-9]+\.[0-9]+", numero_str)) > 0:
        num = float(re.findall('[-+]?\d+\.\d+', numero_str)[0])
        if num > 0:
            return num
        else:
            return -2
    elif len(re.findall("[a-zA-Z]+", numero_str)) > 0:
        return -1
    else:
        return -3
def sanitizar_string(valor_str,valor_por_defecto = ""):
    valor_str = valor_str.replace("/", " ")
    if valor_str == valor_por_defecto:
        return valor_por_defecto
    if len(re.findall('[0-9]+', valor_str)) > 0:
        valor = re.findall('\d+', valor_str)
        return "N/A"
    elif len(re.findall('[a-zA-Z]+', valor_str)) > 0:
        lista_valor = re.findall("[a-zA-Z]+[a-zA-Z]+", valor_str)
        valor = " "
        valor = ((valor.join(lista_valor)).lower()).strip()
        return valor
def sanitizar_dato(heroe, clave, tipo_dato):
    if clave in heroe.keys():
        if tipo_dato == "flotante":
            heroe[clave] = sanitizar_flotante(heroe[clave])
            return True
        elif tipo_dato == "entero":
            heroe[clave] = sanitizar_entero(heroe[clave])
            return True
        elif tipo_dato == "string":
            heroe[clave] = sanitizar_string(heroe[clave])
            return True
        else:
            print("Tipo de dato no reconocido")
    else:
        print("La clave especificada no existe en el héroe")
        return False
def stark_normalizar_datos(lista_heroes):
    for heroe in lista_heroes:
        sanitizar_dato(heroe, "altura", "flotante")
        sanitizar_dato(heroe, "peso", "flotante")
        sanitizar_dato(heroe, "fuerza", "entero")
        sanitizar_dato(heroe, "color_pelo", "string")
        sanitizar_dato(heroe, "color_ojos", "string")
        sanitizar_dato(heroe, "inteligencia", "string")
stark_normalizar_datos(lista_personajes)
#1.5
def guardar_archivo(nombre_archivo:str, contenido:str)->bool:
    flag = False
    with open(nombre_archivo , "w+") as archivo:
        archivo.write(contenido)
        flag = True
    if flag == True:
        print("se creo el archivo {0}".format(nombre_archivo))
        retorno = True
    else:
        print("Error al crear el archivo: nombre_archivo")
        retorno = False
    return retorno

#1.6

def capitalizar_palabras(palabras:str):
    lista_palabras = palabras.split(" ")
    i = 0
    for palabra in lista_palabras:
        lista_palabras[i] = palabra.capitalize()
        i += 1
    
    pal = " "
    pal = pal.join(lista_palabras)
    #print(pal)
    return pal

#capitalizar_palabras(lista_personajes[0]['nombre'])

def obtener_nombre_capitalizado(heroe):
    nombre = capitalizar_palabras(heroe["nombre"])
    return nombre

#obtener_nombre_capitalizado(lista_personajes[0])

def obtener_nombre_y_dato(heroe:dict, clave:str):
    nombre = obtener_nombre_capitalizado(heroe)
    dato = heroe[clave]
    clave = capitalizar_palabras(clave)
    mensaje = "Nombre: {0}| {1}:{2}".format(nombre,clave,dato)
    print(mensaje)

#obtener_nombre_y_dato(lista_personajes[0],"fuerza")

#2.1
def es_genero(heroe:dict, genero:str):
    '''
    Se ingresa un heroe y un genero y se determina que estos datos coinciden
    se retorna un True, sino un False

    heroe: se debe ingresar un heroe en formato dict
    genero: se debe ingresar un genero
    '''
    genero = genero.upper()

    if heroe['genero'] == genero:
        retorno = True
    else:
        retorno = False
    return retorno

#2.2
def imprimir_dato(info:str):
    '''
    Toma un dato, valida si es un string y luego lo imprime
    info: valor que debe ser un string
    '''
    if type(info) == str:
        print(info)

def stark_guardar_heroe_genero(lista_heroes:list, genero:str):
    contenido = ""
    for heroe in lista_heroes:
        genero_heroe = es_genero(heroe, genero)
        if genero_heroe:
            contenido += "Nombre: {0}\n".format(heroe['nombre'])
    nombre_archivo = "clase_08/"
    nombre_archivo += "genero_{0}".format(genero)

    guardar_archivo(nombre_archivo, contenido)
            


#stark_guardar_heroe_genero(lista_personajes,"M")



#3.1
def calcular_min_genero(lista_heroes:list, clave:str, genero:str):
    flag = False
    for heroe in lista_heroes:
        if es_genero(heroe, genero) and flag == False:
            minimo = heroe
            flag = True
        if es_genero(heroe, genero) and heroe[clave] < minimo[clave]:
            minimo = heroe
    #print(minimo)
    return minimo
            

#calcular_min_genero(lista_personajes, 'fuerza', "F")    

def calcular_max_genero(lista_heroes:list, clave:str, genero:str):
    flag = False
    for heroe in lista_heroes:
        if es_genero(heroe, genero) and flag == False:
            maximo = heroe
            flag = True
        if es_genero(heroe, genero) and heroe[clave] > maximo[clave]:
            maximo = heroe
    #print(maximo)
    return maximo

def calcular_max_min_dato_genero(lista_heroes:list, dato:str, clave, genero):
    if dato == "minimo":
        personaje = calcular_min_genero(lista_heroes, clave, genero)
    if dato == "maximo":
        personaje = calcular_max_genero(lista_heroes, clave, genero)
    #print(personaje)
    return personaje

#calcular_max_min_dato_genero(lista_personajes, "minimo", "fuerza", "M")

def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes: list,calculo:str, clave:str, genero:str):
    personaje = calcular_max_min_dato_genero(lista_heroes, calculo, clave, genero)
    #print(personaje[clave])
    contenido = "{0} {1}: Nombre: {2} | {3}: {4}".format(calculo,clave,personaje['nombre'],clave,personaje[clave])
    nombre = "clase_08/heroes_{0}_{1}_{2}".format(calculo,clave,genero)
    if guardar_archivo(nombre,contenido):
        retorno = True
    else:
        retorno = False
    return retorno

#stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "minimo", "altura", "m")

def sumar_dato_heroe_genero(lista_heroe:list, clave:str, genero:str):
    acumulador = 0
    for heroe in lista_heroe:
        if type(heroe) == dict and len(heroe) > 0 and es_genero(heroe,genero):
            acumulador += heroe[clave]
    return acumulador
#sumar_dato_heroe_genero(lista_personajes, "altura", "m")

def cantidad_heroes_genero(lista_heroes:list, genero:str):
    cantidad = 0
    for heroes in lista_heroes:
        if es_genero(heroes,genero):
            cantidad += 1
    return cantidad
#cantidad_heroes_genero(lista_personajes,'m')

def calcular_promedio_genero(lista_heroes:list, genero:str, clave:str):
    dividendo = sumar_dato_heroe_genero(lista_heroes,clave,genero)
    divisor = cantidad_heroes_genero(lista_heroes, genero)
    promedio = dividendo/divisor
    return promedio
#calcular_promedio_genero(lista_personajes, "m", "altura")

def stark_calcular_imprimir_guardar_promedio(lista_heroes:list, genero:str, clave:str):
    contenido = "{0} promedio genero {1}: ".format(clave,genero)
    contenido += str(calcular_promedio_genero(lista_heroes, genero, clave))
    nombre = "clase_08/heroe_promedio_{0}_{1}".format(clave, genero)
    if guardar_archivo(nombre,contenido):
        retorno = True
    else:
        retorno = False
    return retorno
#stark_calcular_imprimir_guardar_promedio(lista_personajes, "m", "altura")

#5.1

def calcular_cantidad_tipo(lista_heroes:list,clave:str):
    if valid.validar_lista_no_vacia(lista_heroes):
        dic_colores = {}
        lista_colores = []
        for heroe in lista_heroes:
            lista_colores.append(heroe[clave])
        set_colores = set(lista_colores)

        for color in set_colores:
            contador = 0
            for heroe in lista_heroes:
                if heroe[clave] == color:
                    contador += 1
            color = color.capitalize()
            dic_colores[color] = contador
        
        
    else:
        print("Error : La lista se encuentra vacia")
    return dic_colores

calcular_cantidad_tipo(lista_personajes, "color_pelo")

def guardar_cantidad_heroes_tipo(lista_heroes:list, clave:str, color:str) -> bool:
    dicc = calcular_cantidad_tipo(lista_heroes, clave)
    nombre_archivo = "clase_08/heroes_cantidad_{0}".format(clave)
    contenido = "\nCaracteristica: {0} {1} - Cantidad de heroes: {2}\n".format(clave,color,dicc[color])
    if guardar_archivo(nombre_archivo,contenido):
        retorno = True
    else:
        retorno = False
    return retorno

guardar_cantidad_heroes_tipo(lista_personajes,"color_ojos", "Blue")

def stark_calcular_cantidad_por_tipo(lista_heroes:list, clave:str)->bool:
    pass

  



#validar_lista_no_vacia(lista_personajes)



    


            

        
            











