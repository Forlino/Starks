from data_stark import lista_personajes
"""A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia"""


def imprimir_nombre_genero_NB(lista_heroes):
    '''
    Brief:
    Esta función imprime el nombre de los superhéroes con género no binario (NB) en la lista proporcionada.

    Parametros:
    lista_heroes (list): Lista que contiene los datos de los superhéroes.
    '''
    print("Superhéroes de género NB:")
    for superheroe in lista_heroes:
        if superheroe["genero"] == "NB":
            print(superheroe["nombre"])

def superheroe_mas_alto_genero(lista_heroes,genero):
    '''
    Brief:
    Esta función devuelve el superhéroe más alto de un género específico en la lista proporcionada.

    Parametros:
    lista_heroes (list): Lista que contiene los datos de los superhéroes.
    genero (str): Género para buscar el superhéroe más alto.

    Retorno:
    dict or None: Diccionario que representa al superhéroe más alto del género especificado o None si no se encuentra.
    '''
    altura_maxima = None
    superheroe_mas_alto = None

    for superheroe in lista_heroes:
        if superheroe["genero"] == genero:
            altura_actual = float(superheroe["altura"])
            if altura_maxima == None or altura_actual > altura_maxima:
                altura_maxima = altura_actual
                superheroe_mas_alto = superheroe

    return superheroe_mas_alto

def determinar_superheroe_mas_debil(lista_heroes,genero):
    '''
    Brief:
    Esta función determina el superhéroe más débil de un género específico en la lista proporcionada.

    Parametros:
    lista_heroes (list): Lista que contiene los datos de los superhéroes.
    genero (str): Género para buscar el superhéroe más débil.

    Retorno:
    dict or None: Diccionario que representa al superhéroe más débil del género especificado o None si no se encuentra.
    '''
    fuerza_minima = None
    superheroe_mas_debil = None

    for superheroe in lista_heroes:
        if superheroe["genero"] == genero:
            fuerza_actual = int(superheroe["fuerza"])
            if fuerza_minima == None or fuerza_actual < fuerza_minima:
                fuerza_minima = fuerza_actual
                superheroe_mas_debil = superheroe

    return superheroe_mas_debil

def fuerza_promedio_genero_NB(lista_heroes):
    '''
    Brief:
    Esta función calcula la fuerza promedio de los superhéroes con género no binario (NB) en la lista proporcionada.

    Parametros:
    lista_heroes (list): Lista que contiene los datos de los superhéroes.

    Retorno:
    float: Fuerza promedio de los superhéroes con género no binario o 0 si no hay superhéroes con ese género.
    '''
    suma_fuerza = 0
    cantidad = 0

    for superheroe in lista_heroes:
        if superheroe["genero"] == "NB":
            fuerza = int(superheroe["fuerza"])
            suma_fuerza += fuerza
            cantidad += 1

    if cantidad == 0:
        promedio = 0
    else:
        promedio = suma_fuerza / cantidad

    return promedio

def contiene(iterable, valor):
    '''
    Brief:
    Esta función verifica si un valor está presente en un iterable.

    Parametros:
    iterable (iterable): Iterable en el que se verificará la presencia del valor.
    valor: Valor que se verificará si está presente en el iterable.

    Retorno:
    bool: True si el valor está presente en el iterable, False en caso contrario.
    '''
    retorno = False
    for elemento in iterable:
        if elemento == valor:
            retorno = True
            break
    return retorno
def contar_por_atributo(lista_heroes,atributo):
    '''
    Brief:
    Esta función cuenta la cantidad de veces que aparece cada valor de un atributo en la lista de superhéroes.

    Parametros:
    lista_heroes (list): Lista que contiene los datos de los superhéroes.
    atributo (str): Atributo cuyos valores se contarán.

    Retorno:
    dict: Diccionario que contiene los valores del atributo y su respectivo conteo.
    '''
    conteo_atributos = {}
    for superheroe in lista_heroes:
        valor_atributo = superheroe[atributo]
        if contiene(conteo_atributos,valor_atributo):
            conteo_atributos[valor_atributo] += 1
        else:
            conteo_atributos[valor_atributo] = 1

    return conteo_atributos

def agrupar_por_atributo(lista_heroes,atributo):
    '''
    Brief:
    Esta función agrupa a los superhéroes en la lista según un atributo específico.

    Parametros:
    lista_heroes (list): Lista que contiene los datos de los superhéroes.
    atributo (str): Atributo por el cual se agruparán los superhéroes.

    Retorno:
    dict: Diccionario que contiene los superhéroes agrupados según el valor del atributo.
    '''
    agrupados = {}

    for superheroe in lista_heroes:
        valor_atributo = superheroe[atributo]
        if contiene(agrupados,valor_atributo):
            agrupados[valor_atributo].append(superheroe)
        else:
            agrupados[valor_atributo] = [superheroe]

    return agrupados

def mostrar_menu_informes():
    print("INFORMES:")
    print("A. Superhéroes de género NB")
    print("B. Superhéroe más alto de género F")
    print("C. Superhéroe más alto de género M")
    print("D. Superhéroe más débil de género M")
    print("E. Superhéroe más débil de género NB")
    print("F. Fuerza promedio de superhéroes de género NB")
    print("G. Cantidad de superhéroes por color de ojos")
    print("H. Cantidad de superhéroes por color de pelo")
    print("I. Superhéroes agrupados por color de ojos")
    print("J. Superhéroes agrupados por tipo de inteligencia")
    print("Q. Salir")

def main():
    while True:
        mostrar_menu_informes()
        opcion = input("Seleccione una opción (A/B/C/D/E/F/G/H/I/J/Q): ")

        if opcion == "A" or opcion == "a":
            imprimir_nombre_genero_NB(lista_personajes)
        elif opcion == "B" or opcion == "b":
            superheroe_alto_F = superheroe_mas_alto_genero(lista_personajes,"F")
            print("Superhéroe más alto de género F:")
            if superheroe_alto_F:
                print("Nombre:", superheroe_alto_F["nombre"])
                print("Altura:", superheroe_alto_F["altura"])
            else:
                print("No se encontró ningún superhéroe de género F.")
        elif opcion == "C" or opcion == "c":
            superheroe_alto_M = superheroe_mas_alto_genero(lista_personajes,"M")
            print("Superhéroe más alto de género M:")
            if superheroe_alto_M:
                print("Nombre:", superheroe_alto_M["nombre"])
                print("Altura:", superheroe_alto_M["altura"])
            else:
                print("No se encontró ningún superhéroe de género M.")
        elif opcion == "D" or opcion == "d":
            superheroe_debil_M = determinar_superheroe_mas_debil(lista_personajes,"M")
            print("Superhéroe más débil de género M:")
            if superheroe_debil_M:
                print("Nombre:", superheroe_debil_M["nombre"])
                print("Fuerza:", superheroe_debil_M["fuerza"])
            else:
                print("No se encontró ningún superhéroe de género M.")
        elif opcion == "E" or opcion == "e":
            superheroe_debil_NB = determinar_superheroe_mas_debil(lista_personajes,"NB")
            print("Superhéroe más débil de género NB:")
            if superheroe_debil_NB:
                print("Nombre:", superheroe_debil_NB["nombre"])
                print("Fuerza:", superheroe_debil_NB["fuerza"])
            else:
                print("No se encontró ningún superhéroe de género NB.")
        elif opcion == "F" or opcion == "f":
            fuerza_promedio_NB = fuerza_promedio_genero_NB(lista_personajes)
            print(f"Fuerza promedio de superhéroes de género NB: {fuerza_promedio_NB:.2f}")
        elif opcion == "G" or opcion == "g":
            conteo_color_ojos = contar_por_atributo(lista_personajes, "color_ojos")
            print("Cantidad de superhéroes por color de ojos:")
            for color_ojos, cantidad in conteo_color_ojos.items():
                print(f"{color_ojos}: {cantidad}")
        elif opcion == "H" or opcion == "h":
            conteo_color_pelo = contar_por_atributo(lista_personajes, "color_pelo")
            print("Cantidad de superhéroes por color de pelo:")
            for color_pelo, cantidad in conteo_color_pelo.items():
                print(f"{color_pelo}: {cantidad}")
        elif opcion == "I" or opcion == "i":
            superheroes_agrupados_color_ojos = agrupar_por_atributo(lista_personajes, "color_ojos")
            print("Superhéroes agrupados por color de ojos:")
            for color_ojos, superheroes in superheroes_agrupados_color_ojos.items():
                print(f"\nColor de ojos: {color_ojos}")
                for superheroe in superheroes:
                    print(f"  Nombre: {superheroe['nombre']}")
        elif opcion == "J" or opcion == "j":
            superheroes_agrupados_inteligencia = agrupar_por_atributo(lista_personajes, "inteligencia")
            print("Superhéroes agrupados por tipo de inteligencia:")
            for inteligencia, superheroes in superheroes_agrupados_inteligencia.items():
                print(f"\nTipo de inteligencia: {inteligencia}")
                for superheroe in superheroes:
                    print(f"  Nombre: {superheroe['nombre']}")
        elif opcion == "Q" or opcion == "q":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()