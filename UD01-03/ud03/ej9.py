"""Dibuja un ordinograma de un programa que pida la edad por teclado y nos muestra el
mensaje de “Eres mayor de edad” o el mensaje de “Eres menor de edad”.
"""


edad = int(input("Dame una edad: "))

if edad<18:
    print("Eres menor de edad")
else:
    print("")