"""Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división (Ten en cuenta la división por cero)
"""


n1 = int(input("Dame el lado del primer numero: "))
n2 = int(input("Dame el lado del segundo numero: "))

suma = n1+n2
print(f"La suma es {suma}")
resta = n1-n2
print(f"La resta es {resta}")
mult = n1*n2
print(f"La multiplicacion es {mult}")

if n2 == 0:
    print("No se puede dividir")

else:
    div = n1/n2
    print(f"La division es {div}")