"""Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de 10
"""
n = input("Dime un numero: ")

if n%10 == 0:
    print("Es divisible por 10")
else:
    print("No es divisible por 10")