## hacer operaciones aritmeticas

def printauto():
    print("-"*15)

def opciones():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

def operacion(a,b):
    if op == 1 :
       resultado =  a + b
    elif op == 2 :
        resultado =  a - b
    elif op == 3 :
        resultado =  a * b
    elif op == 4 :
        resultado =  a / b
    return resultado

op = 0
while op != 4:
    printauto()
    opciones()
    printauto()
    op = int(input("Ingresa una Opcion del <1 - 4> : "))
    while op <1 or op > 5 :
        print("Intenta denuevo opcion fuera de rango")
        op = int(input("Ingresa una Opcion del <1 - 4> : "))
    printauto()
    if op == 1 :
        a = float(input("Ingresa el primer numero : "))
        b = float(input("Ingresa el segundo numero : "))
        printauto()
        print("Resultado --> ",operacion(a,b))
    elif op == 2 :
        a = float(input("Ingresa el primer numero : "))
        b = float(input("Ingresa el segundo numero : "))
        printauto()
        print("Resultado --> ",operacion(a,b))
    elif op == 3 :
        a = float(input("Ingresa el primer numero : "))
        b = float(input("Ingresa el segundo numero : "))
        printauto()
        print("Resultado --> ",operacion(a,b))
    elif op == 4 :
        a = float(input("Ingresa el primer numero : "))
        b = float(input("Ingresa el segundo numero : "))
        printauto()
        print("Resultado --> ",operacion(a,b))
    else :
        print("Proceso terminado")
        break
