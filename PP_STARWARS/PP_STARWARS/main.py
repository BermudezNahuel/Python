import json

'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones

def starwars_app():
    lista_personajes = funciones.cargar_json("PP_STARWARS\PP_STARWARS\data.json")
    lista_copia = lista_personajes[:]
    lista_normalizada = funciones.normalizar_datos(lista_copia,"height")
    lista_normalizada = funciones.normalizar_datos(lista_copia,"mass")

    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input("Ingrese una opcion: ")
        if(respuesta=="1"):
            print("\n")
            copia_lista = lista_normalizada[:]
            copia_lista = funciones.ordenar_personajes(copia_lista,"height")
            contenido = funciones.mostrar_lista(copia_lista)
        elif(respuesta=="2"):
            copia_lista = lista_normalizada[:]
            masculino = funciones.listar_por_genero(copia_lista,"male")
            femenino = funciones.listar_por_genero(copia_lista,"female")
            sin_genero =  funciones.listar_por_genero(copia_lista,"n/a")
        elif(respuesta=="3"):
            print("\n")
            copia_lista = lista_normalizada[:]
            copia_lista = funciones.ordenar_personajes(copia_lista,"mass")
            contenido = funciones.mostrar_lista(copia_lista)
        elif(respuesta=="4"):
            patron = input("Ingrese el nombre del personaje: ")
            copia_lista = lista_normalizada[:]
            copia_lista = funciones.buscador_personajes(copia_lista,patron)
            contenido = funciones.mostrar_lista(copia_lista)
        elif(respuesta=="5"):
            funciones.guardar_archivo("PP_STARWARS/archivo.csv",contenido)
            print("5 - Exportar lista personajes a CSV\n")
        elif(respuesta=="6"):
            break


starwars_app()

