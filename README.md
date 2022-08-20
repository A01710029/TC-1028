# TC-1028 Proyecto Libre Final
### Contexto
Este programa es un juego de adivinanza de números. El usuario ingresa un número "tope" para definir el rango dentro del cual el programa genera un número aleatorio. Después, el usuario debe adivinar este número. El programa devuelve cuántos intentos y cuánto tiempo necesitó el usuario para adivinar correctamente y muestra los intentos anteriores durante el juego para que se pueda guiar el usuario.

El programa está basado en el juego de adinivir el número, en el cual una persona piensa en un número aleatorio, le dice a la otra persona el rango en el que está este número y con esa información la otra persona debe adivinarlo. 

Me parece un proyecto interesante porque siempre me ha gustado jugar este juego con mis amigos y mi familia, pero un programa puede crear un número totalmente aleatorio, mientras que las personas tendemos a escoger ciertos números. Por ejemplo, ya que conozco muy bien a mi hermana, sé sus números favoritos y puedo utilizar esos para guiar mis adivinanzas. Además, un programa puede trabajar con rangos mucho más grandes y no puede cambiar ni se le puede olvidar el número, lo que asegura un juego más divertido y justo para el que debe adivinar.

### Instrucciones
importar random
importar time

EO(pedir num_tope)
int intentos = 0
float timer = 0
intentos_previos = {}
int num_compu = 0
int adivinanza = 0

generar valor de num_compu con random
empezar timer

mientras adivinanza =/= num_compu
    pedir(adivinanza)
    si adivinanza < num_compu
        devolver("Intenta un número más pequeño")
    si adivinanza > num_compu
        devolver("Intenta un número más grande")
    agregar adivinanza a intentos_previos
    intentos = intentos + 1
    devolver intentos_previos
 
 parar timer
 devolver("Adivinaste correctamente!")
 EF(intentos, timer)

