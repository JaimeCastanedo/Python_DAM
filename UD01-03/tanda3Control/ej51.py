"""
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 euros, el
segundo 20 euros, el tercero 40 euros y así sucesivamente. Realizar un algoritmo para
determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses
"""

total = 1

for i in range(20):
    if total == 1:
        total *= 10
        total_pago = 10
    else:
        total *= 2
        total_pago += total
    print(f"{total} el {i+1}º mes")
print(f"El total a pagar de todos los meses es: {total_pago}€")