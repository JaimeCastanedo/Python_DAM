"""
Diamante
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
   """

altura = int(input("Dime la altura del diamante: "))

print(" " * altura + "*")

for i in range (altura -2):
    print(" " * (altura -1 -i) + "*" + " " * (2*i + 1) + "*")
    
for i in range (altura -2, -1, -1):
    print(" " * (altura -1 -i) + "*" + " " * (2*i + 1) + "*")
    
print(" " * altura + "*")

"""

Opcion de clase:


a = 5
e = 1
for i in range(1, a+1):
    if i == 1:
        print(" " * (a-i), end="")
        print("*")
    else:
        print(" " * (a-i), end="*")
        e +=2
        print(" " * (i*2-e), end="*")

for i in range(a, 1, -1):
    if i == 1:
        print(" " * (a-i), end="")
        print("*")
    else:
        print(" " * (a-i), end="*")
        e -=2
        print(" " * (i*2-e), end="*")

"""