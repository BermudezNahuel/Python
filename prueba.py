lista = ["emmett","Marty","Biff"]


def buscar_min_max(lista: list[dict], key:str, tipo:str) -> int:
    '''
    Se encargar de buscar cual es el heroe que posee el minimo o maximo valor de una determina
    clave. Luego retorna el indice del lugar que ocupa ese heroe dentro de la lista.
    -lista: ingresar lista de heroes
    -key: ingresar clave a comparar
    -tipo: ingresar el tipo de valor que desea encontrar ascendente o descendente
    '''
    min_max = 0
    if lista:
        for i in range(len(lista)):
            if ((tipo == "asc" and lista[i][key] < lista[min_max][key]) 
                or (tipo == "desc" and lista[i][key] > lista[min_max][key])):
                min_max = i
    return min_max

for i in range(len(lista) - 1):
    min_index = busca_minimo(lista[i:]) + i
    lista[i], lista[min_index] = lista[min_index], lista[i]
print(lista)