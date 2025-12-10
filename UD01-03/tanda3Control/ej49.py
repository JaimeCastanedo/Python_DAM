"""
Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la
semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por
las horas trabajadas.
"""

sueldo_por_hora = 9
total_horas = 0

for i in range (6):
    horas = int(input(f"Dime las horas que has trabajado el dia {i+1}: "))
    total_horas = total_horas + horas
    total_sueldo = sueldo_por_hora * total_horas
print(f"El total de horas que ha trabajado es: {total_horas} que equivale a pagarle {total_sueldo}€")