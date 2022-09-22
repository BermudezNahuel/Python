import re


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
            A - Imprimir la lista de nombres junto con sus iniciales
            B - Generar códigos de héroes
            C - Normalizar datos
            D - Imprimir índice de nombres
            E - Navegar fichas
            S - Salir
            '''
    imprimir_menu_desafio_05(menu)
    eleccion = input("Ingrese opcion elegida(A,B,C,D,E,S)").upper()
    if re.match('[A-O,Z]',eleccion):
        print(eleccion)

    else:
        print("mal")
        return -1

stark_menu_principal_desafio_5()

