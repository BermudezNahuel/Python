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


lista_de_elementos = []

for h in habilidades:
    clave_nombre = h['Nombre'] #obtener valor almacenado en key 'Nombre'
    clave_poder = h['Poder']  #obtener valor almacenado en key 'Poder'
    elemento = (clave_nombre,clave_poder) #creo una variable y le asigno los valores
    lista_de_elementos.append(elemento)

#print(lista_de_elementos)--> para verificar si se construyo la lista

#Convertir la lista de elementos a una tupla, para ordenar de menor a mayor
tupla_de_elementos = tuple(lista_de_elementos) #conrversion de list -->tuple
tupla_de_elementos = sorted(tupla_de_elementos, key=lambda p: p[1]) #ordenar lista de tupla
#print(tupla_de_elementos) #-->Verificar si se ordenaron los elementos

#Creo el diccionario habilidades_UTN
habilidades_UTN = {'Habilidades_UTN': tupla_de_elementos}
#Accedo al valor de la clave 'Hablidades_UTN', para usar un for
lista_poderes = habilidades_UTN["Habilidades_UTN"]


#Obtengo el nombre de la key en la siguiente linea
nombre_key = list(habilidades_UTN.items())[0][0]
#Imprimo con el formato deseado
print(nombre_key,":")

#Ahora lo recorro con un for
n = 1
for hab_y_poder in lista_poderes:
    #Le doy un formato a los que quiero imprimir
    hab_y_poder_str = ("Habilidad {0} : {1} | Poder: {2}".format(n,hab_y_poder[0],hab_y_poder[1]))
    print(hab_y_poder_str)
    n += 1
