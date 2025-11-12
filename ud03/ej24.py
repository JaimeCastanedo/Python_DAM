"""Dibuja un ordinograma de un programa que calcule y escriba la suma y el producto de los
10 primeros números naturales.
"""

suma = 0
resta = 0
mult = 1
div = 1

for i in range(1,11):
    suma = suma + i    
    resta = i-resta
    mult = mult * i
    div = div/i

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicacion es: {mult}")
print(f"La division es: {div}")