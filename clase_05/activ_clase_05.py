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
for heroe_n in lista_personajes:
    print(heroe['nombre'])



'''

lista_vacia = []
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

#print(lista_personajes[0])
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
    con el siguiente formato Nombre : heroe
    
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
#stark_imprimir_nombres_heroes(lista_personajes)

def obtener_nombre_y_dato(heroe,clave):
    '''
    Toma un diccionario y devuelve el nombre
    del personaje y el valor de un dato

    heroe: valor de un 
    
    '''
    nombre = obtener_nombre(heroe) #creo una VAR y almaceno return que da la FN
    info = heroe[clave]
    nombre_info = nombre + " | " + clave + ": " + info
    #print(nombre_info)
    return nombre_info
    
#obtener_nombre_y_dato(lista_personajes[0],'fuerza')

def stark_imprimir_nombres_alturas(lista):
    for h in lista:
        variable1 = obtener_nombre_y_dato(h,'fuerza') # creo una VAR para lamacenar el return de la FN obtner_nombre_etc...
        imprimir_dato(variable1) #utilizo la FN, paso como parametro la VAR creada anteriormente
    
#stark_imprimir_nombres_alturas(lista_personajes)

def calcular_max(lista, clave):
    valor_max = lista[0]
    nombre = lista[0]['nombre']
    for heroes in lista:
        if valor_max[clave] < heroes[clave]:
            valor_max = heroes
            nombre = obtener_nombre(heroes)

    #print('maximo',nombre, '|', valor_max[clave])
    return nombre, valor_max[clave]
calcular_max(lista_personajes,'peso')


def calcular_min(lista, clave):
    valor_max = lista[0]
    nombre = lista[0]['nombre']
    for heroes in lista:
        if valor_max[clave] > heroes[clave]:
            valor_max = heroes
            nombre = obtener_nombre(heroes)

    #print('minimo',nombre, '|', valor_max[clave])
    return nombre, valor_max[clave]

calcular_min(lista_personajes,'peso')

















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