n=int(input("Ingrese un numero entero positivo: "))
if n > 0:

	for i in range(2,n):
		creciente=2
		primo= True

		while primo == True and creciente < i:
			
			if i % creciente ==0:
				primo = False

			else:
				creciente += 1
	
		if primo:
			print(i, "es primo")

	
else:
	print("Numero incorrecto, intentelo de nuevo")

