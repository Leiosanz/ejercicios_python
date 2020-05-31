#EJERCICIO 1

#Pedir 10 numeros por teclado. Sumarlos y mostrar el resultado en pantalla.

suma=0
for n in range (0,10):
	numero=int(input("Introduce un numero:"))
	suma+=numero
print("La suma es", suma)	