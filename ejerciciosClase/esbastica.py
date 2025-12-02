a = int(input("Introduce a la altura: "))

for i in range(a):
    if i == 0:
        print("#" + "  " * (a - 1) + "#" + "#" * (a * 2))
    elif i == a - 1:
        print("#" * a * 4)
    else:
        print("#" + "  " * (a - 1) + "#")
    
for i in range(a):
    if i == (a - 1):
        print("#" * (a * 2 + 1) + "  " * (a - 1) + "#")
    else:
        print("  " * (a) + "#" + "  " * (a - 1) + "#")