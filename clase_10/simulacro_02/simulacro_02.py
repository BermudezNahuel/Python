from dataclasses import replace
import re
import fun_02

direccion = "C:/Users/Nahuel/Documents/TUP/P y L 1/programacion-y-laboratorio-1/clase_10/data_stark.json"
lista_personajes = fun_02.leer_json(direccion)
lista_para_imprimir = lista_personajes[:]

#lista_copia = lista_personajes[:]
#contenido = fun_02.mostrar_lista(lista_copia)
while True:
    menu = '''
    \n
    1 - TOP N PRIMEROS HEROES nombre e identidad
    2 - LISTA HEROES POR ALTURA nombre e identidad
    3 - LISTA DE HEROES POR FUERZA nombre e identidad
    4 - LISTA DE POR ENCIMA O DEBAJO DEL PROMEDIO DE HEROES nombre e identidad
    5 - LISTA DE HEROES POR INTELIGENCIA
    6 - GUARDAR LISTA CREADA
    7 - SALIR DE LA APLICACION
    \n
    '''
    print(menu)
    respuesta = input("Ingrese una opcion: ")
    respuesta = fun_02.validar_dato(respuesta, "[1-7]{1}")

    if respuesta == "1":
        print("\n")
        n_top = input("Ingrese un numero para realizar el top: \n")
        n_top = int(fun_02.validar_dato(n_top, "[0-9]{1,2}"))
        lista_para_imprimir = lista_personajes[:]
        n_top = fun_02.validar_len_lista(lista_para_imprimir, n_top)
        lista_para_imprimir = lista_para_imprimir[:n_top]
        contenido = fun_02.mostrar_lista(lista_para_imprimir)
    elif respuesta == "2":
        print("\n")
        tipo = input("Quiere lista en forma ascendente (asc) o descendente (desc): ")
        tipo = fun_02.validar_dato(tipo,"asc|desc")
        lista_para_imprimir = lista_personajes[:]
        lista_para_imprimir = fun_02.ordenar(lista_para_imprimir,"altura", tipo)
        fun_02.mostrar_lista(lista_para_imprimir, "altura")
    elif respuesta == "3":
        print("\n")
        tipo = input("Quiere lista en forma ascendente (asc) o descendente (desc): ")
        tipo = fun_02.validar_dato(tipo,"asc|desc")
        lista_para_imprimir = lista_personajes[:]
        lista_para_imprimir = fun_02.ordenar(lista_para_imprimir,"fuerza", tipo)
        fun_02.mostrar_lista(lista_para_imprimir, "fuerza")
    elif respuesta == "4":
        print("\n")
        clave = input("Ingrese que valor quiere: altura|peso|fuerza: ")
        clave = fun_02.validar_dato(clave, "altura|peso|fuerza")
        menor_mayor = input("Heroes por arriba o por debajo ('menor') del promedio('mayor'): ")
        menor_mayor = fun_02.validar_dato(menor_mayor,"menor|mayor")
        lista_para_imprimir = lista_personajes[:]
        lista_para_imprimir = fun_02.buscar_promedio_menor_mayor(lista_para_imprimir,clave,menor_mayor)
        fun_02.mostrar_lista(lista_para_imprimir,clave)
    elif respuesta == "5":
        lista_para_imprimir = lista_personajes[:]
        lista_para_imprimir = fun_02.buscador(lista_para_imprimir)
        fun_02.mostrar_lista(lista_para_imprimir,"inteligencia")
    elif respuesta == "6":
        fun_02.guardar_archivo("clase_10/simulacro_02/lista_personajes.csv", lista_para_imprimir)
    elif respuesta == "7":
        break

