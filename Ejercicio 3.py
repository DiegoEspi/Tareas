Nombre=input("Ingrese el nombre del participante: ")
D=int(input("Ingrese la dificultad del piquero: "))
jueces=7
x=0
i=0
puntajes=[]
for i in range(0,jueces) :
    x=input("Ingrese puntaje del juez: ")
    puntajes.append(x)
puntajes.sort()
puntajes.remove[0]
puntajes.remove[6]
print (puntajes)