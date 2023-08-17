## Hacer un yan ken po

op1 = 0
op2 = 0
def printauto():
    print("-"*15)

def opciones():
    print("1.Piedra")
    print("2.Papel")
    print("3.Tigera")

player1 = input("Ingresa tu nombre player 1 :").upper()
player2 = input("Ingresa tu nombre player 2 :").upper()
printauto()
opciones()
printauto()
print(player1," - Ingresa tu movimiento")
op1 = int(input("Elige una opcion <1 - 3>"))
while op1 <1 or op1>4:
    print("Opcion no habilitada")
    op1 = int(input("Elige una opcion <1 - 3>"))
if  op1 == 1:
    print("Piedra")
elif  op1 == 2:
    print("Papel")
elif op1 == 3:
    print("Tigera")
    
print(player2," - Ingresa tu movimiento")
op2 = int(input("Elige una opcion <1 - 3>"))
while op2 <1 or op2>4:
    print("Opcion no habilitada")
    op2 = int(input("Elige una opcion <1 - 3>"))
if  op2 == 1:
    print("Piedra")
elif  op2 == 2:
    print("Papel")
else:
    print("Tigera")

printauto()

if op1 ==1 and op2==2 : 
    print("Gano el player : ",player2)
elif op1 ==1 and op2==3 : 
    print("Gano el player : ",player1)
elif op1 ==1 and op2==1:
    print("Quedaron parejos - EMPATE")

if op1 ==2 and op2==1 : 
    print("Gano el player : ",player1)
elif op1 ==2 and op2==3 : 
    print("Gano el player : ",player2)
elif op1 ==2 and op2==2:
    print("Quedaron parejos - EMPATE")

if op1 ==3 and op2==1 : 
    print("Gano el player : ",player2)
elif op1 ==3 and op2==2 : 
    print("Gano el player : ",player1)
elif op1 ==3 and op2==3:
    print("Quedaron parejos - EMPATE")