''' Funciones
1. Ejercicio: Define una función que tome dos números y retorne su suma. 

2. Ejercicio: Defineuna función que tome un número y retorne su factorial. 

3. Ejercicio: Define una función que tome un número y determine si es primo. 

4. Ejercicio: Define una función que reciba una lista de números y retorne la suma 
de ellos. 

5. Ejercicio: Define una función que reciba una cadena de texto y retorne la 
cadena en reversa. '''

# 1
def suma (a, b):
  return a + b
print (suma (10,5))


# 2
import math
def factorial (a):
  return a
print(math.factorial(8))

# 3
def primo (num):
  esPrimo = True
  for i in range(2, num):
    if(num % i == 0):
      esPrimo = False
      return
    return esPrimo
print(primo(5))


#4 
lista = {}


def lista(numeros):
  suma = 0
  for numero in numeros:
      suma += numero
  return suma

listaNumeros =[2,5,78,63,4]
print(lista(listaNumeros))


# 5
texto = "hola mundo que tal?"
cadena_invertida = texto[::-1]
print(cadena_invertida)