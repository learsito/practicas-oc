#spam = input("Cuántas cifras desea operar? (Elija de 2 a 4): ")

def dosvar():
    a=input("Introduzca el valor: ")
    op=input("Elija una operación (+, -, /, *): ")
    b=input("Introduzca el valor: ")
    print("\nEl resultado es: ")
    if op == "+":

        print( int(a) + int(b) )
    else: 
        print("ERROR EN EL OPERADOR")

dosvar()
z=input("Es correcto? ")