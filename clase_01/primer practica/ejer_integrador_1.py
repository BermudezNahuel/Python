peso = 0
precio_por_kilo = 0
tipo_validad = ""
acumulador_subtotal = 0
acumulador_kilos = 0
alimento_mas_caro = ""
precio_alimento_mas_caro = 0



while True:
    
    while True:
        peso = int(input("Ingrese peso del producto: "))
        if (peso > 9 and peso < 101):
            break

    while True:
        precio_por_kilo = int(input("Ingrese precio por kilo: "))
        if precio_por_kilo > 0:
            break

    while True:
        tipo_validad = input("Ingrese tipo (a, v, m): ")
        if (tipo_validad == "a" 
            or tipo_validad == "v" 
            or tipo_validad == "m"):
            break

    subtotal = peso * precio_por_kilo
    acumulador_subtotal += subtotal
    acumulador_kilos += peso
   
    
    if precio_por_kilo > precio_alimento_mas_caro:
        precio_alimento_mas_caro = precio_por_kilo
        alimento_mas_caro = tipo_validad

    respuesta = input("Quiere ingresar otro producto (s/n)")
    if  respuesta == "n":
        break



if acumulador_kilos > 300:
    descuento = 0.75
elif acumulador_kilos > 100:
    descuento = 0.85
else:
    descuento = 1
    
total_con_descuento = acumulador_subtotal * descuento
precio_promedio = acumulador_subtotal / acumulador_kilos


print("El importe total a pagar: ", acumulador_subtotal)
if acumulador_kilos > 100:
    print("Total con descuento: ", total_con_descuento)    
print("Tipo de alimento mas caro: ", alimento_mas_caro)
print("Precio promedio por kilo: ", precio_promedio)



 




