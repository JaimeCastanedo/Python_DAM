"""Dibuja un ordinograma de un programa que suma independientemente los pares y los
impares de los números comprendidos entre 100 y 200, y luego muestre por pantalla ambas
sumas.
"""

suma_pares = 0
suma_impares = 0
numero = 100

while numero <= 200:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
    
    numero = numero + 1

print("Suma de números pares entre 100 y 200:", suma_pares)
print("Suma de números impares entre 100 y 200:", suma_impares)