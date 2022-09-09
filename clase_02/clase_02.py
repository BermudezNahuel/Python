
terminal = "123"

try:
    peso = int(terminal)
except:
    print("error")

'''
variable.isnumeric() --> permite saber si la variable es un numero
'''

'''
Una lista es una sucesion de cosas

lista = [1,2,3,4,5, "hola"]

tuple --> lista que no se pueden alterar ni orden, ni contenidos

diccionario --> coleccion de elementos, pero puedo darle un nombre y un valor a cada campo
por ejemple: diccionario = {"nombre": "nahuel", "edad": 29}


set-->  es como una lista declarada ente llaves, no contiene elemtos repetidos

.append() --> metodo para agregar elementos a una lista
por ejemplo:

lista = [] #asi se crea una lista vacia
lista.append(1) #agregar un elemento
print(lista[0])

lista = [1,2,3,4,5,6]
print(lista[3])

print(lista[3:4])

print[-1] #da la vuelat y devuelve el ultimo numero

#recorrer lista 
for numero in lista:
    print(numero)

lista_temas = ["asd", "qwe", "zxc"]
for tema in lista_temas:
    print(tema)

###Diccionario###

dic ={} #diccionario vacio

dic = {'clave': "hola"}

#lista con dciconarios adentro

lista_nombre = []
lista_apellidos = []

for i in range(3):
    nombre = input("ingrese nombre")
    apellido = input("ingrese apellido")
    lista_nombre.append(nombre)
    lista_apellidos.append(apellido)
#len(lista_nombre) --> da el largo de la lista

# primera solucion -->for i in range(len(lista_nombres)):
# segunda solucion -->for nombre in lista_nombre:



# "{0}" --> es un comodina

cantida_de_empleados = 3


'''
cantida_de_empleados = 3
lista_nombre = []
lista_apellidos = []
lista_empelados = []

for i in range(cantida_de_empleados):
    print(
        "{0} - {1} - {2}".format(i,lista_nombre[i], lista_apellidos[i])
    )
 
dic = {}


for i in range(cantida_de_empleados):
    dic_empleado = {}
    nombre = input("ingrese nombre")
    apellido = input("ingrese apellido")

    lista_nombre.append(nombre)
    lista_apellidos.append(apellido)
    dic_empleado["nombre"] = nombre
    dic_empleado["apellido"] = apellido

    lista_empelados.append(dic_empleado)




#for i in range(cantida_de_empleados):
    #print(lista_empelados)
