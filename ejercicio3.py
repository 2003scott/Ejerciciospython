## Imprimir todos los numeros pares

def printauto():
    print("-"*15)

printauto()
n= int(input("Elije el rango de numeros : "))

for i in range (n+1):
    if i  %2==0 :
        print(i)
    

## Imprimir todos los numeros impares

printauto()
n= int(input("Elije el rango de numeros : "))

for i in range (n+1):
    if i  %2!=0 :
        print(i)



