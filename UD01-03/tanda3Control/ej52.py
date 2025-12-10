"""
Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule
cuánto pagó la empresa por los N empleados.
"""

horasSemanales = int(input("Dime las horas que ha trabajado esta semana: "))
trabajadores = int(input("Dime la cantidad de empleados que han trabajado esas horas: "))
pagoHora = int(input("Dime cuanto se le paga a cada trabajador la hora: "))

pagoTotal = pagoHora * horasSemanales
print(f"Los trabajadores ganarán: {pagoTotal}€ a la semana")

pagoTotal = pagoTotal *trabajadores
print(f"En total, la empresa deberá pagar: {pagoTotal}€ a los trabajadores")