#pedir dos numeros por teclado y mostrar todos los numeros pares comprendidos entre ambos.

numero1=int(input("Ingrese un numero: "))
numero2=numero1
while numero2<=numero1:
	numero2=int(input("Ingrese otro numero: "))
 
if numero1 > 0 and numero2 > 0 and numero1 != numero2:
	
	for i in range(numero1,numero2):
		if i%2 == 0:
			print(i)

		

	

