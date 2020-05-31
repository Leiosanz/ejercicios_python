# #Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print("¡Hola Mundo!")

# #Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla 
#el contenido de la variable.

X="¡Hola Mundo!"
print(X)


# #Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario 
# lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario
# haya introducido.

N=input("Nombre:")
print("¡Hola",  N + "!")


# #Ejercicio 4
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima 
#por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre=input("Nombre:")
n=input("Número:") 
print((nombre + "\n") * int(n))


# Ejercicio 5
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario 
#lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario 
#en mayúsculas y <n> es el número de letras que tienen el nombre.

Nombre=input("introduce el nombre:")
print(Nombre.upper() , "tiene" , (len(Nombre)), "letras")



# Ejercicio 6
# Escribir un programa que realice la siguiente operación aritmética (3+22⋅5)2.

Calculo=((3+2)/(2*5))**2
print(Calculo)


# Ejercicio 7
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.


Horas=float(input("Horas trabajadas:"))
Coste=float(input("coste hora:"))
Paga=float(Horas*Coste)
print(Paga)


# Ejercicio 8
# Escribir un programa que lea un entero positivo, 𝑛, introducido por el usuario y después muestre en 
#pantalla la suma de todos los enteros desde 1 hasta 𝑛. La suma de los 𝑛 primeros enteros positivos puede 
#ser calculada de la siguiente forma:

# suma=𝑛(𝑛+1)2



# Ejercicio 9
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de 
#masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal 
#es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

P=float(input("Ingresa tu peso:"))
E=float(input("Ingresa tu estatura:"))
IMC=float(P/E)

print("Tu indice de masa corporal es:", float(IMC) , "imc"),

# Ejercicio 10
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da 
#un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> 
#son el cociente y el resto de la división entera respectivamente.

n=int(input("Numero entero:"))
m=int(input("Numero entero:"))
c=int(n//m)
r=int(n%m)
print("La", n , "entre la" , m ,"da un cociente de" , c , "y un resto de" , r)


# Ejercicio 11
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de 
# años, y muestre por pantalla el capital obtenido en la inversión.

C=float(input("Cantidad a invertir:"))
I=float(input("Interes anual:"))
A=int(input("Numero de años:"))
Ca=C*I*A
print("El capital obtenido para la inversion es:", Ca, "€")

# Ejercicio 12
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por 
#correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de 
#los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
#Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el 
#peso total del paquete que será enviado.

P=int(input("Cantidad de payasos:"))
M=int(input("Cantidad de muñecas:"))
S=P+M
pesop=float(P*112)
pesom=float(M*75)
Peso=pesop+pesom


print("Cantidad de payasos y muñecas vendidas:", S, "unidades")
print("Su peso total es", Peso, "kg")


# Ejercicio 13
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
#Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final 
#de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en 
#la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por 
#pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos 
#decimales.

C=float(input("Cantidad de dinero ca:"))

primer=float(C*1+0.4)
segundo=float(primer*1+0.4)
tercero=float(segundo*1+0.4)

print("la cantidad de ahorros en el primer año fue de", (round(primer, 2)), "€")
print("la cantidad de ahorros en el segundo año fue de", (round(segundo,2)), "€")
print("la cantidad de ahorros en el tercer año fue de" , (round(tercero, 2)), "€")


# Ejercicio 14
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el 
#programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser 
#fresca y el coste final total.

Bv=int(input("Ingrese numero de barras que no son del dia:"))

Preciobarra=3.49
Preciobarravieja=3.49*0.6
Descuento=60
Total=Preciobarra-Preciobarravieja


print("el precio de una barra de pan es de:", Preciobarra, "€")
print("el descuento por ser vieja es de ", Descuento, "%")
print("Coste final es:", float(Bv*Total), "€")

