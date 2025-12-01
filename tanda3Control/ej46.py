"""
Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de
potencia.
"""
base = int(input("Dame la base: "))
exp = int(input("Dame el exponente: "))
total = 1

for i in range(exp):
    total = total * base
print(f"El resultado es: {total}")