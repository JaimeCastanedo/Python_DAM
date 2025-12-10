"""Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales
son iguales
"""

n1 = int(input("Dame el primer numero: "))
n2 = int(input("Dame el segundo numero: "))
n3 = int(input("Dame el tercer numero: "))

if n1 >= n2 and n1 >= n2:
        mayor = n1
elif n2 >= n1 and n2 >= n3:
        mayor = n2
else:
        mayor = n3

  
if n1 <= n2 and n1 <= n3:
        menor = n1
elif n2 <= n1 and n2 <= n3:
        menor = n2
else:
        menor = n3
    
    
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")

    
if n1 == n2:
        print(f"Primero y Segundo son iguales")
if n1 == n3:
        print(f"Primero y Tercero son iguales")
if n2 == n3:
        print(f"Segundo y Tercero son iguales")
    
if n1 == n2 == n3:
        print("Los tres números son iguales")