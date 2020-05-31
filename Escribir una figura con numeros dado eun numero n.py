#Construye un programa que , al recibir como dato un numero entero positivo, escriba una figura como la que
#se muestra a continuación (elemplo para N=6)


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

comprobar=True

while comprobar:

	n=int(input("Ingresa un número entero positivo: "))

	if n>0:

		comprobar= False

		for i in range (1,n+1):
			print(" ")

			for j in range (1, i+1):
				print(j, end= " ")

		for i in range (n-1, 0, -1):
			print(" ")	

			for j in range(1, i+1):
				print(j, end=" ")	


	else:
		print("El número ingresado es incorrecto. Inténtelo nuevamente")