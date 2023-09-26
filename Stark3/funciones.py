
def stark_normalizar_datos(lista_de_heroes):
    '''
    Brief:
    Esta función normaliza los datos de altura, peso y fuerza en la lista de superhéroes si no están en el formato correcto.

    Parametros:
    lista_de_heroes (list): Lista que contiene los datos de los superhéroes.

    Retorno:
    bool: True si se realizaron cambios, False si no se realizaron cambios.
    '''
    flag_cambios = False
    for heroe in lista_de_heroes:
        if type(heroe["altura"]) != float:
            heroe["altura"] = float(heroe["altura"]) 
            flag_cambios = True

        if type(heroe["peso"]) != float:
            heroe["peso"] = float(heroe["peso"])
            flag_cambios = True
        
        if type(heroe["fuerza"]) != int:
            heroe["fuerza"] = int(heroe["fuerza"])
            flag_cambios = True

        
    return flag_cambios

def obtener_dato(heroe, clave_a_buscar):
    '''
    Brief:
    Esta función obtiene un dato específico de un superhéroe basado en una clave a buscar.

    Parametros:
    heroe (dict): Diccionario que contiene los datos de un superhéroe.
    clave_a_buscar (str): Clave cuyo valor se quiere obtener.

    Retorno:
    any: El valor correspondiente a la clave especificada o False si la clave no existe en el diccionario.
    '''
    dato = False
    for clave in heroe: #Si esta vacio el diccionario no entra al for por lo tanto es falso
        if clave == "nombre":
            dato = heroe[clave_a_buscar]
            break
    
    return dato

def obtener_nombre(heroe):
    '''
    Brief:
    Esta función obtiene el nombre de un superhéroe en un formato específico.

    Parametros:
    heroe (dict): Diccionario que contiene los datos de un superhéroe.

    Retorno:
    str or bool: El nombre del superhéroe formateado o False si no se pudo obtener el nombre.
    '''
    nombre_formateado = False
    nombre = obtener_dato(heroe, "nombre")
    if nombre != False:
        nombre_formateado = f"Nombre: {nombre}"
    
    return nombre_formateado

def obtener_nombre_y_dato(heroe, clave_a_buscar):
    '''
    Brief:
    Esta función obtiene el nombre del superhéroe y un dato específico en un formato específico.

    Parametros:
    heroe (dict): Diccionario que contiene los datos de un superhéroe.
    clave_a_buscar (str): Clave cuyo valor se quiere obtener.

    Retorno:
    str or bool: El nombre del superhéroe y el dato especificado formateados o False si no se pudo obtener alguno de los datos.
    '''
    nombre_y_dato = False
    nombre_formateado = obtener_nombre(heroe)
    dato = obtener_dato()
    if nombre_formateado != False and dato != False:
        nombre_y_dato = f"{nombre_formateado} | {clave_a_buscar}: {dato}"
    
    return nombre_y_dato

def obtener_maximo(lista_de_heroes, clave):
    '''
    Brief:
    Esta función obtiene el valor máximo de una clave específica entre los superhéroes en la lista.

    Parametros:
    lista_de_heroes (list): Lista que contiene los datos de los superhéroes.
    clave (str): Clave cuyo valor máximo se quiere obtener.

    Retorno:
    any or bool: El valor máximo de la clave especificada o False si no se pudo obtener el valor máximo.
    '''
    maximo = False
    for heroe in lista_de_heroes:
        dato = obtener_dato(heroe, clave)
        if type(dato) != int and type(dato) != float:
            maximo = False
            break
        if maximo == False or dato > maximo:
            maximo = dato
    return maximo

def obtener_minimo(lista_de_heroes, clave):
    '''
    Brief:
    Esta función obtiene el valor mínimo de una clave específica entre los superhéroes en la lista.

    Parametros:
    lista_de_heroes (list): Lista que contiene los datos de los superhéroes.
    clave (str): Clave cuyo valor mínimo se quiere obtener.

    Retorno:
    any or bool: El valor mínimo de la clave especificada o False si no se pudo obtener el valor mínimo.
    '''
    minimo = False
    for heroe in lista_de_heroes:
        dato = obtener_dato(heroe, clave)
        if type(dato) != int and type(dato) != float:
            minimo = False
            break
        if minimo == False or dato < minimo:
            minimo = dato
    return minimo

def obtener_dato_cantidad(lista_de_heroes, dato_a_buscar, clave):
    '''
    Brief:
    Esta función obtiene una sublista de superhéroes que tienen un dato específico en una clave dada.

    Parametros:
    lista_de_heroes (list): Lista que contiene los datos de los superhéroes.
    dato_a_buscar: Dato específico que se busca en la clave.
    clave (str): Clave en la que se buscará el dato.

    Retorno:
    list: Sublista de superhéroes que tienen el dato especificado en la clave.
    '''
    sublista_heroes = []
    for heroe in lista_de_heroes:
        dato = obtener_dato(heroe, clave)
        if dato_a_buscar == dato:
            sublista_heroes.append(heroe)
    return sublista_heroes

def stark_imprimir_heroes(lista_de_heroes):
    retorno = False
    for heroe in lista_de_heroes:
        nombre_heroe = obtener_nombre(heroe)
        if nombre_heroe != False:
            print(nombre_heroe)
            retorno = True

    return retorno


def sumar_dato_heroe(lista_de_heroes, clave):
    '''
    Brief:
    Esta función imprime los nombres de los superhéroes en la lista.

    Parametros:
    lista_de_heroes (list): Lista que contiene los datos de los superhéroes.

    Retorno:
    bool: True si se imprimió al menos un nombre, False si no se imprimió ningún nombre.
    '''
    acumulador_dato = False
    for heroe in lista_de_heroes:
        if type(heroe) == dict:
            dato = obtener_dato(heroe, clave)
            if dato != False:
                if acumulador_dato == False:
                    acumulador_dato = dato
                else:
                    acumulador_dato += dato
    return acumulador_dato

def dividir(dividendo, divisor):
    '''
    Brief:
    Esta función realiza una división entre el dividendo y el divisor, si es posible.

    Parametros:
    dividendo: El número que se va a dividir.
    divisor: El número por el cual se va a dividir el dividendo.

    Retorno:
    float or bool: El resultado de la división si el divisor es diferente de cero, False si el divisor es cero.
    '''
    division = False
    if divisor != 0:
        division = dividendo / divisor
    return division

def calcular_promedio(lista_de_heroes, clave):
    '''
    Brief:
    Esta función calcula el promedio de un dato específico entre los superhéroes en la lista.

    Parametros:
    lista_de_heroes (list): Lista que contiene los datos de los superhéroes.
    clave (str): Clave cuyo valor se utilizará para calcular el promedio.

    Retorno:
    float or bool: El promedio del dato especificado o False si no se pudo calcular el promedio.
    '''
    promedio = False
    suma_datos = sumar_dato_heroe(lista_de_heroes, clave)
    cantidad_heroes = len(lista_de_heroes)
    if type(suma_datos) == float or type(suma_datos) == int:
        promedio = dividir(suma_datos, cantidad_heroes)
    return promedio

def mostrar_promedio_dato(lista_de_heroes, clave):
    '''
    Brief:
    Esta función calcula y muestra el promedio de un dato específico entre los superhéroes en la lista.

    Parametros:
    lista_de_heroes (list): Lista que contiene los datos de los superhéroes.
    clave (str): Clave cuyo valor se utilizará para calcular el promedio y mostrarlo.

    Retorno:
    bool: True si se mostró el promedio, False si no se pudo mostrar.
    '''
    retorno = False
    promedio = calcular_promedio(lista_de_heroes, clave)
    if promedio != False:
        print(f"El promedio de {clave} es: {promedio}")
        retorno = True
    return retorno

def imprimir_menu():
    mensaje  = "1  - A. Normalizar datos (No se debe poder acceder a los otros puntos)\n"
    mensaje += "2  - B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n"
    mensaje += "3  - C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n"
    mensaje += "4  - D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n"
    mensaje += "5  - E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n"
    mensaje += "6  - F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n"
    mensaje += "7  - G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n"
    mensaje += "8  - H. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
    mensaje += "9  - I. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n"
    mensaje += "10 - J. Listar todos los superhéroes agrupados por color de ojos.\n"
    mensaje += "11 - K. Listar todos los superhéroes agrupados por tipo de inteligencia\n"
    mensaje += "12 - Salir\n"
    print(mensaje)

def contiene(lista, valor):
    '''
    Brief:
    Esta función verifica si un valor está presente en una lista.

    Parametros:
    lista (iterable): La lista o iterable en la que se va a buscar el valor.
    valor: El valor que se desea verificar si está presente en la lista.

    Retorno:
    bool: True si el valor está presente en la lista, False si no está presente.
    '''
    flag_contiene = False
    for elemento in lista:
        if elemento == valor:
            flag_contiene = True
            break
    return flag_contiene

def validar_entero(numero_str):
    '''
    Brief:
    Esta función verifica si una cadena representa un número entero.

    Parametros:
    numero_str (str): La cadena que se desea verificar si representa un número entero.

    Retorno:
    bool: True si la cadena representa un número entero, False si no representa un número entero.
    '''
    flag_es_entero = False
    digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for caracter in numero_str:
        if contiene(digitos, caracter):
            flag_es_entero = True
        else:
            flag_es_entero = False
            break

    return flag_es_entero

def crear_sublista(lista, clave):
    '''
    Brief:
    Esta función crea una sublista de valores únicos de una clave específica de los elementos de la lista.

    Parametros:
    lista (iterable): La lista de elementos de donde se extraerán los valores.
    clave (str): La clave cuyos valores se utilizarán para crear la sublista.

    Retorno:
    list: Sublista de valores únicos de la clave especificada.
    '''
    sublista = []
    for elemento in lista:
        if not contiene(sublista, elemento[clave]):
            sublista.append(elemento[clave])
    return sublista

def stark_menu_principal():
    '''
    Brief:
    Esta función muestra el menú principal y permite al usuario elegir una opción válida.

    Retorno:
    int or bool: La opción elegida por el usuario como un entero si es válida, False si no es válida.
    '''
    opcion_elegida = False
    opciones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    imprimir_menu()
    opcion_elegida_str = input("Elija una opcion: ")
    if validar_entero(opcion_elegida_str):
        opcion_casteada = int(opcion_elegida_str)
        if contiene(opciones, opcion_casteada):
            opcion_elegida = opcion_casteada
    return opcion_elegida

def stark_marvel_app(lista_de_heroes):
    '''
    Brief:
    Esta función representa la aplicación principal de la Marvel Stark Database.

    Parametros:
    lista_de_heroes (list): Lista que contiene los datos de los superhéroes.
    ''' 
    flag_datos_normalizados = False
    while True:
        print("=" * 50)
        opcion_elegida = stark_menu_principal()

        if opcion_elegida == 1:
            if stark_normalizar_datos(lista_de_heroes) == True:
                flag_datos_normalizados = True
                mensaje = "Datos Normalizados"
            else:
                mensaje =  "Hubo un error al normalizar los datos. Verifique que la" 
                mensaje += " lista no este vacía o que los datos ya no se hayan normalizado anteriormente"
            print(mensaje)
        elif flag_datos_normalizados:
            match opcion_elegida:
                case 2:
                    lista_NB = obtener_dato_cantidad(lista_de_heroes, "NB", "genero")
                    print("Heroes de genero NB:")
                    if stark_imprimir_heroes(lista_NB) == False:
                        print("No hay ningun heroe de genero NB")
                case 3:
                    lista_F = obtener_dato_cantidad(lista_de_heroes, "F", "genero")
                    maximo_altura_F = obtener_maximo(lista_F, "altura")
                    lista_maximo_altura_F = obtener_dato_cantidad(lista_F, maximo_altura_F, "altura")
                    print("Heroes de genero F de mayor altura:")
                    if stark_imprimir_heroes(lista_maximo_altura_F) == False:
                        print("No hay ningun heroe de genero F")
                case 4:
                    lista_M = obtener_dato_cantidad(lista_de_heroes, "M", "genero")
                    maximo_altura_M = obtener_maximo(lista_M, "altura")
                    lista_maximo_altura_M = obtener_dato_cantidad(lista_M, maximo_altura_M, "altura")
                    print("Heroes de genero M de mayor altura:")
                    if stark_imprimir_heroes(lista_maximo_altura_M) == False:
                        print("No hay ningun heroe de genero M")
                case 5:
                    lista_M = obtener_dato_cantidad(lista_de_heroes, "M", "genero")
                    minimo_fuerza_M = obtener_minimo(lista_M, "fuerza")
                    lista_minimo_fuerza_M = obtener_dato_cantidad(lista_M, minimo_fuerza_M, "fuerza")
                    print("Heroes de genero M mas debiles:")
                    if stark_imprimir_heroes(lista_minimo_fuerza_M) == False:
                        print("No hay ningun heroe de genero M")
                case 6:
                    lista_NB = obtener_dato_cantidad(lista_de_heroes, "NB", "genero")
                    maximo_fuerza_NB = obtener_minimo(lista_NB, "fuerza")
                    lista_maximo_fuerza_NB = obtener_dato_cantidad(lista_NB, maximo_fuerza_NB, "fuerza")
                    print("Heroes de genero NB mas debiles:")
                    if stark_imprimir_heroes(lista_maximo_fuerza_NB) == False:
                        print("No hay ningun heroe de genero NB")
                case 7:
                    lista_NB = obtener_dato_cantidad(lista_de_heroes, "NB", "genero")
                    promedio_fuerza_NB = calcular_promedio(lista_NB, "fuerza")
                    if promedio_fuerza_NB != False:
                        mensaje = f"El promedio de fuerza NB es: {promedio_fuerza_NB:.2f}"
                    else:
                        mensaje = "No hay personajes NB"
                    print(mensaje)
                case 8:
                    tipos_de_ojos = crear_sublista(lista_de_heroes, "color_ojos")
                    print("Cantidad de heroes por tipo de color de ojos")
                    for tipo in tipos_de_ojos:
                        sublista_tipo = obtener_dato_cantidad(lista_de_heroes, tipo, "color_ojos")
                        cantidad_tipo = len(sublista_tipo)
                        print(f"{tipo}: {cantidad_tipo}")
                case 9:
                    tipos_de_pelo = crear_sublista(lista_de_heroes, "color_pelo")
                    print("Cantidad de heroes por tipo de color de pelo")
                    for tipo in tipos_de_pelo:
                        sublista_tipo = obtener_dato_cantidad(lista_de_heroes, tipo, "color_pelo")
                        cantidad_tipo = len(sublista_tipo)
                        print(f"{tipo}: {cantidad_tipo}")

                case 10:
                    tipos_color_ojos = crear_sublista(lista_de_heroes, "color_ojos")
                    print("Lista de heroes por tipo de color de ojos:")
                    for tipo in tipos_color_ojos:
                        sublista_tipo = obtener_dato_cantidad(lista_de_heroes, tipo, "color_ojos")
                        print(f"{tipo}:")
                        stark_imprimir_heroes(sublista_tipo)
                        print('  -----  ')
                
                case 11:
                    tipos_inteligencia = crear_sublista(lista_de_heroes, "inteligencia")
                    print("Lista de heroes por tipo de inteligencia:")
                    for tipo in tipos_inteligencia:
                        sublista_tipo = obtener_dato_cantidad(lista_de_heroes, tipo, "inteligencia")
                        print(f"{tipo}:")
                        stark_imprimir_heroes(sublista_tipo)
                        print('  -----  ')
                    
                case 12:
                    break
                case _:
                    print("Ingrese una opcion correcta")
        else:
            print("Debes normalizar los datos antes de continuar")
        
    print("¡Hasta pronto, Iron Man!")
