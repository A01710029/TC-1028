"""
El programa genera un número aleatorio basado en un 
parametro del usuario y compara sus adivinanzas
hasta que lo adivina correctamente. 
Permite que se lleven a cabo varias rondas hasta que, 
finalmente, el usuario decide terminar el juego 
y regresa las mejor ronda.
"""

#bibliotecas 
import math 
import random 
import time 

"""
==== variables del juego (no cambian cada ronda) ==== 
"""

#matriz para guardar valores de cada ronda 
matriz_rondas = [] 

#contador de rondas 
rondas = 1 

#empieza ciclo del juego 
while True: 
    
    """
    ==== variables del juego (cambian cada ronda) ==== 
    """

    nombre = str(input("¿Cómo te llamas? \n")) 
    adivinanza = int() 
    intentos = 1 
    lista_intentos = [] 
    lista_ronda = [] 

    #declara parametro para número aleatorio 
    print("¿Cuál debería ser el número tope?") 
    tope = int(input()) 

    """
    verifica que el número tope no sea negativo o menor a 2 
    cuando se recibe un parametro aceptable, se genera el 
    número aleatorio (num_compu) 
    """
    while(tope <= 1): 
            print("El número tiene que ser mayor que uno.") 
            print("¿Cuál debería ser el número tope?") 
            tope = int(input()) 
    num_compu = random.randint(1,tope) 
        
    """
    ==== funciones del juego ==== 
    """

    def comienzo(nombre, tope): 
        """
        recibe: nombre valor string, tope valor numérico 
        agrega valores a la lista de la ronda actual 
        imprime texto para introducir la ronda 
        """
        lista_ronda.append(nombre) 
        lista_ronda.append(tope) 
        print("¡Hola", nombre + "!") 
        print("""¡Intenta adivinar en qué número 
entre 1 y""", str(tope) + """ estoy pensando!""") 
        print("Escribe '0' si quieres ver tus intentos anteriores.") 

    def adivina_compara(adivinanza, intentos):
        """
        recibe: adivinanza valor numérico, intentos valor numérico 
        compara adivinanza al número aleatorio, da pistas al usuario 
        basado en si es mayor o menor el valor, y agrega 
        adivinanzas a la lista de la ronda 
        también agrega al valor de intentos cada vez que se 
        compara una adivinanza (contador del ciclo) 
        y permite activar función para imprimir intentos anteriores 
        devuelve: cantidad de intentos (valor entero del contador) 
        """
        while (adivinanza != num_compu): 
            adivinanza = int(input()) 
            if adivinanza == 0: 
                intentos = intentos - 1
            if adivinanza < num_compu: 
                intentos = intentos + 1 
                lista_intentos.append(adivinanza) 
                print("Intenta un número más grande") 
            elif adivinanza > num_compu: 
                intentos = intentos + 1 
                lista_intentos.append(adivinanza) 
                print("Intenta un número más pequeño") 
        print("¡Adivinaste el número,", nombre + "!") 
        lista_ronda.append(intentos) 
        return "¿Cuántos intentos tomó?: " + str(intentos) 

    def imprimir_lista():
        """
        función auxiliar para imprimir 
        muestra en pantalla los intentos previos (fallados) 
        en forma de lista 
        """
        i = 0 
        len_intentos = len(lista_intentos) 
        while(i < len_intentos-1): 
            if(lista_intentos[i] == 0): 
                lista_intentos.remove(0) 
            i = i + 1 
        print(lista_intentos) 

    def mejor_adivinanza(matriz):
        """
        recibe: matriz (valores de todas las rondas) 
        divide cada adivinanza por el valor tope y compara 
        los promedios de todas las rondas para identificar el valor menor 
        si hay un empate, nombre la última ronda con el valor menor
        devuelve: el nombre de la ronda con el menor promedio 
        """
        menor_val = matriz[0][2]/matriz[0][1]
        menor_nom = ""
        i = 0
        while i < len(matriz):
            j = 0
            while j < len(matriz[0]):
                if(matriz[i][2]/matriz[i][1] < menor_val):
                    menor_val = matriz[i][2]
                    menor_nom = matriz[i][0]
                else:
                    menor_nom = matriz[0][0]
                j = j + 1
            i = i + 1
        return menor_nom 
    
    def mejor_tiempo(matriz):
        """
        recibe: matriz (valores de todas las rondas) 
        compara los valores de tiempo de todas las rondas 
        para identificar el valor menor 
        devuelve: el nombre de la ronda con el menor tiempo 
        """
        menor_val = matriz[0][3]
        menor_nom = ""
        i = 0
        while i < len(matriz):
            j = 0
            while j < len(matriz[0]):
                if(matriz[i][3] < menor_val):
                    menor_val = matriz[i][2]
                    menor_nom = matriz[i][0]
                else:
                    menor_nom = matriz[0][0]
                j = j + 1
            i = i + 1
        return menor_nom

    def stats_rondas(matriz):
        """
        recibe: matriz (valores de todas las rondas) 
        llama las funciones que comparan los valores entre rondas
        para encontrar las mejores rondas
        devuelve: los nombres de las mejores rondas, ordenadas
        """
        print(matriz_rondas)
        mejor_a = mejor_adivinanza(matriz) 
        mejor_t = mejor_tiempo(matriz)
        return "La ronda con el mejor promedio de adivinanzas fue: " + mejor_a \
            + "\nLa ronda con el mejor tiempo fue: " + mejor_t

    def nombre_replace(nombre, rep):
        """"
        recibe: nombre valor string y rep valor string
        remplaza el nombre de la ronda actual con una versión
        del mismo nombre que incluye el número de ronda
        para poder diferenciar las rondas de un mismo usuario
        """
        i = 1
        while i < len(matriz_rondas):
            j = 0
            while j < len(matriz_rondas[0]):
                if(matriz_rondas[i][j] == nombre):
                    matriz_rondas[i][j] = rep
                j = j + 1
            i = i + 1

    """
    ==== parte principal del programa ====
    """
    comienzo(nombre, tope)
    tiempo_inicial = time.time()
    print(adivina_compara(adivinanza, intentos))
    tiempo_final = time.time()
    tiempo_total = round(tiempo_final - tiempo_inicial, 2)
    lista_ronda.append(tiempo_total)
    matriz_rondas.append(lista_ronda)
    print("¿Cuánto tiempo tomó?:", tiempo_total, "secs")
   
    """
    verifica si el nombre de la ronda actual se ha repetido
    si es verdad, llama la función para agregarle
    número de ronda al nombre (para diferenciarlos)
    """
    if(rondas > 1): 
        nombre_repeat = nombre + str(rondas)
        nombre_replace(nombre, nombre_repeat)

    #agrega al contador de rondas 
    rondas = rondas + 1

    """
    activa más rondas (repite el ciclo)
    o termina el juego (termina el ciclo) e imprime resultados finales
    """
    check = input("¿Quieres jugar de nuevo? Escribe y o n \n")
    if(check == "y"):
        continue
    else:
        if rondas > 2:
            print(stats_rondas(matriz_rondas))
    break