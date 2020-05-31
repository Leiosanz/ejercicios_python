#Ejercicio 1:

total=0

for x in range(101):
	total+=x

print("Sumatoria total:", total)

#Ejercicio 2:

total=0
for x in range(101):
	if x%3 ==0:
		total+=x
print("Sumatoria total:", total)		

#Ejercicio 3:

numero=int(input("entero positivo:"))
f=1
if numero !=0:
	for x in range(1, numero+1):
		f=f*x
	
print("factorial:", f)	

#Ejercicio 4:

Total=0
Total1=1

print(Total)
print(Total1)
for x in range (8):
	Total2=Total+Total1
	print(Total2)
	Total=Total1
	Total1=Total2
	

