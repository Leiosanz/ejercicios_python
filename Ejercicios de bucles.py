# Ejercicio 1
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

i=input("Escribe una palabra:")

for i in range (10):
	print("Puto")


#OTRA MANERA:

for i in "leonardosa":
	print("Puto")

# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha 
# cumplido (desde 1 hasta su edad).


i=int(input("ingresa tu edad:"))

for i in range (1,i+1):
	print(i)

#OTRA MANERA:

i=int(input("ingresa tu edad:"))

for i in range (i):

	print(str(i+1))


# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los 
# números impares desde 1 hasta ese número separados por comas.

i=int(input("Escribe un numero entero positivo:"))

if i>0:
	for i in range (1, i+1, 2):
		print(i, end=",")

#OTRA MANERA:

i=int(input("Escribe un numero entero positivo:"))	

for i in range (1, i+1, 2):
	print(i, end=",")


# Ejercicio 4
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás
# desde ese número hasta cero separados por comas.

i=int(input("Escriba un numero entero positivo:"))

for i in range(i,-1,-1):
	print(i, end=",")

# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de 
# años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

	


# Ejercicio 6
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
# como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****



i=int(input("Escriba un numero entero:"))

for x in range(i):
	print("*"*(i+1))


# Ejercicio 7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.








# Ejercicio 8
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
# como el de más abajo.

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1







# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
# por la contraseña hasta que introduzca la contraseña correcta.










# Ejercicio 10
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o
# no.









# Ejercicio 11
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de
# la palabra introducida empezando por la última.


# Ejercicio 12
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
# el número de veces que aparece la letra en la frase.


# Ejercicio 13
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba
# “salir” que terminará.


