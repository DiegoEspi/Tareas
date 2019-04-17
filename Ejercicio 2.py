# Ejercicio N°2
n = input("Ingrese numero departamento: ")
n = list(n)
if 3 < len(n) < 5:
    n = input("Ingrese numero departamento: ")
    n = list(n)
    p = 0
    m = int(n[3])
    if n[0] == "2":
        p = (400)
    elif n[0] == "0" and n[1] == "1":
        p = (100)
    elif m == 3 or m == 7:
        p = 250 + (250*15/100)
    elif m == 0 or m == 4:
        p = 250 - (250*20/100)
    elif m == 1 or m == 2 or m == 5 or m == 6:
        p = 250
    print ("El precio es ",p)
else:
    print ("Numero invalido")
