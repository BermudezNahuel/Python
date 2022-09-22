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
    print ("\n Nombre: {0} | Altura: {1}\n".format(altura_min_nombre, altura_min))


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
    print ("\n Nombre: {1} | Altura: {0}\n".format(heroe_mas_pesado, heroe_mas_pesado_nombre))

def calcular_heroe_mas_liviano():
    heroe_mas_liviano = float(lista_personajes[0]['peso'])
    heroe_mas_liviano_nombre = ''
    for heroe in lista_personajes:
        peso = float(heroe['peso'])
        if peso < heroe_mas_liviano:
            heroe_mas_liviano = float(heroe['altura'])
            heroe_mas_liviano_nombre = heroe['nombre']
    print ("\n Nombre: {1} | Peso: {0}\n".format(heroe_mas_liviano, heroe_mas_liviano_nombre))
    

while True:
    print   (  
                '1 - Nombre y altura del heroe mas alto\n'
                '2 - Nombre y altura del heroe mas bajo\n'
                '3 - Altura promedio de los heroes\n'
                '4 - Nombre y peso del heroe mas pesado\n'
                '5 - Nombre y peso del heroe mas liviano\n'
                '6 - Nombre y altura de cada heroe\n'
                '7 - Salir del programa\n'
            )

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
    elif respuesta == 7:
        break


