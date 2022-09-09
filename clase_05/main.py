from data import lista_bzrp
from calculos import calcula_maximo_minimo
from calculos import calcular_promedio_tiempo
from calculos import calcular_promedio_vistas
from calculos import calcular_tema_mas_corto
from calculos import calcular_tema_mas_largo
from calculos import calcular_tema_mas_visto
from calculos import calcular_tema_menos_visto

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
            break

bzrp_app(lista_bzrp)































