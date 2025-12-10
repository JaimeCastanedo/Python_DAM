"""Escriba un programa que toma como dato de entrada un número que corresponde a la
longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud
de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la esfera
que corresponde con dicho radio.
"""
import math

pi = math.pi
r = int(input("Dame el radio del cuadrado: "))

long = 2*r*pi
area = pi*r**2
vol = (4*pi*r**3)/3

print(f"la longitd es: {long}, el area es: {area} y el volumen es: {vol}")
