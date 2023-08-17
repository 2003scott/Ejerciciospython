## hacer un sumador de numeros

suma=0

n= int(input("Elijer el rango : "))

for i in range (1,n+1):
    print(i)
    suma = suma + i ##Esto alamacena los numero en nuestra variable y las va sumando
print(suma)