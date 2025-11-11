"""Dibuja un ordinograma de un programa que lea dos números y lo visualiza en orden
ascendente.
"""

n1 = int(input("Dame el primer numero: "))
n2 = int(input("Dame el segundo numero: "))

if n1<n2:
    print(n1,n2)
else:
    print(n2,n1)