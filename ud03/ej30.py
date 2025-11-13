"""Dibuja un ordinograma de un programa que dada una cantidad de euros que el usuario
introduce por teclado (múltiplo de 5 €) mostrará los billetes de cada tipo que serán necesarios
para alcanzar dicha cantidad (utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar
el mínimo de billetes posible. Por ejemplo, si el usuario introduce 145 el programa indicará que
será necesario 1 billete de 100 €, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo
29 billetes de 5, que aunque sume 145 € no es el mínimo número de billetes posible)
"""


print("Introduce una cantidad múltiplo de 5 €")

cantidad = int(input("Cantidad en euros: "))

if cantidad % 5 != 0:
    print("Error: La cantidad debe ser múltiplo de 5 €")
else:
    billetes_500 = 0
    billetes_200 = 0
    billetes_100 = 0
    billetes_50 = 0
    billetes_20 = 0
    billetes_10 = 0
    billetes_5 = 0
    
    # billetes de 500
    if cantidad >= 500:
        billetes_500 = cantidad // 500
        cantidad = cantidad % 500
    
    # billetes de 200
    if cantidad >= 200:
        billetes_200 = cantidad // 200
        cantidad = cantidad % 200
    
    # billetes de 100
    if cantidad >= 100:
        billetes_100 = cantidad // 100
        cantidad = cantidad % 100
    
    # billetes de 50
    if cantidad >= 50:
        billetes_50 = cantidad // 50
        cantidad = cantidad % 50
    
    # billetes de 20
    if cantidad >= 20:
        billetes_20 = cantidad // 20
        cantidad = cantidad % 20
    
    # billetes de 10
    if cantidad >= 10:
        billetes_10 = cantidad // 10
        cantidad = cantidad % 10
    
    # billetes de 5
    if cantidad >= 5:
        billetes_5 = cantidad // 5
        cantidad = cantidad % 5
    

    print("\nBILLETES NECESARIOS:")
    
    if billetes_500 > 0:
        print(f"{billetes_500} billete(s) de 500 €")
    
    if billetes_200 > 0:
        print(f"{billetes_200} billete(s) de 200 €")
    
    if billetes_100 > 0:
        print(f"{billetes_100} billete(s) de 100 €")
    
    if billetes_50 > 0:
        print(f"{billetes_50} billete(s) de 50 €")
    
    if billetes_20 > 0:
        print(f"{billetes_20} billete(s) de 20 €")
    
    if billetes_10 > 0:
        print(f"{billetes_10} billete(s) de 10 €")
    
    if billetes_5 > 0:
        print(f"{billetes_5} billete(s) de 5 €")
    

    if cantidad == 0:
        print("\n¡Cantidad completada correctamente!")
    else:
        print(f"\nError: Quedan {cantidad} € sin asignar")