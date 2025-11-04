"""Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división.
"""

n1 = int(input("Dame el lado del primer numero: "))
n2 = int(input("Dame el lado del segundo numero: "))

suma = n1+n2
resta = n1-n2
mult = n1*n2
div = n1//n2

print(f"La suma es: {suma}")
print(f"La rtesta es: {resta}")
print(f"La multiplicacion es: {mult}")
print(f"La division es: {div}")