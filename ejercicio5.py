'''Bucles y Funciones
Ejercicios nivel básico

 1. Crea una función para verificar si un número es par o impar y devuelva “El 
número es par” o “El número es impar” según corresponda.

 pythonCopy code 
 
def es_par(numero): return numero % 2 == 0 num = int(input("Ingresa un número: ")) ife
 s_par(num): print("Es un número par.") else: print("Es un número impar.") '''
 
 
'''2. Crea una función a la que pases un número como argumento, calcule el factorial 
de ese número y haga print del resultado.

 pythonCopy code 
 
def factorial(numero): resultado = 1 for i in range(1, numero+1): resultado *= i retur
 nresultado num = int(input("Ingresa un número: ")) print("El factorial de", num, "e
 s:", factorial(num)) '''
 
 
'''3. Crea una función a la que se le pase un número como argumento, calcule la 
cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado 
total de dígitos.

 PISTA: Para convertir un número a string usa el método str(). Te recordamos que 
para saber la longitud de una cadena utilizamos len()

 pythonCopy code 
 
def contar_digitos(numero): return len(str(numero)) num = int(input("Ingresa un númer
 o: ")) print("La cantidad de dígitos es:", contar_digitos(num)) '''


'''4. Dada una lista de números, crea una función que devuelva el número máximo 
de la lista.

 pythonCopy code 
 
def encontrar_maximo(lista): maximo = lista[0] for numero in lista: if numero > maxim
 o: maximo = numero return maximo numeros = [5, 12, 3, 8, 9] print("El número máximo e
 s:", encontrar_maximo(numeros)) '''


'''5. Crea una función que, dado un número, sume los dígitos de ese número y 
devuelva el resultado.

 pythonCopy code 
 
def sumar_digitos(numero): suma = 0 while numero > 0: suma += numero % 10 numero //= 1
 0return suma num = int(input("Ingresa un número: ")) print("La suma de los dígitos e
 s:", sumar_digitos(num)) '''



'''6. Dados dos números, crea una función para encontrar el mínimo común múltiplo 
(MCM) de los dos números, que se les pasarán como argumento a la función, y 
devuelva el MCM.

 pythonCopy code 
 
def mcm(a, b): if a == 0 or b == 0: return 0 else: maximo = max(a, b) while True: ifma
 ximo % a == 0 and maximo % b == 0: return maximo maximo += 1 num1 = int(input("Ingrese 
el primer número: ")) num2 = int(input("Ingrese el segundo número: ")) print("El MCM e
 s:", mcm(num1, num2)) '''
 
 
 
'''7. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el 
área de un triángulo.

 pythonCopy code 
 
def calcular_area_triangulo(base, altura): return (base * altura) / 2 base = float(inp
 ut("Ingrese la base del triángulo: ")) altura = float(input("Ingrese la altura del tri
 ángulo: ")) print("El área del triángulo es:", calcular_area_triangulo(base, altura)) '''
 
'''8. Crea una función que, dado un número, verifique si un número es positivo, 
negativo o cero.

 pythonCopy code 
 
def verificar_signo(num): if num > 0: return "positivo" elif num < 0: return "negativ
 o"else: return "cero" num = float(input("Ingresa un número: ")) print("El número es:", 
verificar_signo(num)) '''


'''9. Crea una función que, dada una palabra, cuente la cantidad de letras en una 
palabra.

 pythonCopy code 
 
def contar_letras(palabra): contador = 0 for letra in palabra: if letra.isalpha(): con
 tador += 1 return contador palabra = input("Ingresa una palabra: ") print("La cantidad 
de letras es:", contar_letras(palabra)) '''



'''10. Crea una función que, dada una lista de números, convierta la lista de números 
a su valor absoluto.

pythonCopy code 

def valor_absoluto(lista): for i in range(len(lista)): lista[i] = abs(lista[i]) return
 lista numeros = [5, -12, 3, -8, 9] print("Lista con valores absolutos:", valor_absolut
 o(numeros)) '''
 
 
'''11. Crea una función que, dado un número, verifique si un número es primo.

 pythonCopy code 
 
def es_primo(numero): if numero <= 1: return False for i in range(2, numero): if numer
 o % i == 0: return False return True num = int(input("Ingresa un número: ")) ifes_prim
 o(num): print("Es un número primo.") else: print("No es un número primo.") '''



'''12. Dados dos números, crea una función para encontrar el máximo común divisor 
(MCD) de esos dos números.
 pythonCopy code...'''
'''def mcd(a, b): 
 while b: a, b = b, a % b 
 return a num1 = int(input("Ingresa el primer número: ")) 
num2 = int(input("Ingresa el segundo número: ")) 
print("El MCD es:", mcd(num1, num2)) '''