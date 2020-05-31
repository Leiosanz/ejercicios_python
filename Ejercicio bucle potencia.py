

comprobar=True
while comprobar==True:


	n=int(input("Ingresa un numero entero:"))

	
	if n>0:

		comprobar=False
		resultado=0

		for i in range (1, n+1):

			if i%2 ==0:
				resultado-=i**i

			else:
				resultado+=i**i


		print("El resultado de la serie es:", resultado)


	else:
		 ("El numero ingresado no es correcto, intentelo nuevamente:")
