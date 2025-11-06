"""Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
incorrecto
"""

nom = input("Dime el nombre de usuario para crearlo: ")
con = input("Dime la contraseña: ")

nom2 = input("Dime el usuario: ")
con2 = input("Dime la contraseña: ")

if nom == nom2 and con == con2:
    print("Inicio de sesion confirmado")
elif nom != nom2 and con == con2:
    print("El usuario no coincide")
elif con != con2 and nom == nom2:
    print("La contraseña no coincide")
else:
    print("No has acertado ni el nombre ni la contraseña")