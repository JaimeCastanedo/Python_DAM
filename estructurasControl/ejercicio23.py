"""Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
según sea el caso y el total a pagar de la compra.
"""

compra = int(input("Dime cual es el valor de tu cuenta: "))
opcion = 0

if opcion == 1:
    total = compra - (compra * 0.5)
if opcion == 2:
    total = compra + (compra * 0.3)

print(f"El pago tatal es: {total}€")
