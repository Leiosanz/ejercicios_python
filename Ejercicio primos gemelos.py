
comprobar=True
while comprobar == True:
	n1=int(input("Ingrese un numero entero positivo:"))
	n2=int(input("Ingrese un numero entero positivo:"))
	a=0
	if n1>0 and n2>0 and n1!=n2:
		comprobar=False
		if n1>n2:
			n1^=n2
			n2^=n1
			n1^=n2

		for i in range(n1,n2):
			creciente=2
			es_Primo= True

			while es_Primo and creciente<i:
				if i%creciente ==0:
					es_Primo=False

				else:
					creciente+=1

			if es_Primo and not a:
				a=i

			elif es_Primo and a:
				b=i

				if b-a==2:
			   		print(a,"y",b,"son numeros primos gemelos")

				a=i
			

	else:
		if n1==n2:
			print("Los numeros son iguales, intentelo de nuevo")

		else:
			print("Los numeros ingresados son incorrectos, intentelo nuevamente")


	

