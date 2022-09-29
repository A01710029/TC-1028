#Estoy escribiendo los comentarios en inglés. Hablé con el 
#profesor sobre esta decisión.

#import math, random, and time
import math
import random

#declare variables
nombre = str(input("¿Cómo te llamas?\n"))
adivinanza = int()
intentos = 1
lista_intentos = []

#ask for top number
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
    print("Hola", nombre)
    print("""¡Intenta adivinar en qué número 
entre 1 y""", str(tope) + """ estoy pensando!""")
    print("Escribe '0' si quieres ver tus intentos anteriores")

#function to prompt, analyze, give feedback on, 
#and keep count of guesses
#add failed guesses to list
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
    intentos = str(intentos)
    return "¿Cuántos intentos tomo?: " + intentos

#function to print failed guesses list
#(has to be activated by user)
def imprimir_lista():
    i = 0
    len_intentos = len(lista_intentos)
    while(i < len_intentos-1):
        if(lista_intentos[i] == 0):
            lista_intentos.remove(0) #removes calls to list from list
        i = i + 1
    print(lista_intentos)

#call function + print final results
comienzo(nombre, tope)
print(adivina_compara(adivinanza, intentos))