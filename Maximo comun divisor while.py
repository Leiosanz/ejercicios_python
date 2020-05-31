#Construye un programa que calcule el máximo comun divisor (MCD) de los números naturales N1 y N2.
#El MCD entre dos números es el natural más grande que divide a ambos.

#Si el usuario escribe un número incorrecto, el programa no se ejecuta. En cambio, pregunta de nuevo por 
#la información hasta que el dato ingresado sea correcto.

comprobar=True

while comprobar:

	a=int(input("Ingrese el primer número:"))
	b=int(input("Ingrese el segundo número:"))

	MCD= False

	if a>0 and b>0 and a!=b:

		comprobar=False

		if b<a:
			aux=a
			a=b
			b=aux

		i=a

		while MCD== False and i >=1:

			if a%i==0 and b%i==0:
				print("El MCD es", i)
				MCD=True

			else:

				i-=1	


	else:

		if a==b:
			print("Los números son iguales. Inténtelo nuevamente.")

		else:
			print("Los números son incorrectos. Inténtelo nuevamente.")