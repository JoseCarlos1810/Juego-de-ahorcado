# Ahorcado
### Contexto
El ahorcado (también llamado colgado) es un juego originalmente de lápiz y papel para dos o más jugadores. Un jugador piensa en una palabra, frase u oración y el otro trata de adivinarla según lo que sugiere por letras o dentro de un cierto número de oportunidades que son contadas haciendo a un humano de palo siendo ahorcado; por ello el nombre del juego. Cada vez que dices una letra que no está en la palabra o dices una palabra que no es la que había pensado, el otro jugador se dibujará una parte del humano de palo hasta completar un humano de palo ahorcado.

Este programa sera un juego de ahorcado donde se podra seleccionar si jugar individualmente o de dos jugadores, si se elije la opción de jugar individualmente, se seleccionara una palabra de una forma aleatoria de una lista de palabras, con un minimo de 6 letras y un maximo de 10, y comenzara el juego del ahorcado con las reglas antes descritas, si se selecciona la opción de dos jugadores, se le pedira ingresar una palabra, con un minimo de 6 letras y un maximo de 10, al primer jugador y el segundo jugador comenzara a jugar con las reglas ya descritas. Antes de seleccionar el modo se mostraran las instrucciones para jugar al ahorcado y un juego de practica con la palabra "Ahorcado"

# ¿Por qué?
Para este proyecto elegí el juego del ahorcado. Esto debido a que me ayudará a retar mis conocimientos de la programación, al igual que practicar todo lo que aprenda desde que inicie el proyecto hasta finalizarlo. A su vez, el juego de ahorcado me parece interesante ya que lo podría usar hasta en otros idiomas para aprender distintas palabras de forma aleatoria y, por último, también lo elegí ya que lo puedo usar para hacer algo en algún tiempo libre que tenga y, en el caso del modo de dos jugadores, usarlo con otras personas para pasar el rato.

# ¿Cómo funciona?
Este codigo funciona a base de listas, ciclos, condicionales y distintas funciones básicas como el print y el input. En este caso se uso listas para las palabras y letras que se usan en el ahorcado, junto con ello, las condicionales sirvieron para verificar si había o no una letra dentro de la palabra, usando los ciclos para verificar las posiciones donde se encontraba o encontraban las letras, esto solo fue en el juego del ahorcado, también se usaron para poder jugar nuevamente sin tener que salir y para verificar que tipo de juego querías.
# Instrucciones
Descargar el arvhivo:

python codigo_ahorcado.py

Correrlo en terminal o abrir en Thonny y darle al boton de play.

Jugar al ahorcado con las instrucciones descritas anteriormente

Gracias por visitar
# Algoritmo
### Entradas
Modo al que se jugara

En caso de ser de dos jugadores o prueba, ingresar la palabra

Letras (Para adivinar la palabra)
### Proceso
Solicitar al usuario elegir un modo de juego, individual, de dos jugadores, tutorial o prueba

Si elije el modo individual:

•	Elegir aleatoriamente una palabra de una lista de palabras

•	Mostrar el mástil donde ira el ahorcado

•	Mostrar los guiones donde irán las letras

•	Solicitar al usuario letras para completar la palabra

•	Si la letra está en la palabra ponerlas en la pantalla las veces que se repita

•	Si la letra no está en la palabra ponerle al muñeco una parte más, iniciando con la cabeza, luego los ojos, luego la boca, luego el cuerpo, luego un brazo, luego el otro, luego una pierna y por último la otra pierna. También se mostrarán las letras que haya intentado, pero no estuvieran en la palabra

•	Mientras no se complete el ahorcado, se le seguirá pidiendo letras hasta que gane completando la palabra o pierda completando el ahorcado

Si elije el modo de dos jugadores:

•	Pedir una palabra al jugador uno

•	Mostrar el mástil donde ira el ahorcado

•	Mostrar los guiones donde irán las letras

•	Solicitar al jugador dos letras para completar la palabra

•	Si la letra está en la palabra ponerlas en la pantalla las veces que se repita

•	Si la letra no está en la palabra ponerle al muñeco una parte más, iniciando con la cabeza, luego los ojos, luego la boca, luego el cuerpo, luego un brazo, luego el otro, luego una pierna y por último la otra pierna. También se mostrarán las letras que haya intentado, pero no estuvieran en la palabra

•	Mientras no se complete el ahorcado, se le seguirá pidiendo letras hasta que gane completando la palabra o pierda completando el ahorcado
Si elije el modo tutorial:

•	Dar una explicación extensa de las reglas y funcionamiento del ahorcado como lo que se acepta y lo que no se acepta en el código

•	Después de eso, usar el modo individual, pero la palabra que se seleccionó será siempre “ahorcado”, lo demás funcionará como el modo individual

Si elije el modo de prueba:

•	Se le pedirá al usuario que ingrese una palabra como en el modo de dos jugadores

•	Una vez el jugador ingrese la palabra, la computadora jugara el ahorcado seleccionando letras aleatoriamente 
### Salidas
Si adivina la palabra, mostrar mensaje “Felicidades, adivinaste la palabra”

Si completa el ahorcado por no adivinar la palabra, mostrar mensaje “Perdiste, el muñeco murió”

Dibujos del muñeco

Palabra que se tenía que adivinar

Letras que son incorrectas

Letras que son correctas

Espacios de la palabra


