from distutils.log import info
from pickle import FALSE
import string
from data_stark import lista_personajes

def stark_normalizar_datos(lista,clave_altura,clave_peso,clave_fuerza):
    '''
    Esta funcion toma los valores numericos de los personajes que se encuentran
    en formato string, los convierte en float e int y los modifica en los diccionarios
    
    lista: lista de personajes
    clave_altura: altura del personaje 
    clave_peso: peso del personaje 
    clave_fuerza: fuerza del personaje 

    '''
    if(len(lista) > 0 and type(lista) == type([])):
        
        for h in lista:
            if  (
                    type(h[clave_altura]) == float and 
                    type(h[clave_peso]) == float and  
                    type(h[clave_fuerza]) == int
                ):
                pass
            else:
                h[clave_altura] = float(h[clave_altura])
                h[clave_peso]= float(h[clave_peso])
                h[clave_fuerza] = int(h[clave_fuerza])
            
            lista_modificada = 'si'    
    else:
        print('Error: lista vacia')
    if lista_modificada == 'si':
        print('Datos normalizados')

stark_normalizar_datos(lista_personajes, 'altura','peso','fuerza')

def imprimir_dato(info:str):
    '''
    Toma un dato, valida si es un string y luego lo imprime
    info: valor que debe ser un string
    '''
    if type(info) == str:
        print(info)

def obtener_nombre(heroe):
    '''
    Obtiene el nombre el un heroe y lo devuelve
    con el siguiente formato "Nombre : heroe"
    
    heroe: es un diccionario
    '''
    nombre_personaje = 'Nombre: '
    nombre_personaje += heroe['nombre']
    #print(nombre_personaje)    
    return nombre_personaje

def stark_imprimir_nombres_heroes(lista):
    '''
    Recibe una lista y luego imprime usando las
    funciones obtener_nombre() e imprimir_dato()

    lista: recibe una lista
    '''
    if len(lista) > 0:
        for h in lista:
            nombre_formateado = obtener_nombre(h) #creo una variable y almaceno el valor de return de la FN
            imprimir_dato(nombre_formateado) # le paso como parametro a la FN la variable que cree, que almacena el return de la FN anterior
    else: 
        return -1

def obtener_nombre_y_dato(heroe,clave):
    '''
    Toma un diccionario y devuelve el nombre
    del personaje y el valor de un dato

    heroe: diccionario
    clave: ingrese key del diccionario 
    
    '''
    nombre = obtener_nombre(heroe) #creo una VAR y almaceno return que da la FN
    info = heroe[clave]
    nombre_info = '{0}|{1}:{2}'.format(nombre,clave, info)
    #print(nombre_info)
    return nombre_info

def stark_imprimir_nombres_alturas(lista):
    '''
    Toma una lista de heroes, y devuelve el nombre
    y altura de cada personaje de la lista

    lista: lista de elementos
    '''
    if len(lista) > 0:
        for h in lista:
            variable1 = obtener_nombre_y_dato(h,'fuerza') # creo una VAR para lamacenar el return de la FN obtner_nombre_etc...
            imprimir_dato(variable1) #utilizo la FN, paso como parametro la VAR creada anteriormente
    else:
        return -1

def calcular_max(lista, clave):
    '''
    Recorre una lista de diccionarios, compara key
    determinada, retornando el diccionario con el
    valor de key mas pequeño.

    lista: ingresar una lista
    clave: ingrese una key del diccionario

    '''
    valor_max = lista[0]
    for heroes in lista:
        if valor_max[clave] < heroes[clave]:
            valor_max = heroes
    #print('Maximo',valor_max['nombre'], '|', valor_max[clave])
    return valor_max

def calcular_min(lista, clave):
    '''
    Recorre una lista de diccionarios, compara key
    determinada, retornando el diccionario con el
    valor de key mas pequeño.

    lista: ingresar lista de elementos
    clave: ingresar una key del diccionario
    '''
    valor_min = lista[0]
    for heroes in lista:
        if heroes[clave] < valor_min[clave]:
            valor_min = heroes
    #print(valor_min)
    return valor_min

def calcular_max_min_dato(lista: list, tipo: str, clave:str):
    '''
    Recorre una lista de diccionarios, compara key
    determinada, retornando el diccionario con el
    valor de key mas pequeño o mas grande, dependiendo
    del tipo que se haya ingresado.

    lista: ingrese el nombre de una lista
    tipo: ingrese maximo o minimo
    clave: ingrese una key

    '''
    if (tipo == 'maximo'):
        heroe = calcular_max(lista, clave)
    elif (tipo == 'minimo'):
        heroe =  calcular_min(lista, clave)
    return heroe 

def stark_calcular_imprimir_heroe(lista, tipo, clave):
    '''
    Calcula en imprime los valores maximo o minimo
    ,de una comparacion de elementos que pertenecen a un diccionario

    lista: introducir el nombre una lista
    tipo: ingresar minimo o maximo,(string)
    clave: ingresar la key que se quiera comparar
    '''
    personaje = calcular_max_min_dato(lista, tipo, clave)
    valor = obtener_nombre_y_dato(personaje,clave)

    if tipo == 'maximo':
        mensaje_str = 'Mayor {0} {1}'.format(clave, valor)
    else:
        mensaje_str = 'Menor {0} {1}'.format(clave, valor)
    
    info_format = imprimir_dato(mensaje_str)

def sumar_dato_heroe(lista, clave):
    '''
    Recorre una lista de diccionarios, y suma todos
    los valores de una key determinada, y retorna el valor

    lista: ingresar nombre de una lista
    clave: ingresar key elegida
    '''
    acumulador_clave = 0
    for heroe in lista:
        if (type(heroe) == type({}) and len(heroe) >0 ):
            acumulador_clave += heroe[clave]
    #print(acumulador_clave)
    return acumulador_clave
#sumar_dato_heroe(lista_personajes, 'altura')

def dividir(dividendo, divisor):
    '''
    Realiza una division entre 2 valores y
    retorna el resultado

    dividendo: ingresar dividendo
    divisor: ingresar divisor
    '''
    if divisor == 0:
        return 0
    else:
        resultado = dividendo/divisor
        return resultado

def calcular_promedio(lista, clave):
    '''
    Realiza el promedio de los valores
    de una key determinada de todos los
    diccionarios de la lista

    lista: ingresar nombre de lista
    clave: ingresar nombre de key
    '''
    dividendo = sumar_dato_heroe(lista,clave)
    divisor = len(lista)
    resultado = dividir(dividendo, divisor)
    #print(resultado) 
    return  resultado
#calcular_promedio(lista_personajes, 'altura')

def stark_calcular_imprimir_promedio_altura(lista):
    '''
    Realiza el promedio de la altura de todos los superheroes

    lista: ingresar nombre de lista
    '''
    if len(lista):
        dividendo = sumar_dato_heroe(lista, 'altura')
        divisor = len(lista)
        promedio = dividir(dividendo, divisor)
        print('Altura Promedio:',promedio )
    else:
        return -1
#stark_calcular_imprimir_promedio_altura(lista_personajes)


def imprimir_menu():
    '''
    imprime un menu con opciones
    '''

    info = '''
            1 - Nombre y altura del heroe mas alto
            2 - Nombre y altura del heroe mas bajo
            3 - Altura promedio de los heroes
            4 - Nombre y peso del heroe mas pesado
            5 - Nombre y peso del heroe mas liviano
            6 - Nombre y altura de cada heroe
            7 - Salir del programa
            '''# de esta manera creo un strin multilinea
    imprimir_dato(info)

def validar_entero(info):
    '''
    Valida que el string ingresado
    tenga por lo menos 2 digitos, y 
    luego lo tranforma a un entero

    info: ingesar numero
    '''

    if len(info) <= 2 and len(info) > 0:
        #print(info)
        return True
    else:
        return False


def stark_menu_principal():
    '''
    Imprime el menu principal y pregunta al
    usuario que opcion quiere elegir. Si la opcion
    es valida restorna la opcion en formato integer
    '''
    imprimir_menu()
    opcion = input('Elija una opcion')
    
    validar = validar_entero(opcion)
    if validar:
        opcion = int(opcion)
        #print(opcion)
        return opcion
    else:
        return -1


def stark_marvel_app(lista):
    '''
    recibire por parámetro la lista de héroes y 
    se encargará de la ejecución principal de nuestro programa

    lista: ingresar nombre de la lista
    '''
    
    while True:
        opcion = stark_menu_principal()
        
        if opcion == 1:
                stark_calcular_imprimir_heroe(lista, 'maximo', 'altura')
                
        elif opcion == 2:
                stark_calcular_imprimir_heroe(lista, 'minimo', 'altura')
               
        elif opcion == 3:
                stark_calcular_imprimir_promedio_altura(lista)
                
        elif opcion == 4:
                stark_calcular_imprimir_heroe(lista, 'maximo', 'peso')
                
        elif opcion == 5:
                stark_calcular_imprimir_heroe(lista, 'minimo', 'peso')
                
        elif opcion == 6:
                stark_imprimir_nombres_heroes(lista)
                
        elif opcion == 7:
            break
        
stark_marvel_app(lista_personajes)














'''


def nombre_altura_heroes():
    for heroe_nya in lista_personajes:
        nombre = heroe_nya['nombre']
        altura = heroe_nya['altura']
        print("\n Nombre:", nombre, "|", "Altura: ", altura)

def calcular_heroe_mas_alto():
    altura_max = float(lista_personajes[0]['altura'])
    altura_max_nombre = ''

    for heroes in lista_personajes:
        altura = float(heroes['altura'])
        if altura > altura_max:
            altura_max = altura
            altura_max_nombre = heroes['nombre']
    print ("\n Nombre: {0} | Altura: {1}\n".format(altura_max_nombre, altura_max))


def calcular_heroe_mas_bajo():
    altura_min = float(lista_personajes[0]['altura'])
    altura_min_nombre = lista_personajes[0]['nombre']
    for heroes in lista_personajes:
        altura = float(heroes['altura'])
        if altura < altura_min:
            altura_min = altura
            altura_min_nombre = heroes['nombre']
    print ("\n Nombre: {0} | Altura: {1}".format(altura_min_nombre, altura_min))


def promedio_heroe_altura():
    acumulador_altura = 0
    altura_promedio = ''
    for heroe in lista_personajes:
        altura = float(heroe['altura'])
        acumulador_altura += altura
        altura_promedio = acumulador_altura / len(lista_personajes)
    print("\n Altura promedio:{0}\n".format(altura_promedio))

def calcular_heroe_mas_pesado():
    heroe_mas_pesado = float(lista_personajes[0]['peso'])
    heroe_mas_pesado_nombre = ''
    for heroe in lista_personajes:
        peso = float(heroe['peso'])
        if peso > heroe_mas_pesado:
            heroe_mas_pesado = float(heroe['altura'])
            heroe_mas_pesado_nombre = heroe['nombre']
    print ("\n Nombre: {1} | Altura: {0}".format(heroe_mas_pesado, heroe_mas_pesado_nombre))

def calcular_heroe_mas_liviano():
    heroe_mas_liviano = float(lista_personajes[0]['peso'])
    heroe_mas_liviano_nombre = ''
    for heroe in lista_personajes:
        peso = float(heroe['peso'])
        if peso < heroe_mas_liviano:
            heroe_mas_liviano = float(heroe['altura'])
            heroe_mas_liviano_nombre = heroe['nombre']
    print ("\n Nombre: {1} | Peso: {0}".format(heroe_mas_liviano, heroe_mas_liviano_nombre))
    

while True:
    print(  '1 - Nombre y altura del heroe mas alto\n')
    print(  '2 - Nombre y altura del heroe mas bajo\n')
    print(  '3 - Altura promedio de los heroes\n')
    print(  '4 - Nombre y peso del heroe mas pesado\n')
    print(  '5 - Nombre y peso del heroe mas liviano\n')
    print(  '6 - Nombre y altura de cada heroe')
         

    respuesta = int(input("\n Ingrese el numero del menu: "))
 

    if respuesta == 1:
        calcular_heroe_mas_alto()
    elif respuesta == 2:
        calcular_heroe_mas_bajo()
    elif respuesta == 3:
        promedio_heroe_altura()
    elif respuesta == 4:
        calcular_heroe_mas_pesado()
    elif respuesta == 5:
        calcular_heroe_mas_liviano()
    elif respuesta == 6:
        nombre_altura_heroes()
'''       