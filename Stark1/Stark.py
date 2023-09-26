from data_stark import lista_personajes
"""A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino"""

def mostrar_datos_superheroe(superheroe):
    '''
    Brief:
    Esta función imprime los datos de un superhéroe.

    Parametros:
    superheroe (dict): Un diccionario que contiene los datos del superhéroe, con claves como nombre, poderes, etc.

    Returns:
    None. Imprime los datos del superhéroe en la consola.
    '''
    for clave, valor in superheroe.items():
        print(f"{clave}: {valor}")

def mostrar_datos_lista_heroes(lista_heroes):
    '''
    Muestra los datos de la lista de héroes proporcionada.

    Parametros:
    lista_heroes (list): La lista de héroes a mostrar.

    '''
    print("Opción A: Recorrer la lista e imprimir todos los datos de cada superhéroe\n")
    for superheroe in lista_heroes:
        mostrar_datos_superheroe(superheroe)
        print()

def mostrar_heroe_mayor_fuerza(lista_heroes):
    '''
    Muestra la identidad y el peso del superhéroe con mayor fuerza en la lista proporcionada.

    Parametros:
    lista_heroes (list): La lista de superhéroes para buscar la mayor fuerza.

    '''
    print("Opción B: Mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)\n")
    fuerza_maxima = 0
    superheroe_max_fuerza = None
    for superheroe in lista_heroes:
        fuerza = int(superheroe["fuerza"])
        if fuerza > fuerza_maxima:
            fuerza_maxima = fuerza
            superheroe_max_fuerza = superheroe

    if superheroe_max_fuerza:
        print("Identidad:", superheroe_max_fuerza["identidad"])
        print("Peso:", superheroe_max_fuerza["peso"])
    else:
        print("No se encontró ningún superhéroe con información de fuerza.")

def mostrar_heroe_mas_bajo(lista_heroes):
    '''
    Muestra el nombre e identidad del superhéroe más bajo en la lista proporcionada.

    Parametros:
    lista_heroes (list): La lista de superhéroes para buscar el más bajo.

    '''
    print("Opción C: Mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)\n")
    altura_minima = None

    for superheroe in lista_heroes:
        altura_actual = float(superheroe["altura"])
        if altura_minima == None or altura_actual < altura_minima:
            altura_minima = altura_actual
    if altura_minima != None:
        print("superheroes de menor altura:")
        for superheroe in lista_heroes:
            altura_actual = float(superheroe["altura"])
            nombre_actual = superheroe ["nombre"]
            identidad_actual = superheroe["identidad"]
            if altura_actual == altura_minima:
                print(f"nombre: {nombre_actual}, identidad: {identidad_actual}")
    else:
        print("No se encontro ningun superheroe")

    
            

def mostrar_promedio_peso_masculino(lista_heroes):
    '''
    Determina el peso promedio de los superhéroes masculinos en la lista proporcionada.

    Parametros:
    lista_heroes (list): La lista de superhéroes para calcular el peso promedio de los masculinos.

    '''
    print("Opción D: Determinar el peso promedio de los superhéroes masculinos (PROMEDIO)\n")
    suma_pesos_masculinos = 0
    cantidad_masculinos = 0

    for superheroe in lista_heroes:
        if superheroe["genero"] == "M":
            peso_masculino = float(superheroe["peso"])
            suma_pesos_masculinos += peso_masculino
            cantidad_masculinos += 1

    if cantidad_masculinos > 0:
        peso_promedio_masculinos = suma_pesos_masculinos / cantidad_masculinos
        print(f"Peso promedio de superhéroes masculinos: {peso_promedio_masculinos:.2f}")
    else:
        print("No se encontraron superhéroes masculinos.")

def mostrar_promedio_superior_a_femeninas(lista_heroes):
    '''
    Muestra el nombre y peso de los superhéroes cuya fuerza supera la fuerza promedio de las superhéroes femeninas en la lista proporcionada.

    Parametros:

    lista_heroes (list): La lista de superhéroes para comparar con la fuerza promedio de las femeninas.
    '''
    print("Opción E: Mostrar nombre y peso de los superhéroes cuya fuerza supere la fuerza promedio de las superhéroes femeninas\n")
    fuerza_promedio_femenina = 0
    cantidad_femeninos = 0

    for superheroe in lista_heroes:
        if superheroe["genero"] == "F":
            fuerza_femenina = int(superheroe["fuerza"])
            fuerza_promedio_femenina += fuerza_femenina
            cantidad_femeninos += 1

    if cantidad_femeninos > 0:
        fuerza_promedio_femenina /= cantidad_femeninos

        for superheroe in lista_personajes:
            fuerza_superheroe = int(superheroe["fuerza"])
            if fuerza_superheroe > fuerza_promedio_femenina:
                print("Nombre:", superheroe["nombre"])
                print("Peso:", superheroe["peso"])
                print()

    else:
        print("No se encontraron superhéroes femeninos.")

def mostrar_menu():
    '''
    Muestra el menú de opciones para interactuar con la lista de superhéroes.
    '''
    print("MENU:")
    print("A. Recorrer la lista e imprimir todos los datos de cada superhéroe")
    print("B. Mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)")
    print("C. Mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)")
    print("D. Determinar el peso promedio de los superhéroes masculinos (PROMEDIO)")
    print("E. Mostrar nombre y peso de los superhéroes cuya fuerza supere la fuerza promedio de las superhéroes femeninas")
    print("Q. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (A/B/C/D/E/Q): ")

        if opcion == "A" or opcion == "a":
            mostrar_datos_lista_heroes()
        elif opcion == "B" or opcion == "b":
            mostrar_heroe_mayor_fuerza()
        elif opcion == "C" or opcion == "c":
            mostrar_heroe_mas_bajo()
        elif opcion == "D" or opcion == "d":
            mostrar_promedio_peso_masculino()
        elif opcion == "E" or opcion == "e":
            mostrar_promedio_superior_a_femeninas()
        elif opcion == "Q" or opcion == "q":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()