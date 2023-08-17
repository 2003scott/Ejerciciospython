## Ejercicios de ESTADISTA INDIFERENCIAL

def autoprint():
    print()
    print("="*50)
    print()

print("-"*10,"ESTADISTA INDIFERENCIAL")
autoprint()

# cuando se conoce la poblacion
## Formula
#  
#           N x Z x P x q
#   n= ------------------------
#       d**2 (N-1) + Z x P x q
#







# cuando no se conoce la poblacion
## Formula
#  
#        Z x P x q 
#   n= ------------
#          d**2
#

autoprint()


print("--- Cuando no se conoce la poblacion ---")
autoprint()

p:float = 0.85 #probabilidad de exito
q:float = 0.15 #probabilidad de fracazo
z:float = 1.96 #
d:float = 0.05 

n:float=0

n = ((z)**2 * (p) * (q)) / d **2

print(n)








