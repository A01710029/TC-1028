#Estoy escribiendo los comentarios en inglés. Hablé con el 
#profesor sobre esta decisión.

#import math and random
import math
import random

#declare variables
nombre = str(input("¿Cómo te llamas?\n"))
adivinanza = int()
intentos = 0

#ask for top number
print("¿Cuál debería ser el número tope?")
tope = int(input())

#check that top number is not negative or zero
#once ok, generate random number
while(tope <= 0):
    print("El número tiene que ser mayor que cero.")
    print("¿Cuál debería ser el número tope?")
    tope = int(input())
num_compu = random.randint(1,tope)
    
#function to display game start text
def comienzo(nombre, tope):
    print("Hola", nombre)
    print("""¡Intenta adivinar en qué número 
entre 1 y""", str(tope) + """ estoy pensando!""")

#function to prompt, analyze, give feedback on, 
#and keep count of guesses
def adivina_compara(adivinanza, intentos):
    while (adivinanza != num_compu):
        adivinanza = int(input())
        if adivinanza < num_compu:
            intentos = intentos + 1
            print("Intenta un número más grande")
        elif adivinanza > num_compu:
            intentos = intentos + 1
            print("Intenta un número más pequeño")
    print("¡Adivinaste el número!")
    intentos = str(intentos)
    return "Cuántos intentos tomo?: " + intentos

#call function + print final results
comienzo(nombre, tope)
print(adivina_compara(adivinanza, intentos))