habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]

lista_tupla = []

for h in habilidades:
    '''
    dic_nuevo = {}
    dicc = dict(h)
    clave = dicc['Nombre']
    valor = dicc['Poder']

    lista = [{'Nombre':'NUCLEO', 'Id':20, 'Tipo':'MP', 'Fuente':2},{'Nombre':'PVC de mexichem', 'Id':19, 'Tipo':'MP', 'Fuente':2}]

for elem in lista:      #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
    for k,v in elem.items():        #acedemos a cada llave(k), valor(v) de cada diccionario
        print(k, v)

    '''
    clave_nombre = h['Nombre'] #obtener valor almacenado en key 'Nombre'
    clave_poder = h['Poder']  #obtener valor almacenado en key 'Poder'
    tupla = (clave_nombre,clave_poder) #creo una variable llamada tupla y le asigno los valores de 
    lista_tupla.append(tupla)

tupla_ordenada = sorted(lista_tupla, key=lambda p: p[1]) #ordenar lista de tupla

lista_ordenada = list(tupla_ordenada)


habilidades_utn = {}
habilidades_utn['habilidades_UTN'] = lista_ordenada

lista_armas = habilidades_utn['habilidades_UTN']

n = 1

variable1 = list(habilidades_utn.items())[0][0]

print(variable1,":")

for habilidad_poder in lista_armas:
    poderes_str = "Habilidad {0} : {1} | Poder: {2}".format(n,habilidad_poder[0], habilidad_poder[1])
    print(poderes_str)
    n += 1



#print("{0} - {1} - {2}".format(i,lista_nombre[i], lista_apellidos[i]))


