"""
   *
  ***
 *****
*******
 *****
  ***
   *
"""

altura = int(input("Dime la altura: "))

for i in range (altura):
    if i == altura:
        print(" " * (altura -i) + "*")
    else:
        print(" " * (altura -1 -i) + "*" * (2 * i + 1))
        
for i in range (altura -2, -1, -1):
    if i == altura:
        print(" " * (altura -i) + "*")
    else:
        print(" " * (altura -1 -i) + "*" * (2 * i + 1))