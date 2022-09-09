nombre_her = ""
edad = 0
sexo = ""
habilidad = ""
contador_magia_y_fuerza = 0
contador_heroes_fuerza = 0
acumulador_edad_heroes_fuerza = 0
edad_mas_joven = 0
contador_heroinas = 0
contador_heroinas_edad = 0
flag = 0
mayor_edad = 0
promedio_edad_heroes_fuerza = 0

while True:
    
    nombre_her = input("Ingrese nombre de Heroe | Heroina: ")
    
    while True:
        edad = int(input("Ingrese edad de Heroe | Heroina: "))
        if edad > 0:
            break
        
    while True:
        sexo = input("Ingrese el sexo(m, f, nb): ")
        if sexo == "m" or sexo == "f" or sexo == "nb":
            break
        
    while True:
        habilidad = input("Ingrese Habilidad(fuerza, magia, inteligencia): ")
        if (habilidad == "fuerza" or 
            habilidad == "magia" or 
            habilidad == "inteligencia"):
            break
        
    if habilidad == "fuerza":
        if flag == 0 or edad < edad_mas_joven:
            edad_mas_joven = edad
            her_mas_joven = nombre_her
            flag = 1

        if sexo == "m":
            contador_heroes_fuerza += 1
            acumulador_edad_heroes_fuerza += edad

    if (habilidad != "inteligencia") and sexo == "f":
        contador_magia_y_fuerza += 1
    
    if edad > mayor_edad:
        mayor_edad = edad
        sexo_mas_viejo = sexo
        nombre_viejo = nombre_her

    if sexo == "f":
        contador_heroinas += 1
        contador_heroinas_edad += edad
    
    respuesta = input("Quiere ingresar otro mas(s/n): ")
    if respuesta == "n":
        break
    
if contador_heroinas > 0:
    promedio_edad_heroinas = contador_heroinas_edad / contador_heroinas
if contador_heroes_fuerza > 0 :
    promedio_edad_heroes_fuerza = (acumulador_edad_heroes_fuerza
                                / contador_heroes_fuerza)

print("El nombre de Héroe | Heroína de 'fuerza' más joven es: ", 
    her_mas_joven, " con ", edad_mas_joven, " años" )
print("El sexo y nombre de Héroe | Heroína de mayor edad: ",
    sexo_mas_viejo, nombre_viejo, " con ", mayor_edad, " años")
print("La cantidad de Heroinas que tienen habilidades de fuerza",
    "o magia es: ", contador_magia_y_fuerza)
if promedio_edad_heroinas > 0:    
    print("El promedio de edad entre Heroinas es: ", promedio_edad_heroinas,
    " años")
if promedio_edad_heroes_fuerza > 0:
    print("El promedio de edad entre Heroes de fuerza es: ", 
    promedio_edad_heroes_fuerza)


