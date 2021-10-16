#Hello world:
def helloWorld():
    print('Hello world!')
    #Puedo generar tantos prints como quiera, y cada declaración print generará el texto en una línea nueva:
    print('Hola mundo!')
    print('Jai!')
    print('Arigato!')


#Operaciones simples:
def operacionesSimples():
    print(2+2)
    print(5 + 4 - 3)
    print( 10/2 * ( 2*(3+4) ) )
    print((4+8)/2) #Una división (/) generará siempre un float, por lo tanto en este caso el resultado no sería 6, sino 6.0

#Tipos de datos:
def tiposDatos():
    cadena="Esto es una cadena de carácteres"
    entero=5
    flotante=5.5
    print(type(cadena),type(entero),type(flotante))
#Maneras en que se produce un float:
def floatWays():
    print( 8 / 2 )
    print( 6 * 7.0 )
    print( 4 + 1.65 )

#Exponenciación:
def esponenciacion():
    print( 2**5 ) #Aquí el '**' representa la exponenciación. En este caso  se leería como 2 elevado a la 5, o 5*5*5*5*5
    ejemplo=5**3**2 #Se pueden encadenar exponenciaciones, como se muestra en el ejemplo  de la izquierda.
    print(9**(1/2) ) #Es posible usar los floats. El anterior ejemplo da como resultado la raíz cuadrada de 9, por lo tanto resultará en un Float.

def pracBac(): #Ejercicio de práctica: Cultivo de bacterias comienza con 500 bacterias y duplica su tamaño cada hora. Calcular el número de bacterias que habrá en el cultivo según las horas dadas como input.
    h=input("Introduzca horas transcurridas: ")
    cantdBactrs=500*(2**h)
    print(cantdBactrs)
    
