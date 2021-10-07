def dosvar():
    a=input("Introduzca el primer valor: ")
    op=input("Elija operador (+,  -,  /,  *): ")
    b=input("Introduzca siguiente valor: ")
    print("\nEl resultado es: ")
    a=int(a)
    b=int(b)
    if op == "+":
        print( a + b )
    elif op == '-':
        print(a - b)
    elif op == '/':
        print(a / b)
    elif op == '*':
        print(a * b)
    else: 
        print(error)

def tresvar():
    a=input("Introduzca el primer valor: ")
    op=input("Elija operador (+, -, /, *): ")
    b=input("Introduzca siguiente valor: ")
    op2=input("Introduzca siguiente operador (+, -, /, *): ")
    c=input("Introduzca siguiente valor: ")
    print('El resultado es: ')
    a=int(a)
    b=int(b)
    c=int(c)
    if op == '+' and op2 == '+':
        print( a + b + c)
    elif op == '+' and op2 == '-':
        print(a + b - c)
    elif op == '+' and op2 == '/':
        print(a + b / c)
    elif op == '+' and op2 == '*':
        print(a + b * c)
    elif op == '-' and op2 == '+':
        print(a - b + c)
    elif op == '-' and op2 == '-':
        print(a - b - c)
    elif op == '-' and op2 == '/':
        print(a - b / c)
    elif op == '-' and op2 == '*':
        print(a - b * c)
    elif op == '/' and op2 == '+':
        print(a / b + c)
    elif op == '/' and op2 == '-':
        print(a / b - c)
    elif op == '/' and op2 == '/':
        print(a / b / c)
    elif op == '/' and op2 == '*':
        print(a / b * c)
    elif op == '*' and op2 == '+':
        print(a * b + c)
    elif op == '*' and op2 == '-':
        print(a * b - c)
    elif op == '*' and op2 == '/':
        print(a * b / c)
    elif op == '*' and op2 == '*':
        print(a * b * c)
    else:
        print(error)

def quadvar():
    a=input("Introduzca el primer valor: ")
    op=input("Elija operador (+, -, /, *): ")
    b=input("Introduzca siguiente valor: ")
    op2=input("Introduzca siguiente operador (+, -, /, *): ")
    c=input("Introduzca siguiente valor: ")
    op3=input("Introduzca siguiente operador (+, -, /, *): ")
    d=input("Introduzca siguiente valor: ")
    print('El resultado es: ')
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    if op == '+' and op2 == '+' and op3 == '+':
        print(a + b + c + d)
    elif op == '+' and op2 == '+' and op3 == '-':
        print(a + b + c - d)
    elif op == '+' and op2 == '+' and op3 == '/':
        print(a + b + c / d)
    elif op == '+' and op2 == '+' and op3 == '*':
        print(a + b + c * d)
    elif op == '+' and op2 == '-' and op3 == '+':
        print(a + b - c + d)
    elif op == '+' and op2 == '-' and op3 == '-':
        print(a + b - c - d)
    elif op == '+' and op2 == '-' and op3 == '/':
        print(a + b - c / d)
    elif op == '+' and op2 == '-' and op3 == '*':
        print(a + b - c * d)
    elif op == '+' and op2 == '/' and op3 == '+':
        print(a + b / c + d)
    elif op == '+' and op2 == '/' and op3 == '-':
        print(a + b / c - d)
    elif op == '+' and op2 == '/' and op3 == '/':
        print(a + b / c / d)
    elif op == '+' and op2 == '/' and op3 == '*':
        print(a + b / c * d)
    elif op == '+' and op2 == '*' and op3 == '+':
        print(a + b * c + d)
    elif op == '+' and op2 == '*' and op3 == '-':
        print(a + b * c - d)
    elif op == '+' and op2 == '*' and op3 == '/':
        print(a + b * c / d)
    elif op == '+' and op2 == '*' and op3 == '*':
        print(a + b * c * d)
    elif op == '-' and op2 == '+' and op3 == '+':
        print(a - b + c + d)
    elif op == '-' and op2 == '+' and op3 == '-':
        print(a - b + c - d)
    elif op == '-' and op2 == '+' and op3 == '/':
        print(a - b + c / d)
    elif op == '-' and op2 == '+' and op3 == '*':
        print(a - b + c * d)
    elif op == '-' and op2 == '-' and op3 == '+':
        print(a - b - c + d)
    elif op == '-' and op2 == '-' and op3 == '-':
        print(a - b - c - d)
    elif op == '-' and op2 == '-' and op3 == '/':
        print(a - b - c / d)
    elif op == '-' and op2 == '-' and op3 == '*':
        print(a - b - c * d)
    elif op == '-' and op2 == '/' and op3 == '+':
        print(a - b / c + d)
    elif op == '-' and op2 == '/' and op3 == '-':
        print(a - b / c - d)
    elif op == '-' and op2 == '/' and op3 == '/':
        print(a - b / c / d)
    elif op == '-' and op2 == '/' and op3 == '*':
        print(a - b / c * d)
    elif op == '-' and op2 == '*' and op3 == '+':
        print(a - b * c + d)
    elif op == '-' and op2 == '*' and op3 == '-':
        print(a - b * c - d)
    elif op == '-' and op2 == '*' and op3 == '/':
        print(a - b * c / d)
    elif op == '-' and op2 == '*' and op3 == '*':
        print(a - b * c * d)
    elif op == '/' and op2 == '+' and op3 == '+':
        print(a / b + c + d)
    elif op == '/' and op2 == '+' and op3 == '-':
        print(a / b + c - d)
    elif op == '/' and op2 == '+' and op3 == '/':
        print(a / b + c / d)
    elif op == '/' and op2 == '+' and op3 == '*':
        print(a / b + c * d)
    elif op == '/' and op2 == '-' and op3 == '+':
        print(a / b - c + d)
    elif op == '/' and op2 == '-' and op3 == '-':
        print(a / b - c - d)
    elif op == '/' and op2 == '-' and op3 == '/':
        print(a / b - c / d)
    elif op == '/' and op2 == '-' and op3 == '*':
        print(a / b - c * d)
    elif op == '/' and op2 == '/' and op3 == '+':
        print(a / b / c + d)
    elif op == '/' and op2 == '/' and op3 == '-':
        print(a / b / c - d)
    elif op == '/' and op2 == '/' and op3 == '/':
        print(a / b / c / d)
    elif op == '/' and op2 == '/' and op3 == '*':
        print(a / b / c * d)
    elif op == '/' and op2 == '*' and op3 == '+':
        print(a / b * c + d)
    elif op == '/' and op2 == '*' and op3 == '-':
        print(a / b * c - d)
    elif op == '/' and op2 == '*' and op3 == '/':
        print(a / b * c / d)
    elif op == '/' and op2 == '*' and op3 == '*':
        print(a / b * c * d)
    elif op == '*' and op2 == '+' and op3 == '+':
        print(a * b + c + d)
    elif op == '*' and op2 == '+' and op3 == '-':
        print(a * b + c - d)
    elif op == '*' and op2 == '+' and op3 == '/':
        print(a * b + c / d)
    elif op == '*' and op2 == '+' and op3 == '*':
        print(a * b + c * d)
    elif op == '*' and op2 == '-' and op3 == '+':
        print(a * b - c + d)
    elif op == '*' and op2 == '-' and op3 == '-':
        print(a * b - c - d)
    elif op == '*' and op2 == '-' and op3 == '/':
        print(a * b - c / d)
    elif op == '*' and op2 == '-' and op3 == '*':
        print(a * b - c * d)
    elif op == '*' and op2 == '/' and op3 == '+':
        print(a * b / c + d)
    elif op == '*' and op2 == '/' and op3 == '-':
        print(a * b / c - d)
    elif op == '*' and op2 == '/' and op3 == '/':
        print(a * b / c / d)
    elif op == '*' and op2 == '/' and op3 == '*':
        print(a * b / c * d)
    elif op == '*' and op2 == '*' and op3 == '+':
        print(a * b * c + d)
    elif op == '*' and op2 == '*' and op3 == '-':
        print(a * b * c - d)
    elif op == '*' and op2 == '*' and op3 == '/':
        print(a * b * c / d)
    elif op == '*' and op2 == '*' and op3 == '*':
        print(a * b * c * d)
    else:
        print(error)

error="ERROR EN EL OPERADOR"
loop ='no'
print("~~~~~~~~~~BIENVENIDO~~~~~~~~~~")
while loop  == 'no':
    print("Elija una opción: ")
    spam = input("Cuántas cifras desea operar? (Elija de 2 a 4): ")
    if spam == '2':
        dosvar()
    elif spam == '3':
        tresvar()
    elif spam == '4':
        quadvar()
    else:
        print("No es posible operar con esta cantidad de sifras.")
    loop=input('Desea salir del programa? (Escriba "si" o "no"): ')
    while loop != 'si' and loop != 'no':
        loop=input('Esta opción no es posible. Escriba una opción válida ("si" o "no"): ')