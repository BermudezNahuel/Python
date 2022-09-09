

''' version 1
while (respuesta != 1):
    respuesta = input("Numero")
    respuesta = int(respuesta)
    if(respuesta == 10):
        print("ES 10")
    elif(respuesta == 11):
        print("ES 11")
    else:
        print("no es 10")

    version 2
while (True):
    respuesta = input("Numero")
    respuesta = int(respuesta)
    if(respuesta == 1):
        break
    if(respuesta == 10):
        print("ES 10")
    elif(respuesta == 11):
        print("ES 11")
    else:
        print("no es 10")
    #version 3 - UN DO WHILE EN PYTHON

while (True):
    respuesta = input("Numero")
    respuesta = int(respuesta)
    
    if(respuesta == 10):
        print("ES 10")
    elif(respuesta == 11):
        print("ES 11")
    else:
        print("no es 10")
    
    if(respuesta == 1):
        break # de esta manera se parece mas a un do while, primero pega una vuelta y al final evalua 
              # la condicion

'''

# BUCLE 4

''' lista = [0,1,2,3,4,5,6] #puedo armar lista a mano
# iteracion, funcion con memoria que recuerda el anterior

#version 1
lista = range(20) # creo la lista con un range

for numero in lista: #Permite recorrer una lista de cualquier cosa: Ej mail. palabras, etc. No es necesario que los elements sean del mismo tipo
    print(numero)

#version 2
for numero in range(20):
    print(numero)
'''

#Lo mismo que el FOR pero sin el range
'''
numero = 0
while (numero < 20):
    print(numero)
    numero += 1
'''

'''
lista = [1,2,3,4,5] #Lista de numeros
lista[3] # posicion numero en la lista, en este caso es el numero 3
'''