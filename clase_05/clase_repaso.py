from clase_repaso_datos import lista_pokemones


'''
Crear la función "obtener_nombre_pokemon" la cual recibirá por
parámetro un diccionario que representará al pokemon, la función deberá obtener el nombre
y retornarlo como un string.

'''
def obtener_nombre_pokemon(pokemon):
        nombre_str = str(pokemon['nombre'])
        #print(nombre_str)
        return nombre_str

#obtener_nombre_pokemon(lista_pokemones[0])
    
'''
01.2
Crear la función "imprimir_pokemones" la cual recibirá por
parámetro una lista de pokemones e imprimirá sus nombres. Reutilizar 'obtener_nombre_pokemon'
'''
def imprimir_pokemones(lista):
    for pokemon in lista:
        nombres = obtener_nombre_pokemon(pokemon)
        print(nombres)

#imprimir_pokemones(lista_pokemones)

'''
02.1
Crear la función "tiene_id_par" la cual recibirá por parámetro un diccionario
que representará al pokémon y verificará que su id sea par, en caso de que sea par
retornará True, caso contrário retornará False.
'''
def tiene_id_par(poke):
    if poke['id']%2 == 0:
        #print('true')
        return True
    else:
        #print('false')
        return False

#tiene_id_par(lista_pokemones[0])

'''
02.2
Crear la función "obtener_id_pokemon" la cual recibirá por
parámetro un diccionario que representará al pokemon, la función deberá obtener el id
y retornarlo como un string.
'''
def obtener_id_pokemon(pokemon):
    id_str = str(pokemon['id'])
    #print(id_str)
    return id_str
#obtener_id_pokemon(lista_pokemones[4])    

'''
02.3
Crear la función "pokedex_imprimir_pokemon_id_par" la cual recibirá por parámetro
la lista de pokemones y deberá imprimir solo los que cumplan con la condición de
tener un ID par. Reutilizar las funciones:
    'tiene_id_par', 'obtener_nombre_pokemon'
'''
def pokedex_imprimir_pokemon_id_par(lista):
    for pokemon in lista:
        id = tiene_id_par(pokemon)
        if id:
            id_int = int(obtener_id_pokemon(pokemon))
            if id_int % 2 == 0:
                nombre = obtener_nombre_pokemon(pokemon)
                print('Nombre: {0} | ID:{1}'.format(nombre, pokemon['id']))

#pokedex_imprimir_pokemon_id_par(lista_pokemones)    

'''
03.1
Crear la función "id_multiplo_25" la cual recibe por parámetro un diccionario
que representará al pokémon y verificará que su id múltiplo de 25, en caso de que
lo sea retornará True, caso contrário retornará False.
'''

def id_multiplo_25(pokemon):
    if pokemon['id'] % 25 == 0:
        #print('true')
        return True
    else:
        #print('false')
        return False
'''
version mas carto de la funcion anterior
 def id_multiplo_25(pokemon):
    return pokemon['id'] % 25 == 0:
'''   
       
#id_multiplo_25(lista_pokemones[5])
'''
03.2
Crear la función "pokedex_imprimir_pokemon_id_mul_25" la cual recibirá por parámetro
la lista de pokemones y deberá imprimir solo los que cumplan con la condición de
tener un ID múltiplo de 25. Reutilizar las funciones:
    'id_multiplo_25', 'obtener_nombre_pokemon'
'''
def pokedex_imprimir_pokemon_id_mul_25(lista):
    for pokemon in lista:
        id_x_25 = id_multiplo_25(pokemon)
        if id_x_25:
            nombre = obtener_nombre_pokemon(pokemon)
            print(nombre)

#pokedex_imprimir_pokemon_id_mul_25(lista_pokemones)

'''
04.1
Crear la función "nombre_format_pokemon" la cual recibirá por
parámetro un diccionario que representará al pokemon, la función deberá
obtener el nombre y su número y retornarlo como un string formateado
respetando el estilo: #006 - charizard
Reutilizar las funciones:
    'obtener_id_pokemon', 'obtener_nombre_pokemon'
'''
def nombre_format_pokemon(pokemon):
    id_poke = int(obtener_id_pokemon(pokemon))
    nombre = obtener_nombre_pokemon(pokemon)
    id_nombre_str = '#{0:03d} - {1}'.format(id_poke, nombre) # 0:03.2
    print(id_nombre_str)
    return id_nombre_str

nombre_format_pokemon(lista_pokemones[5])
#nombre_format_pokemon(lista_pokemones[0])

'''
04.2
Crear la función "pokedex_imprimir_nombres_poke_fmt" la cual recibirá una lista de pokemones
y deberá imprimirlos formateados respetando el estilo: #006 - charizard
Reutilizar las funciones:
    "nombre_format_pokemon
'''

def pokedex_imprimir_nombres_poke_fmt(lista):
    for pokemon in lista:
        nombre_id = nombre_format_pokemon(pokemon)
        print(nombre_id)

#pokedex_imprimir_nombres_poke_fmt(lista_pokemones)

'''
Crear la función "calcular_max_dato" la cual recibirá por parámetro:
    La lista de pokemones
    Un string que representará el máximo
    Un string que representará el dato/key a calcular
La función retornará el valor máximo de la key calculada.
def calcular_max_dato(lista,tipo, clave):
    for pokemon in lista:
        
'''







    
   