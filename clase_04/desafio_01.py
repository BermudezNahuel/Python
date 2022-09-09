from data_stark import lista_personajes


def listado_personajes_masculinos():
    lista_masculinos = []
    for heroes in lista_personajes:
        generoM = heroes['genero']
        if generoM == 'M':
            lista_masculinos.append(heroes['nombre'])
    print('heroes masculinos',lista_masculinos)

def listado_personajes_femeninos():
    lista_femeninos = []

    for heroes in lista_personajes:
        generoF = heroes['genero']
        if generoF == 'F':
            lista_femeninos.append(heroes['nombre'])
    print('Heroinas: ',lista_femeninos)


def altura_max_heroe_masculino():
    altura_max = float(lista_personajes[0]['altura'])
    altura_max_nombre = ''

    for heroes in lista_personajes:
        generoM = heroes['genero']
        if generoM == 'M':
            altura = float(heroes['altura'])
            if altura > altura_max:
                altura_max = altura
                altura_max_nombre = heroes['nombre']
    print ("\n Nombre: {0} | Altura: {1}\n".format(altura_max_nombre, altura_max))

def altura_max_heroe_femenino():
    altura_max = float(lista_personajes[0]['altura'])
    altura_max_nombre = ''

    for heroes in lista_personajes:
        generoF = heroes['genero']
        if generoF == 'F':
            altura = float(heroes['altura'])
            if altura > altura_max:
                altura_max = altura
                altura_max_nombre = heroes['nombre']
    print ("\n Nombre: {0} | Altura: {1}\n".format(altura_max_nombre, altura_max))


def calcular_heroe_mas_bajo_masculino():
    altura_min = float(lista_personajes[0]['altura'])
    altura_min_nombre = lista_personajes[0]['nombre']
    for heroes in lista_personajes:
        generoM = heroes['genero']
        altura = float(heroes['altura'])
        if generoM == 'M':
            altura = float(heroes['altura'])
            if altura < altura_min:
                altura_min = altura
                altura_min_nombre = heroes['nombre']
    print ("\n El heroe mas bajo es: {0} con {1} cm altura".format(altura_min_nombre, altura_min))


def calcular_heroe_mas_bajo_femenino():
    altura_min = float(lista_personajes[3]['altura'])
    altura_min_nombre = lista_personajes[3]['nombre']
    for heroes in lista_personajes:
        generoF = heroes['genero']
        altura = float(heroes['altura'])
        if generoF == 'F':
            altura = float(heroes['altura'])
            if altura < altura_min:
                altura_min = altura
                altura_min_nombre = heroes['nombre']
    print ("\n La heroina mas baja es: {0} con {1} cm de altura".format(altura_min_nombre, altura_min))


def promedio_altura_masculino():
    acumulador_altura = 0
    contador = 0

    for h in lista_personajes:
        generoM = h['genero']
        if generoM == 'M':
            acumulador_altura += float(h['altura'])
            contador += 1
    promedio = acumulador_altura/contador
    print('Altura promedio heroes:', promedio)

def promedio_altura_femenino():
    acumulador_altura = 0
    contador = 0

    for h in lista_personajes:
        generoF = h['genero']
        if generoF == 'F':
            acumulador_altura += float(h['altura'])
            contador += 1
    promedio = acumulador_altura/contador
    print('Altura promedio heroinas:', promedio)
    

def calcular_color_ojos():

    lista_ojos = []

    for h in lista_personajes:
        color = h['color_ojos']
        lista_ojos.append(color)
    set_ojos = set(lista_ojos)

    for color in list(set_ojos):
        cantidad_heroes = 0
        for h in lista_personajes:
            if h['color_ojos'] == color:
                cantidad_heroes += 1
        print('Color:', color, ' son', cantidad_heroes, 'de heroes')


def calcular_color_pelo():

    lista_pelo = []

    for h in lista_personajes:
        color = h['color_pelo']
        lista_pelo.append(color)
    set_pelo = set(lista_pelo)

    for color in list(set_pelo):
        cantidad_heroes = 0
        for h in lista_personajes:
            if h['color_pelo'] == color:
                cantidad_heroes += 1
        print('Color de pelo:', color, ' son', cantidad_heroes, 'de heroes')

'''
dict_ojos = {}
for h in lista_personajes:
    color_ojos = h['color_ojos']
    if color_ojos not in dict_ojos.keys():
        dict_ojos[color_ojos] = 1 # si no existe el color se crea la key de ese color y se le asigna el valor 1
    else: # si existe el color le sumo uno a esa variable
        dict_ojos[color_ojos] += 1 

for color in dict_ojos.item():
    mensaje = ''
    print(mensaje)

'''
def calcular_tipos_inteligencia():
    dic_inteligencia = {}
    
    for h in lista_personajes:
        inteligencia = h['inteligencia']
        if inteligencia not in dic_inteligencia.keys():
            if inteligencia == '':
                inteligencia = 'No tiene'

            dic_inteligencia[inteligencia] = 1
        else:
            dic_inteligencia[inteligencia] += 1
            
    print(dic_inteligencia)


def listar_heroes_por_color_ojo():
    lista_ojos = []

    for h in lista_personajes:
        color = h['color_ojos']
        lista_ojos.append(color)
    set_ojos = set(lista_ojos)

    dic_nombre_color_ojos = {}
    for color in list(set_ojos):
        for h in lista_personajes:
            if h['color_ojos'] == color:
                if h['color_ojos'] not in dic_nombre_color_ojos.keys():
                    dic_nombre_color_ojos[color] = [h['nombre']]
                else:       
                    dic_nombre_color_ojos[color].append(h['nombre'])
        print('\n\n Colores de ojos {0} \n Personajes{1}'.format(color,dic_nombre_color_ojos[color]))
    

def listar_heroes_por_color_pelo():
    lista_pelo = []

    for h in lista_personajes:
        color = h['color_pelo']
        lista_pelo.append(color)
    set_pelo = set(lista_pelo)

    dic_nombre_color_pelo = {}
    for color in list(set_pelo):
        for h in lista_personajes:
            if h['color_pelo'] == color:
                if h['color_pelo'] not in dic_nombre_color_pelo.keys():
                    dic_nombre_color_pelo[color] = [h['nombre']]
                else:
                    dic_nombre_color_pelo[color].append(h['nombre'])

        print('\n\n Colores de pelo {0} \n Personajes{1}'.format(color,dic_nombre_color_pelo[color]))


def listar_nombre_por_inteligencia():
    
    lista_inteligencia = []

    for heroes in lista_personajes:
        heroes_inteligencia = heroes['inteligencia']
        lista_inteligencia.append(heroes_inteligencia)
    set_inteligencia = set(lista_inteligencia)

    dic_nombre_inteligencia = {}
    for inteligencia in list(set_inteligencia):
        for h in lista_personajes:
            if h['inteligencia'] == inteligencia:
                if h['inteligencia'] not in dic_nombre_inteligencia.keys():
                    dic_nombre_inteligencia[inteligencia] = [h['nombre']]# de esta manera creo una lista dentro de una key
                else:
                    dic_nombre_inteligencia[inteligencia].append(h['nombre'])# de esta manero agrego elementos a la key
                    
        mensaje = '\n\n Tipos de Inteligencia: {0} \n Personajes: {1}'
        print(mensaje.format(   inteligencia,
                                dic_nombre_inteligencia[inteligencia]))


while True:
    respuesta = int(input(  
                            'Ingrese que quiere saber:\n'
                            '01 - Personajes Masculinos\n'
                            '02 - Personajes Femeninos\n'
                            '03 - Personaje Masculino Mas Alto\n'
                            '04 - Personaje Femenino Mas Alto\n'
                            '05 - Personaje Masculino Mas Bajo\n'
                            '06 - Personaje Femenino Mas Bajo\n'
                            '07 - Altura Promedio Personajes Masculinos\n'
                            '08 - Altura Promedio Personajes Femeninos\n'
                            '09 - Colores de ojos de personajes\n'
                            '10 - Colores de pelo de personajes\n'
                            '11 - Tipos de Inteligencia\n'
                            '12 - Personajes por color de ojos\n'
                            '13 - Personajes por color de pelo\n'
                            '14 - Personajes por tipo de inteligencia\n'
                            '15 - Salir del programa\n'
                    ))
    
    if respuesta == 1:
        listado_personajes_masculinos()
    elif respuesta == 2:
        listado_personajes_femeninos()
    elif respuesta == 3:
        altura_max_heroe_masculino()
    elif respuesta == 4:
        altura_max_heroe_femenino()
    elif respuesta == 5:
        calcular_heroe_mas_bajo_masculino()
    elif respuesta == 6:
        calcular_heroe_mas_bajo_femenino()   
    elif respuesta == 7:
        promedio_altura_masculino()
    elif respuesta == 8:
        promedio_altura_femenino()
    elif respuesta == 9:
        calcular_color_ojos()
    elif respuesta == 10:
        calcular_color_pelo()
    elif respuesta == 11:
        calcular_tipos_inteligencia()
    elif respuesta == 12:
        listar_heroes_por_color_ojo()
    elif respuesta == 13:
        listar_heroes_por_color_pelo()
    elif respuesta == 14:
        listar_nombre_por_inteligencia()
    elif respuesta == 15:
        break

