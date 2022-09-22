from calculos import calcula_maximo_minimo
from calculos import calcular_promedio_tiempo
from calculos import calcular_promedio_vistas
from calculos import calcular_tema_mas_corto
from calculos import calcular_tema_mas_largo
from calculos import calcular_tema_mas_visto
from calculos import calcular_tema_menos_visto


from calculos import test

import json
import re
'''


[
    
    {
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
    }
]
1 - Tema mas visto
2 - Tema menos visto
3 - Tema mas largo
4 - Tema mas corto
5 - Duracion promedio de temas
6 - Promedio de vistas 
7 - Salir

Tipo : BZRP MUSIC SESSIONS
Artista: Quevedo
Número:  52
Reproducciones: 227 M 
Duración: 204 minutos 
Código: A_g3lMcWVy0
Fecha de farga: 6/7/2022
Hora de carga: 00:00

'''

def mostrar_menu()->str:
    respuesta = input("\n1 - Tema mas visto\n2 - Tema menos visto\n3 - Tema mas largo\n4 - Tema mas corto\n5 - Duracion promedio de temas\n6 - Promedio de vistas\n7 - Salir\n\n> ")
    return respuesta

def bzrp_app(lista:list):
    while True:
        respuesta = mostrar_menu()
        if(respuesta == "1"):
            calcular_tema_mas_visto(lista)
        elif(respuesta == "2"):
            calcular_tema_menos_visto(lista)
        elif(respuesta == "3"):
            calcular_tema_mas_largo(lista)
        elif(respuesta == "4"):
            calcular_tema_mas_corto(lista)
        elif(respuesta == "5"):
            calcular_promedio_tiempo(lista)
        elif(respuesta == "6"):
            calcular_promedio_vistas(lista)
        elif(respuesta == "7"):
            test(lista)
            
            break

def parse_csv(nombre_archivo:str)->list:
    lista_rta = []
    
    with open(nombre_archivo,"r") as archivo:
        #archivo = open(nombre_archivo,"r")
        for linea in archivo:
            lista = linea.split(",")
            video = {}
            video["title"] = lista[0]
            video["views"] = int(lista[1])
            video["length"] = int(lista[2])
            video["img_url"] = lista[3]
            video["url"] = lista[4]
            video["date"] = lista[5]
            lista_rta.append(video)
        #archivo.close() 
    return lista_rta

def generar_csv(nombre_archivo:str, lista:list):
    with open(nombre_archivo, "w") as archivo:
        for video in lista:
            mensaje = "{0},{1},{2},{3},{4},{5}"
            mensaje = mensaje.format(   video["title"],
                                        video["views"],
                                        video["length"],
                                        video["img_url"],
                                        video["url"],
                                        video["date"])
            archivo.write(mensaje)



def parse_json(nombre_archivo:str)->list:
    dic_json = {}
    with open(nombre_archivo,"r") as archivo:
        dic_json = json.load(archivo)
    return dic_json["bzrp"]
    
def parse_json_manual(nombre_archivo:str)->list:
    lista_rta = []
    
    with open(nombre_archivo,"r") as archivo:
        texto_archivo = archivo.read()

    #respuesta = re.findall(r'"title": "([a-zA-Z0-9\| #-]+)',texto_archivo)
    respuesta = re.findall(r'"title": "([^,]+)',texto_archivo)
    
    print(respuesta)

    return lista_rta    

#lista_bzrp = parse_csv("/Users/Mauro/Documents/workspace_pl1_python/PL1_PY_2022_2C/CLASE_08/data.csv")
#generar_csv("/Users/Mauro/Documents/workspace_pl1_python/PL1_PY_2022_2C/CLASE_08/data_test.csv",lista_bzrp)
lista_bzrp = parse_json_manual("/Users/Mauro/Documents/workspace_pl1_python/PL1_PY_2022_2C/CLASE_08/data.json")
lista_bzrp = parse_json("/Users/Mauro/Documents/workspace_pl1_python/PL1_PY_2022_2C/CLASE_08/data.json")
#print(lista_bzrp)
bzrp_app(lista_bzrp)














































t = '"title": "QUEVEDO || BZRP Music Sessions #52","views": 227192970,"length": 204,"img_url": "https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg","url": "https://youtube.com/watch?v=A_g3lMcWVy0","date": "2022-07-06 00:00:00"'








