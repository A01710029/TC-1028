#Estoy escribiendo los comentarios en inglés. Hablé con el 
#profesor sobre esta decisión.

#import math, random, and time
import math
import random
import time

#create matrix to store each round values
#(name, top number, attempts, and total time)
matriz_rondas = []

#starts counter for multiple-round name readjustment
c = 1
while True: 
    #declare variables
    nombre = str(input("¿Cómo te llamas? \n"))
    adivinanza = int()
    intentos = 1
    lista_intentos = []
    lista_ronda = []

    #ask user for + set top number 
    print("¿Cuál debería ser el número tope?")
    tope = int(input())

    #check that top number is not negative or smaller than 2
    #once ok, generate random number
    while(tope <= 1):
            print("El número tiene que ser mayor que uno.")
            print("¿Cuál debería ser el número tope?")
            tope = int(input())
    num_compu = random.randint(1,tope)
        
    #function to display game start text
    def comienzo(nombre, tope):
        lista_ronda.append(nombre)
        lista_ronda.append(tope)
        print("Hola", nombre)
        print("""¡Intenta adivinar en qué número 
entre 1 y""", str(tope) + """ estoy pensando!""")
        print("Escribe '0' si quieres ver tus intentos anteriores")

    #function to prompt, analyze, give feedback on, 
    #and keep count of guesses
    #also adds failed guesses to list
    def adivina_compara(adivinanza, intentos):
        while (adivinanza != num_compu):
            adivinanza = int(input())
            if adivinanza == 0:
                intentos = intentos - 1 #removes calls to list from counter
                imprimir_lista()
            if adivinanza < num_compu: #guess is less than target num
                intentos = intentos + 1
                lista_intentos.append(adivinanza)
                print("Intenta un número más grande")
            elif adivinanza > num_compu: #guess is more than target num
                intentos = intentos + 1
                lista_intentos.append(adivinanza)
                print("Intenta un número más pequeño")
        print("¡Adivinaste el número,", nombre + "!")
        lista_ronda.append(intentos)
        return "¿Cuántos intentos tomó?: " + str(intentos)

    #function to print failed guesses list
    #(has to be activated by user)
    def imprimir_lista():
        i = 0
        len_intentos = len(lista_intentos)
        while(i < len_intentos-1):
            if(lista_intentos[i] == 0):
                lista_intentos.remove(0) #removes calls to list (0 values) from list
            i = i + 1
        print(lista_intentos)

    #calculates the average of each round (guesses and time)
    #then prints the name of the "best" round
    def mejor_adivinanza(matriz):
        menor = matriz[0][2]/matriz[0][1]
        menor_nom = ""
        i = 0
        while i < len(matriz):
            j = 0
            while j < len(matriz[0]):
                if(matriz[i][2]/matriz[i][1] < menor):
                    menor = matriz[i][2]
                    menor_nom = matriz[i][0]
                else:
                    menor_nom = matriz[0][0]
                j = j + 1
            i = i + 1
        return menor_nom 

    #returns the name of the round with the lowest time
    def mejor_tiempo(matriz):
        menor = matriz[0][3]
        menor_nom = ""
        i = 0
        while i < len(matriz):
            j = 0
            while j < len(matriz[0]):
                if(matriz[i][3] < menor):
                    menor = matriz[i][2]
                    menor_nom = matriz[i][0]
                else:
                    menor_nom = matriz[0][0]
                j = j + 1
            i = i + 1
        return menor_nom

    #returns the best round based on average of guesses/top number
    #and shortest time
    def stats_rondas(matriz):
        print(matriz_rondas)
        mejor_a = mejor_adivinanza(matriz) 
        mejor_t = mejor_tiempo(matriz)
        return "La ronda con el mejor promedio de adivinanzas fue: " + mejor_a \
            + "\nLa ronda con el mejor tiempo fue: " + mejor_t

    #replaces the original inputted name 
    #with a name + round number
    #for repeated names
    #(assumes user is playing against themselves)
    def nombre_replace(nombre, rep):
        i = 1
        while i < len(matriz_rondas):
            j = 0
            while j < len(matriz_rondas[0]):
                if(matriz_rondas[i][j] == nombre):
                    matriz_rondas[i][j] = rep
                j = j + 1
            i = i + 1
        return ""
    
    #call functions for each round
    #activates, ends + prints timer
    comienzo(nombre, tope)
    start_time = time.time()
    print(adivina_compara(adivinanza, intentos))
    end_time = time.time()
    total_time = round(end_time-start_time,2)
    lista_ronda.append(total_time)
    matriz_rondas.append(lista_ronda)
    print("¿Cuánto tiempo tomó?:", total_time, "secs")

    #checks if user name has been repeated
    if(c > 1): 
        i = 0
        while i < len(matriz_rondas):
            j = 0
            while j < len(matriz_rondas[0]):
                if(matriz_rondas[0][i] == nombre):
                    nombre_repeat = nombre + str(c)
                    nombre_replace(nombre, nombre_repeat)
                j = j + 1
            i = i + 1

    #adds to counter for multiple-round name adjustment
    c = c + 1

    #asks user if they'd like to play again
    #if yes, restarts the loop / activates another round
    check = input("¿Quieres jugar de nuevo? Escribe y o n \n")
    if(check == "y"):
        continue
    else:
        print(stats_rondas(matriz_rondas)) #final results of the game
    break