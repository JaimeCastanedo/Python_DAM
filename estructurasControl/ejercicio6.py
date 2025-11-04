"""Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre
el porcentaje de descuento realizado
"""

precioA = float(input("Dame el lado del precio del articulo: "))
precioV = float(input("Dame el lado del precio de venta real: "))

porc = (1-(precioV/precioA)) *100

print(round(porc), "%")
