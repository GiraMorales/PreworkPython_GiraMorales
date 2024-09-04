''' Condicionales
1. Ejercicio: Dado un número, imprime si es positivo o negativo. 
2. Ejercicio: Dado un número, imprime si es par o impar. 
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos. '''

nombre = -5

if (nombre>0):
  print("el nuemro es positivo")
elif (nombre<0):
  print("el numero es negativo")
  
  
if(nombre % 2 == 0):
    print("El numero es par")
else:
    print("El numero es impar")
    

n1 = 2
n2 = 10
n3 = 8


if n1 > n2 and n1 > n3:
    print("el numero mayor es: ",n1)
elif n2 > n1 and n2 > n3:
    print("el numero mayor es: ",n2)
elif n3 > n1 and n3 > n2:
    print("el numero mayor es: ",n3)
else:
    print("no se pudo establecer el mayor")


