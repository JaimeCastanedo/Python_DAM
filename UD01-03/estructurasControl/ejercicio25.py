"""La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
control switch).
"""
nombre = input("Dime tu nombre: ")

facul = int(input("Dime la facultad en la que vas a estudiar: \n"
              "1.- Ing. de Sistemas\n"
              "2.- Derecho\n"
              "3.- Ing. Naviera\n"
              "4.- Ing. Pesquera\n"
              "5.- Contabilidad\n"
              "6.- Administracion\n"))

match facul:
    case 1:
        igv = (350 + 650) * 0,18
        monto = (350 + 650) - igv
        
        print(f"Nombre: {nombre}\n"
              "Facultad: Ing. de Sistemas"
              "Importe: 350\n"
              "Mensualidad: 650\n"
              "IGV: {igv}"
              "Monto: {monto}")
    
    case 2:
        igv = (300 + 550) * 0,18
        monto = (300 + 550) - igv
        
        print(f"Nombre: {nombre}\n"
              "Facultad: Derecho"
              "Importe: 300\n"
              "Mensualidad: 550\n"
              "IGV: {igv}"
              "Monto: {monto}")
    
    case 3:
        igv = (300 + 500) * 0,18
        monto = (300 + 500) - igv
        
        print(f"Nombre: {nombre}\n"
              "Facultad: Ing. Naviera"
              "Importe: 300\n"
              "Mensualidad: 500\n"
              "IGV: {igv}"
              "Monto: {monto}")
        
    case 4:
        igv = (310 + 460) * 0,18
        monto = (310 + 460) - igv
        
        print(f"Nombre: {nombre}\n"
              "Facultad: Ing. Pesquera"
              "Importe: 310\n"
              "Mensualidad: 460\n"
              "IGV: {igv}"
              "Monto: {monto}")
        
    case 5:
        igv = (280 + 490) * 0,18
        monto = (280 + 490) - igv
        
        print(f"Nombre: {nombre}\n"
              "Facultad: Contabilidad"
              "Importe: 280\n"
              "Mensualidad: 490\n"
              "IGV: {igv}"
              "Monto: {monto}")

    case 6:
        igv = (360 + 520) * 0,18
        monto = (360 + 520) - igv
        
        print(f"Nombre: {nombre}\n"
              "Facultad: Administracion"
              "Importe: 360\n"
              "Mensualidad: 520\n"
              "IGV: {igv}"
              "Monto: {monto}")
    
    case _:
        print("No es una opcion valida")