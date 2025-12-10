"""
*********
* *   * *
*  * *  *
*   *   *
*       *
*   *   *
*  * *  *
* *   * *
*********
"""

a = int(input("Dime la altura de la figura, debe ser un numero impar: "))

if a % 2 == 0:
    exit()

for i in range(a//2 +1):
    if i == 0:
        print("*" * a)
    elif i == (a//2):
        print("*" + " " * (a-2) + "*")
    elif i == (a//2)-1:
        print("*" + " " * i + "*" +  " " * i + "*")
    else:
        print("*" + " " * i + "*" + " " * (a-2*i-4) + "*" + " " * i + "*")

for i in range(a//2-1,-1,-1):
    if i == 0:
        print("*" * a)
    elif i == (a//2)-1:
        print("*" + " " * i + "*" +  " " * i + "*")
    else:
        print("*" + " " * i + "*" + " " * (a-2*i-4) + "*" + " " * i + "*")
