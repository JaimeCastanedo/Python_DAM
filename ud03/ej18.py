"""Dibuja un ordinograma de un programa que lea dos números y nos diga cual es mayor o si
son iguales
"""


n1 = int(input("Dame el primer numero: "))
n2 = int(input("Dame el segundo numero: "))

if n1==n2:
    print("Son iguales")
elif n1>n2:
    print(f"{n1} es el mayor")
else:
    print(f"{n2} es el mayor")