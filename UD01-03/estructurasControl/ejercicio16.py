"""Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene
"""
"""
n = input("Dame un número entre 0 y 99999: ")
len(n)
print(n)
"""

n = int(input("Dame un número entre 0 y 99999: "))
contador = 1

if n == 0:
    contador = 1
else:
    
    while n > 0:
        contador += 1
        n = n // 10 

    print(f"El número tiene {contador} cifras")