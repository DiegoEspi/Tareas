# Ejercicio N°3
a=float(input("ingrese angulo 1: "))
b=float(input("ingrese angulo 2: "))
c=180-(a+b)
if a==90 or b==90 or c==90:
    print("es un triangulo rectangulo")
elif a>90 or b>90 or c>90:
    print("es un triangulo obtusangulo")
elif a<90 or b<90 or c<90:
    print("es un triangulo acutangulo")
else:
	print("Los angulos no son de un triangulo")
