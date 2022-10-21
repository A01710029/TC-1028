# TC-1028 Proyecto Libre Final
### Contexto
Este programa es un juego de adivinanza de números. El programa empieza con el programa pidiendo al usuario que ingrese un número "tope" para definir el rango dentro del cual el programa genera un número aleatorio. Con este número, el programa crea un número y este se guarda. Cuando este número se genera, el programa empieza un timer que sirve como cronógrafo y dice cúanto tiempo ha pasado desde que el juego empezó. Ahora, el usuario debe adivinar el número. Cada turno, el programa pide una adivinanza del usuario, y el programa dice si esa adivinanza es más grande o más pequeña que el número que se generó aleatoriamente. También muestra los intentos anteriores en forma de lista para que se pueda guiar el usuario. Cada turno que no se adivina correctamente, el programa agrega 1 a la cuenta de los intentos. Cuando se adivina correctamente, el timer se para y el programa devuelve cuántos intentos y cuánto tiempo le tomó al usuario. Con esto, el juego y el programa terminan.

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
     
 ### API
Las bibliotecas que se importaron y usaron para este proyecto son random (https://docs.python.org/3/library/random.html) y time (https://docs.python.org/3/library/time.html). 

La biblioteca random se utiliza con la función "random.randint(rango)", que sirve en el programa para generar el número aleatorio que el usuario debe adivinar, con el número tope que el usuario asigna sirviendo como el límite del rango (línea 50). 

La biblioteca time se utiliza con las función "time.time()", que sirve en el programa para crear el cronómetro del programa. Inicia a contar el tiempo cuando inicia la ronda y para de contar el tiempo cuando la ronda termina (líneas 130 y 132).  
