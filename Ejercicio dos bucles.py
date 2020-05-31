#EJERCICIO 2

#Pedir números al usuario hasta que introduzca uno negativo. Al finalizar mostrar la cantidad de números 
#introducidos sin contar el negativo.

numero=0
contador=0

while numero>=0:

	numero=int(input("Introduce un numero: "))
	contador= contador + 1

contador= contador -1

print("Se han introducido", contador, "numeros")
	



