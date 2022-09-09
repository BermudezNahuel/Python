import string
from data_stark import lista_personajes


'''
{'nombre': 'Howard the Duck', 
'identidad': 'Howard (Last name unrevealed)', 
'empresa': 'Marvel Comics', 
'altura': '79.349999999999994', 
'peso': '18.449999999999999', 
'genero': 'M', 
'color_ojos': 'Brown', 
'color_pelo': 'Yellow', 
'fuerza': '2', 
'inteligencia': ''}
'''
def mostrar_personaje_mas_alto():
    video_mas_largo = calcular_max_min(lista_personajes,"altura","max")

def calcular_max_min(lista:list,clave:str,tipo="max"):
    '''
        clasifico la informacion, entre maximos y minimos
        list: tiene que ser una lista de diccionarios
        clave: tiene que representar una clave del diccionario que contenga un valor numerico
        tipo: solo puede ser maximo o minimo

        retorno: ele elemento(dict) que contiene el valor maximo
    '''
    if(type(lista) == type([]) and len(lista)>0 and type(clave) == type('')):
        elemento_max_min = lista[0]
        for elemento in lista:
            if tipo == 'max' and float(elemento[clave]) > float(elemento_max_min[clave]):
                    elemento_max_min = elemento
            elif tipo == 'min' and float(elemento[clave]) < float(elemento_max_min[clave]):
                elemento_max_min = elemento
        return elemento_max_min

def mostrar_personaje_mas_alto():
    video_mas_largo = calcular_max_min(lista_personajes,"altura","max")

mostrar_personaje_mas_alto()


