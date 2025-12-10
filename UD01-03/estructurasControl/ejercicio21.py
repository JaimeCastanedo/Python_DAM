"""Escriba un programa que calcula el salario neto semanal de un trabajador en función del
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
• Las primeras 35 horas se pagan a tarifa normal.
• Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
• Las tasas de impuesto son:
o Los primeros 500€ son libres de impuestos.
o Los siguientes 400€ tiene un 25% de impuesto.
o Los restantes un 45% de impuesto.
Escribe el nombre del trabajador, salario bruto, tasas y salario neto.
"""

nombre = input("Dime tu nombre: ")
horasTrabajadas = int(input("Dime las horas que has trabajado: "))
tarifa = float(input("Dime la tarifa que tienes"))

pagar = 0
bolsillo = 0

if horasTrabajadas<=35:
    pagar = pagar + (horasTrabajadas*tarifa)
else:
    pagar = pagar + (horasTrabajadas*tarifa)
    horasTrabajadas = horasTrabajadas-35
    pagar = pagar + (horasTrabajadas * (tarifa * 1.5))

if pagar < 500:
    bolsillo = pagar
else:
    bolsillo = bolsillo+500
    pagar = pagar-500
    if pagar<400:
        bolsilo = bolsillo+(pagar-pagar*0.25)
    else:
        bolsillo = bolsillo+(400*0.25)
        pagar = pagar-400
        bolsillo=bolsillo+(pagar-0.45)
        
print(bolsillo)