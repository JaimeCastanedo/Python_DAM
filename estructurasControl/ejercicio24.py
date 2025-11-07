"""Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
Visualizar el descuento y el total a pagar por la compra
"""

total = float(input("Dime el monto de compra: "))
dia = int(input("Si el dia de la semana es martes o jueves presione el 1, sino el 2: "))

if dia == 1:
    total = total - (total * 0.15)

print("El precio total a pagar es: ", total)
