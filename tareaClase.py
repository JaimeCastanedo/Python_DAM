"""        
    *
   **
  * *
 *  *
*   *
 *  *
  * *
   **
    * 
"""
    
altura = int(input("Dime la altura de la figura: "))


for i in range(altura):
    espacios = " " * (altura - i)
    if i == 0:
        print(espacios + "*")
    else:
        print(espacios + "*" + " " * (i - 1) + "*")

print("*" + " " * (altura -1) + "*")

for i in range(altura - 1, -1, -1):
    espacios = " " * (altura - i)
    if i == 0:
        print(espacios + "*")
    else:
        print(espacios + "*" + " " * (i - 1) + "*")