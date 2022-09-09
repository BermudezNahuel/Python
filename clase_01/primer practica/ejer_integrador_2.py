    
tipo_producto = ""
precio = 0
cantidad = 0
marca = ""
fabricante = ""
marca_barbijo_caro = ""
cantidad_barbijo_caro = 0
fabricante_barbijo_caro = ""
precio_barbijo_caro = 0
item_mas_unidades = 0
fabricante_mas_unidades = ""
cantidad_jabones = 0

for iteracion in range(5):

    tipo_producto = input("ingrese tipo de producto: jabon, barbijo o alcohol")
    while tipo_producto != 'barbijo' and tipo_producto != 'jabon' and tipo_producto != 'alcohol':
        tipo_producto = input("ingrese tipo de producto: jabon, barbijo o alcohol")
        
    
    while True:
        precio = int(input("ingrese precio: $"))
        if precio >=100 and precio <=300:
            break

    while True:
        cantidad = int(input("ingrese cantidad"))
        if cantidad >0 and cantidad <1001:
            break
    marca = input("Ingrese marca")
    fabricante = input("ingrese fabricante")

    if (tipo_producto == "barbijo"):
        if precio > precio_barbijo_caro:
            precio_barbijo_caro = precio
            cantidad_barbijo_caro = cantidad
            fabricante_barbijo_caro = fabricante
    elif tipo_producto == "jabon":
        cantidad_jabones += cantidad
    
         
    if cantidad > item_mas_unidades:
            item_mas_unidades = cantidad
            fabricante_mas_unidades = fabricante


print("Barbijo mas caro: ", cantidad_barbijo_caro," y lo fabrica: ", fabricante_barbijo_caro)
print("El item con mas unidades lo fabrica: ", fabricante_mas_unidades)
print("Cantidad total de jabones: ", cantidad_jabones)
