"""Dibuja un ordinograma de un programa que lee dos números y muestra el mayor
"""


n1 = int(input("Dame el primer numero: "))
n2 = int(input("Dame el segundo numero: "))

if n1<n2:
    print(f"{n2} es mayor")
elif n1>n2:
    print(f"{n1} es mayor")
else:
    print("Ambos son el mismo numero")