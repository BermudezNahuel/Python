import fun_poke


menu = '''
        1 - TOP N DE POKEMONES
        2 - ORDENAR PORKEMONES POR PODER
        3 - ORDENAR POKEMONES POR ID
        4 - PROMEDIO DE LAS HABILIDADES DE POKEMONES
        5 - BUSCAR POKEMONES POR TIPO
        6 - GUARDAR LISTA EN ARCHIVO.CSV
        7 - SALIR

        '''
lista_pokemones = fun_poke.leer_poke("C:/Users/Nahuel/Documents/TUP/P y L 1/programacion-y-laboratorio-1/Simulacro_pokemon/pokedex.json")

while True:
    respuesta = input("Ingrese numero de opcion: ")
    respuesta = fun_poke.validar_dato(respuesta, "[1-7]")

    if respuesta == "1":
        n_top = input("Ingrese un numero para el top: ")
        n_top = int(fun_poke.validar_dato(n_top,"[0-9]{1,2}"))
        lista_copia = lista_pokemones[:]
        n_top = fun_poke.validar_lista_len(lista_pokemones, n_top)
        lista_copia = lista_copia[:n_top]
        contenido = fun_poke.mostra_poke(lista_copia)
    elif respuesta == "2":
        respuesta = input("Ingrese un tipo de orden Ascendente(asc) o Descendente(desc)")
        orden = fun_poke.validar_dato(respuesta,"asc|desc")
        lista_copia = lista_pokemones[:]
        lista_ordenada = fun_poke.ordenar_poke(lista_copia, "poder", orden)
        contenido = fun_poke.mostra_poke(lista_ordenada,"poder")
    elif respuesta == "3":
        respuesta = input("Ingrese un tipo de orden Ascendente(asc) o Descendente(desc)")
        orden = fun_poke.validar_dato(respuesta,"asc|desc")
        lista_copia = lista_pokemones[:]
        lista_copia = fun_poke.ordenar_poke(lista_copia, "id", orden)
        contenido = fun_poke.mostra_poke(lista_copia,"id")
    elif respuesta == "4":
        key = input("Ingrese: 'tipo' | 'fortaleza' | 'debilidad' | 'evoluciones': ")
        key = fun_poke.validar_dato(key, "tipo|fortaleza|debilidad|evoluciones")
        orden = input("Ingrese tipo de orden 'menor' | 'mayor': ")
        orden = fun_poke.validar_dato(orden, "menor|mayor")
        lista_copia = lista_pokemones[:]
        lista_copia = fun_poke.buscar_promedio_menor_mayor(lista_copia, key, orden)
        contenido = fun_poke.mostra_poke(lista_copia,key)
    elif respuesta == "5":
        respuesta = input("Ingrese un tipo de pokemon: ")
        lista_copia = lista_pokemones[:]
        patron = fun_poke.listar_tipo_poke(lista_pokemones)
        respuesta = fun_poke.validar_dato(respuesta,patron)
        lista_encontrados = fun_poke.buscador_tipo(lista_copia,respuesta)
        fun_poke.mostra_poke(lista_encontrados,"tipo")
    elif respuesta == "6":
        fun_poke.guardar_archivo("C:/Users/Nahuel/Documents/TUP/P y L 1/programacion-y-laboratorio-1/Simulacro_pokemon/lista.csv",contenido)
    elif respuesta == "7":
        break