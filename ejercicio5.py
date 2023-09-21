## Ejercicios de ESTADISTA INDIFERENCIAL

def autoprint():
    print()
    print("="*45)
    print()

print("-"*10,"ESTADISTA INDIFERENCIAL")
autoprint()

print("--- Cuando se conoce la poblacion ---")
autoprint()

## Formula
#  
#           N x Z x P x q
#   n= ------------------------
#       d**2 (N-1) + Z x P x q
#

n:int= 0 #tamaño de confianza
p:float = 0 #probabilidad de exito
q:float = 0 #probabilidad de fracazo
z:float = 0 #nivel de confianza / normalmente es de (1-α =0.95 -> z = 1.96)
d:float = 0 #margen de error

n= int(input("Ingresa - (N) - : "))
p = float(input("Ingresa - '(P)' - : "))
q = float(input("Ingresa - '(q)' - : "))
d = float(input("Ingresa - '(d) -o- (e)' - : "))
z:float = 1.96  
autoprint()
# print(z,"² x",p,"x",q) 
# print("----------------------")
# print(d,"²")
# autoprint()

r:float=0 

r = ((n) * (z**2) * (p) * (q)) / (d**2) * (n-1) + (z**2) * (p) * (q)                                 
print("Resultado : ",r)
print("Redondeado : ",round(r))




# # cuando no se conoce la poblacion

# autoprint()

# print("--- Cuando no se conoce la poblacion ---")
# autoprint()

# ## Formula
# #  
# #        Z x P x q 
# #   n= ------------
# #          d**2
# #

# p:float = 0 #probabilidad de exito
# q:float = 0 #probabilidad de fracazo
# z:float = 0 #nivel de confianza / normalmente es de (1-α =0.95 -> z = 1.96)
# d:float = 0 #margen de error

# p = float(input("Ingresa - '(P)' - : "))
# q = float(input("Ingresa - '(q)' - : "))
# d = float(input("Ingresa - '(d) -o- (e)' - : "))
# z:float = 1.96
# autoprint()

# print(z,"² x",p,"x",q) 
# print("----------------------")
# print(d,"²")

# autoprint()

# n:float=0 

# n = ((z**2) * (p) * (q)) / d **2                                 
# print("Resultado : ",n)
# print("Redondeado : ",round(n))



