# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

x=int(input("Ingresa tu edad:"))
if x>18:
	print("Soy mayor de edad")
else:
	print("soy menor de edad")	


# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
# por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la 
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

confirmacion="leo"

contraseña=input("Ingrese la contraseña:")
if confirmacion==contraseña.lower():
	print("coincide")

else:
	print("no coincide")	


# Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor 
# es cero el programa debe mostrar un error.

X=int(input("ingrese un numero:"))
Z=int(input("ingrese otro numero:"))

if Z==0:
	print("error")

# Ejercicio 4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

X=int(input("Ingrese un numero entero:"))

if X%2==0:
	print("El numero es par")

else:
	print("el numero es impar")	


# Ejercicio 5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o 
# superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos 
# mensuales y muestre por pantalla si el usuario tiene que tributar o no.

x=int(input("Ingrese su edad:"))
z=int(input("Ingrese sus ingresos mensuales:"))

if x > 16 and z >= 1000:
	print("puede tributar")

else:
	print("no puede tributar")



# Ejercicio 6
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo 
# A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la 
# N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre 
# por pantalla el grupo que le corresponde.

x=input("ingrese su nombre:")
z=input("ingrese su sexo:")

if (z=="m" and x.lower()<"m") or (x =="h" and x.lower()>"n"):
	print("pertenece al grupo A")

else:
	print("pertenece al grupo B")	


# Ejercicio 7
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 200000€ y 35000€	20%
# Entre 350000€ y 60000€	30%
# Más de 60000€	45%

# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo 
# que le corresponde.


Renta=float(input("Escriba su renta anual:"))

if Renta < 10000:
     impuesto = 5
elif Renta < 20000:
     impuesto = 15
elif Renta < 35000:
     impuesto = 20
elif Renta < 60000:
     impuesto = 30
else:
     impuesto = 45

print("Tu tipo impositivo es " + str(impuesto) + "%")

# Ejercicio 8
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden 
# obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. 
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios 
# entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada 
# puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación 
# del nivel.

# Nivel	Puntuación

# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más

# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la 
# cantidad de dinero que recibirá el usuario.

puntuacion=float(input("puntuacion:"))


Inaceptable=0.0
Aceptable=0.4
Meritorio=0.6


if puntuacion==0.0:
	print("Inaceptable y te corresponde", Inaceptable*2400, "€")

elif puntuacion==0.4:
	print("Aceptable y te corresponde", Aceptable*2400, "€")
elif puntuacion==0.6:
	print("Meritorio y te corresponde", Meritorio*2400, "€")
elif puntuacion > 0.6:
	print("Meritorio y te corresponde", puntuacion*2400, "€")


# Ejercicio 9
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular 
# de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar
# al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede
# entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

E=int(input("Ingesa tu edad:"))

if E<4:
	print("Puede entrar gratis")
elif E>=4<=18:
	print("debe pagar 5 euros")

else:
	print("debe pagar 10 euros")	


# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes 
# para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su
# respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un 
# ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar 
# por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

vegetariana="pimiento o tofu"
no_vegetariana="peperoni, jamon y salmon"


pizza=input("Elige el tipo de pizza:")

if pizza.lower()=="vegetariana":
	print(vegetariana)
	ingredientev=input("Elige entre pimiento o tofu:")
	print("Lleva mozzarella, tomate y", ingredientev)
	
elif pizza.lower()=="no vegetariana":
	print(no_vegetariana)
	ingredientenv=input("Elige entre peperoni, jamon y salmon:")
	print("Lleva mozarella, tomate y", ingredientenv)	

