import random
from unicodedata import normalize
adivinar=[]
errores=[]
dibujo= [
'''
   _____
   |   |
       |
       |
       |
       |
=========
''', 
'''
   _____
   |   |
   O   |
       |
       |
       |
=========
''',
'''
   _____
   |   |
   O   |
   |   |
       |
       |
=========
''',
  '''
   _____
   |   |
   O   |
  /|   |
       |
       |
=========
''',
'''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========
''',
'''
   _____
   |   |
   O   |
  /|\  |
  /    |
       |
=========
''','''
  ______
   |   |
   O   |
  /|\  |
  / \  |
       |
=========
''']

#Esta función mostrara un mensaje ganador o perdedor según sea el caso
def resultado(intentos):
    if intentos==6:
        print("""
██████╗░███████╗██████╗░██████╗░██╗░██████╗████████╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔════╝
██████╔╝█████╗░░██████╔╝██║░░██║██║╚█████╗░░░░██║░░░█████╗░░
██╔═══╝░██╔══╝░░██╔══██╗██║░░██║██║░╚═══██╗░░░██║░░░██╔══╝░░
██║░░░░░███████╗██║░░██║██████╔╝██║██████╔╝░░░██║░░░███████╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝
""")
    else:
        print("""

░██████╗░░█████╗░███╗░░██╗░█████╗░░██████╗████████╗███████╗
██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██║░░██╗░███████║██╔██╗██║███████║╚█████╗░░░░██║░░░█████╗░░
██║░░╚██╗██╔══██║██║╚████║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░
╚██████╔╝██║░░██║██║░╚███║██║░░██║██████╔╝░░░██║░░░███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝
        """)

#Esta función es un caso prueba el cual elejira letras random para completar la palabra que se ponga en la terminal
def pruebas():
    palabra=tu_ponla()
    intentos=0
    palabra_prueba=list(palabra)
    abecedario=list('abcdefghijklmnñopqrstuvwxyz')
    adivinar=espacio_palabras(palabra_prueba)
    menu1(intentos)
    while intentos<6:
        letra=random.choice(abecedario)
        if letra in palabra_prueba:
            for i in range(len(adivinar)):
                if letra==palabra_prueba[i]:
                    adivinar[i]=letra
            menu1(intentos)
            if adivinar==palabra_prueba:
                print("Felicidades, adivinaste la palabra")
                final()
                resultado(intentos)
                break
        else:
            intentos+=1
            errores.append(letra)
            menu1(intentos)
    if intentos==6:
        print("Perdiste, el muñeco murió")
        print("La palabra era:", palabra_prueba)
        final()
        resultado(intentos)

#Esta es una función donde se puede agregar palabras al final del archivo
def agregar_palabras():
    archivo=open("palabras.txt","a+")
    agregar=input("Dime que palabra quieres que agregue: ")
    archivo.write(agregar)
    archivo.write("\n")
    archivo.seek(0)
    archivo.close()
    
#Esta es una función donde se elegira una palabra random de una lista de varias palabras
def palabra_random():
    archivo=open("palabras.txt","r")
    archivo.seek(0)
    lineas_archivo=archivo.readlines()
    numero_lineas=len(lineas_archivo)
    palabra_random=random.randint(0,numero_lineas)
    palabra=lineas_archivo[palabra_random]
    return palabra

#Esta es una función donde se imprimen las instrucciones de como jugar y hace que la palabra a adivinar sea ahorcado
def tutorial():
    print("En este juego tienes que intentar adivinar una palabra poniendo letras las cuales llenaran los espacios si están en la palabra, tienes un total de \
6 intentos y te aparecerán las letras que ya intentaste, pero no estaban en la palabra, lo siguiente es una prueba donde la palabra es ahorcado, también hay \
que mencionar que no hay acentos ni símbolos en las palabras")
    palabra="ahorcado"
    return palabra

#Esta es una función donde se le pide al usuario que ponga la palabra con la que quiere jugar
def tu_ponla():
    palabra=input("Dime que palabra quieres poner: ")
    return palabra

#Esta es una función donde la palabra seleccionada se hace minuscula y se le quitan signos y símbolos
def corregir_palabra(palabra):
    palabra_minusculas=palabra.lower()
    palabra_ahorcado=normalize('NFKD', palabra_minusculas).encode('ASCII', 'ignore').decode('ASCII')
    ultima=len(palabra)
    palabra_final=palabra_ahorcado[:-1]
    return palabra_final

#Esta es una función donde se hace una lista de espacios en blanco para saber la longitud de la palabra
def espacio_palabras(letras):
    for i in range(len(letras)):
        adivinar.append("_")
    return adivinar

#Esta es una función donde limpia las listas de letras adivinadas y las letras incorrectas
def final():
    adivinar.clear()
    errores.clear()
 
#Esta es una función donde se muestra un menu el cual contiene el dibujo del ahorcado, las letras adivinadas y las letras incorrectas
def menu1(intentos):
    print(dibujo[intentos])
    print("Palabra: ",adivinar)
    print("Incorrectas: ",errores)

#Esta es una función donde se hará el proceso del ahorcado para verificar si esta bien o mal la letra que adivino el usuario, asi como llamar a las demás funciones
def ahorcado(op):
    intentos=0
    print("Solo hay letras del abecedario, en caso de poner un número o símbolo, se contará como incorrecto")
    if op==1:
        palabra=palabra_random()
    elif op==2:
        palabra=tu_ponla()
    elif op==3:
        palabra=tutorial()
    palabra_ahorcado=corregir_palabra(palabra)
    letras=list(palabra_ahorcado)
    adivinar=espacio_palabras(letras)
    menu1(intentos)
    while intentos<6:
        letra=input('Dime una letra a adivinar: ')
        letra_final=letra.lower()
        if letra_final in letras:
            for i in range(len(adivinar)):
                if letra_final==letras[i]:
                    adivinar[i]=letra_final
            menu1(intentos)
            if adivinar==letras:
                print("Felicidades, adivinaste la palabra")
                final()
                resultado(intentos)
                break
        else:
            intentos+=1
            errores.append(letra_final)
            menu1(intentos)
    if intentos==6:
        print("Perdiste, el muñeco murió")
        print("La palabra era:", palabra_ahorcado)
        final()
        resultado(intentos)
#Esta es una función donde se despliega el menu de opciones para que el usuario vea que puede hacer    
def menu2():
    print("1. Solitario")
    print("2. Tu pon la palabra")
    print("3. Tutorial")
    print("4. Agregar palabra")
    print("5. Salir")
    print("6. Prueba")
    
#Esta es una función donde se le pregunta al usuario que opción del menu quiere elegir y llamar a la función ahorcado de la forma que eliga el usuario
def main():
    continuar=True
    while continuar:
        menu2()
        op=input("Qué quieres hacer: ")
        if op!="1" and op!="2" and op!="3" and op!="4" and op!="5" and op!="6":
            print("Lo que pusiste es incorrecto")
        else:
            if op=="1":
                ahorcado(1)
            elif op=="2":
                ahorcado(2)
            elif op=="3":
                ahorcado(3)
            elif op=="4":
                agregar_palabras()
            elif op=="5":
                continuar=False
            elif op=="6":
                pruebas()
                
main()
