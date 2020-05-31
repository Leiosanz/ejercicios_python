comprobar = 2
while comprobar == 2:

	N= int(input("Ingrese un numero positivo entero: "))
	if N > 0:
		comprobar = 1

		resultado=0
		
		for i in range(1,N+1):
			resultado = resultado + (1/i)

		print("El resultado final es: ", resultado)





	else:
		print("El numero es negativo. Intentelo de nuevo")