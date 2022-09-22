from data_stark import lista_personajes
import re

# 1.1

def extraer_iniciales(nombre_heroe: str):
    if len(nombre_heroe) > 0:
        lista_nombre = nombre_heroe.replace("-", " ")
        lista_nombre = lista_nombre.split(" ")
        acumulador_iniciales = ""
        for elemento in lista_nombre:
            if elemento != "the":
                iniciales = elemento[0:1] + "."
                acumulador_iniciales += iniciales
        return acumulador_iniciales
    else:
        return "N/A"

# 1.2

def definir_iniciales_nombre(heroe: dict):
    if type(heroe) == dict:
        if 'nombre' in heroe:
            nombre_iniciales = extraer_iniciales(heroe['nombre'])
            heroe['iniciales'] = nombre_iniciales
            return heroe
        else:
            return False

# 1.3


def agregar_iniciales_nombre(lista_heroes: list):
    '''
    Modifica la lista de heroes, agregando una nueva key a diccionario

    lista_heroe: ingresar una lista.
    '''
    if type(lista_heroes) == list and len(lista_heroes) > 0:
        for heroe in lista_heroes:
            nombre_con_iniciales = definir_iniciales_nombre(heroe)
            if nombre_con_iniciales == False:
                print("El origen de datos no contiene el formato correcto")
        return True
    else:
        return False

# 1.4

def stark_imprimir_nombres_con_iniciales(lista_heroes: list):
    '''
    Recorre una lista de diccionario, le agrega a cada diccionario una nueva
    key con su respectivo valor. Finalmente imprime el nombre del heroe, con el
    valor de la nueva key

    lista_heroe: se debe ingresar la lista de heroes
    '''
    if type(lista_heroes) == list and len(lista_heroes) > 0:
        if not agregar_iniciales_nombre(lista_heroes):
            print('Error al agregar iniciales a la lista')
        else:
            for heroe in lista_heroes:
                print("*{0}({1})".format(heroe['nombre'], heroe['iniciales']))

# 2.1
def generar_codigo_heroe(id_heroe: int, genero_heroe: str):
    id_heroe = int(id_heroe)
    if (type(id_heroe) == int and
        len(genero_heroe) > 0 and
           (genero_heroe == "M" or
            genero_heroe == "F" or
            genero_heroe == "NB")):
        identificador = str(id_heroe)
        genero_codigo = genero_heroe + "-" + identificador
        if genero_heroe == "NB":
            identificador = "{0}-{1:07d}".format(genero_heroe, id_heroe)
            print(identificador)
        else:
            identificador = "{0}-{1:08d}".format(genero_heroe, id_heroe)
            return identificador
    else:
        print("Error")
        return "N/A"

# 2.2

def agregar_codigo_heroe(heroe: dict, id_heroe: int):
    if len(heroe) > 0:
        codigo_heroe = generar_codigo_heroe(id_heroe, heroe["genero"])
        if len(codigo_heroe) == 10:
            heroe['codigo_heroe'] = codigo_heroe
            return True
        else:
            False
    else:
        False

# 2.3
def stark_generar_codigos_heroes(lista_heroes):
    if len(lista_heroes) > 1:
        contador = 0
        for personajes in lista_personajes:
            if type(personajes) == dict and personajes['genero']:
                contador += 1
                id_personaje = contador
                agregar_codigo_heroe(personajes, id_personaje)
            else:
                print("El origen de datos no contiene el formato correcto")

        primero = lista_heroes[0]['codigo_heroe']
        ultimo = lista_heroes[-1]['codigo_heroe']

        mensaje ="Se asignaron {0} codigos\n*El codigo del primer heroes es:"
        mensaje +="{1}\n*El codigo del ultimo heroe es: {2}"
        mensaje = mensaje.format(contador, primero, ultimo)
        print(mensaje)
    else:
        print("El origen de datos no contiene el formato correcto")

# 3.1

def sanitizar_entero(numero_str: str):
    numero_str = numero_str.strip()
    if len(re.findall("[0-9]+", numero_str)) > 0:
        num = int(re.findall('[-+]?\d+', numero_str)[0])
        if num > 0:
            return int(num)
        else:
            return -2
    elif len(re.findall("[a-zA-Z]+", numero_str)) > 0:
        return -1
    else:
        return -3

# 3.2
def sanitizar_flotante(numero_str):
    numero_str = numero_str.strip()
    if len(re.findall("[0-9]+\.[0-9]+", numero_str)) > 0:
        num = float(re.findall('[-+]?\d+\.\d+', numero_str)[0])
        if num > 0:
            return num
        else:
            return -2
    elif len(re.findall("[a-zA-Z]+", numero_str)) > 0:
        return -1
    else:
        return -3

# 3.3

def sanitizar_string(valor_str,valor_por_defecto = ""):
    valor_str = valor_str.replace("/", " ")
    if valor_str == valor_por_defecto:
        return valor_por_defecto
    if len(re.findall('[0-9]+', valor_str)) > 0:
        valor = re.findall('\d+', valor_str)
        return "N/A"
    elif len(re.findall('[a-zA-Z]+', valor_str)) > 0:
        lista_valor = re.findall("[a-zA-Z]+[a-zA-Z]+", valor_str)
        valor = " "
        valor = ((valor.join(lista_valor)).lower()).strip()
        return valor

# 3.4

def sanitizar_dato(heroe, clave, tipo_dato):
    if clave in heroe.keys():
        if tipo_dato == "flotante":
            heroe[clave] = sanitizar_flotante(heroe[clave])
            return True
        elif tipo_dato == "entero":
            heroe[clave] = sanitizar_entero(heroe[clave])
            return True
        elif tipo_dato == "string":
            heroe[clave] = sanitizar_string(heroe[clave])
            return True
        else:
            print("Tipo de dato no reconocido")
    else:
        print("La clave especificada no existe en el héroe")
        return False


#3.5
def stark_normalizar_datos(lista_heroes):
    for heroe in lista_heroes:
        sanitizar_dato(heroe, "altura", "flotante")
        sanitizar_dato(heroe, "peso", "flotante")
        sanitizar_dato(heroe, "fuerza", "entero")
        sanitizar_dato(heroe, "color_pelo", "string")
        sanitizar_dato(heroe, "color_ojos", "string")
        sanitizar_dato(heroe, "inteligencia", "string")

# 4.1

def generar_indices_nombres(lista_heroes):
    if len(lista_heroes) > 0:
        lista_nombres_personajes = []
        for personajes in lista_heroes:
            if type(personajes) == dict and "nombre" in personajes.keys():
                lista_nombre = re.findall("[a-zA-Z]+", personajes["nombre"])
                for nombre in lista_nombre:
                    lista_nombres_personajes.append(nombre)
            else:
                print("El origen de datos no contiene el formato correcto")
        return lista_nombres_personajes
    else:
        print("El origen de datos no contiene el formato correcto")
    # print(lista_nombres_personajes)

# generar_indices_nombres(lista_personajes)

# 4.2


def stark_imprimir_indice_nombre(lista_heroes):
    lista_nombres = generar_indices_nombres(lista_heroes)
    mensaje = "-"
    mensaje = mensaje.join(lista_nombres)
    print(mensaje)

# stark_imprimir_indice_nombre(lista_personajes)

# 5.1


def convertir_cm_a_mtrs(valor_cm):
    '''
    retornar el número recibido, pero convertido a  la unidad metros

    valor_cm : ingresar un valor flotante
    '''
    if type(valor_cm) == float and valor_cm > 0:
        valor_mtrs = valor_cm / 100
        # print(valor_mtrs)
        return valor_mtrs
    else:
        return -1

# convertir_cm_a_mtrs(122.12)

# 5.2


def generar_separador(patron, largo, imprimir: bool = True):
    '''
    Genera un string que contenga el patrón especificado repitiendo 
    tantas veces como la cantidad recibida como parámetro 
    (uno junto al otro, sin salto de línea)
    Si el parámetro booleano recibido se encuentra en False se deberá 
    solo retornar el separador generado. Si se encuentra en True antes 
    de retornarlo, lo imprime por pantalla

    patron: un carácter que se utilizará como patrón para generar 
    el separador
    largo: un número que representa la cantidad de caracteres que 
    va ocupar el separador.
    imprimir: un parámetro opcional del tipo booleano

    '''
    if ((len(patron) > 0 and len(patron) < 3) and
            (largo > 0 and largo < 236)):
        mensaje = ""
        for elemento in range(largo):
            mensaje += patron
        if imprimir:
            # print(mensaje)
            return mensaje
        else:
            return mensaje
    else:
        return "N/A"

# generar_separador("*#",10)

# 5.3


def generar_encabezado(titulo):
    separador = generar_separador("*", 78)
    titulo = titulo.upper()
    encabezado = "{0}\n{1}\n{2}\n".format(separador, titulo, separador)
    print(encabezado)

# generar_encabezado("Principal")

# 5.4


def imprimir_ficha_heroe(heroe):
    nombre = heroe["nombre"]
    identidad = heroe["identidad"]
    consultora = heroe["empresa"]
    codigo = heroe["codigo_heroe"]
    altura = heroe["altura"]
    peso = heroe["peso"]
    fuerza = heroe["fuerza"]
    color_ojos = heroe["color_ojos"]
    color_pelo = heroe["color_pelo"]

    principal = generar_encabezado("Principal")
    mensaje = "NOMBRE DEL HÉROE: {0}\n"
    mensaje += "IDENTIDAD SECRETA:{1}\n"
    mensaje += "CONSULTORA:{2}\nCODIGO DE HEROE:{3}\n"
    mensaje = mensaje.format(nombre, identidad, consultora,codigo)
    print(mensaje)
    fisico = generar_encabezado("Fisico")
    mensaje_1 = "ALTURA: {0}\nPESO:{1}\nFUERZA:{2}\n"
    mensaje_1 = mensaje_1.format(altura, peso, fuerza)
    print(mensaje_1)
    rasgos_particulares = generar_encabezado("Señas Particulares")
    mensaje_2 = "COLOR DE OJOS: {0}\n"
    mensaje_2 += "COLOR DE PELO: {1}\n"
    mensaje_2 = mensaje_2.format(color_ojos,color_pelo)
    print(mensaje_2)

# imprimir_ficha_heroe(lista_personajes[1])

#5.5
def stark_navegar_fichas(lista_heroes):
    imprimir_ficha_heroe(lista_heroes[0])
    valor = 0
    while True: 
        print("[1]Ir a la Izquierda   [2]Ir a la derecha   [S]Salir")
        ingreso = input("ingrese la opcion:   ")
        if ingreso == "1" or ingreso == "2" or ingreso == "s" or ingreso == "S":
            if (ingreso).upper() == "S":
                break
            if valor > -24 and valor < 23:
                while True:
                    if int(ingreso) == 1:
                        valor -= 1
                        imprimir_ficha_heroe(lista_heroes[valor])
                        break
                    elif int(ingreso) == 2: 
                        valor += 1
                        imprimir_ficha_heroe(lista_heroes[valor])
                        break
            else:
                valor = 0
        else:
            print("Ingrese un valor correcto\n")
       
#stark_navegar_fichas(lista_personajes)

#6.1

def imprimir_menu():
    mensaje =   '''
                    1 - Imprimir la lista de nombres junto con sus iniciales
                    2 - Generar códigos de héroes
                    3 - Normalizar datos
                    4 - Imprimir índice de nombres
                    5 - Navegar fichas
                    S - Salir

                '''
    print(mensaje)


#6.2

def stark_menu_principal():
    imprimir_menu()
    eleccion = (input("Ingrese una opcion: ")).upper()
    return eleccion

#stark_menu_principal()


#6.3

def stark_marvel_app_3(lista_heroes):
    
    while True:
        opcion = stark_menu_principal()
        
        match opcion:
            case "1":
                stark_imprimir_nombres_con_iniciales(lista_heroes)
            case "2":
                stark_generar_codigos_heroes(lista_heroes)
            case "3":
                stark_normalizar_datos(lista_heroes)
            case "4":
                stark_imprimir_indice_nombre(lista_heroes)
            case "5":
                stark_navegar_fichas(lista_heroes)
            case "S":
                break

stark_marvel_app_3(lista_personajes)           

