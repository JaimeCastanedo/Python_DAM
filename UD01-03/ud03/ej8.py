"""Dibuja un ordinograma de un programa que pide la edad por teclado y nos muestra el
mensaje de “Eres mayor de edad”, si y solamente si lo somos.
"""


edad = int(input("Dame una edad: "))

if edad>18:
    print("Eres mayor de edad")
else:
    print("")