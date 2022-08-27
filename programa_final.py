#Profesor, como nota personal, aprendí a programar en inglés y estoy acostumbrada
#a escribir mis comentarios en inglés. ¿Le molesta si comento
#mi proyecto final en inglés, o quiere que lo haga en español?

#import math and random
import math
import random

#greet user

#ask for top number
print("¿Cuál debería ser el número tope?")
tope = int(input())

#generate random number
num_compu = random.randint(0,tope)

#prompt user to start guessing
adivinanza = int(input())

#compare user guess to random number
if adivinanza < num_compu:
    print("Intenta un número más pequeño")
elif adivinanza > num_compu:
    print("Intenta un número más grande")

intentos = int()
intentos = intentos + 1