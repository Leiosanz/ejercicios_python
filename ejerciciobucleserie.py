comprobar = "que te follen"
while comprobar == "que te follen":
	n=int(input("Ingrese un numero entero positivo: "))
	if n > 0:
		resultado=1

		for i in range(1,n+1):
			if i % 2 == 0:
				resultado = resultado / (1/i)

			else:
				resultado*= 1/i

		print("El resultado de la serie es: ", resultado)

		comprobar= "que te den"



	else:
		print("el numero es incorrecto, intentelo nuevamente")

