#%%
#Ejercicio 1
def saludo():
  print("Hola")
saludo()
saludo()

#%%
#Ejercicio 2
def saludo(nombre):
  print(f"Hola {nombre}!")
saludo("Vanina")
saludo("Priscila")
saludo("Jasmin")

#%%
#Ejercicio 3
def suma(num1, num2):
  return num1 + num2

rta= suma(10, 20)
print(rta)
rta= suma(15, 0)
print(rta)
rta= suma(1, 1)
print(rta)

#%%
#Ejercicio 4
def saludo_personalizado(nombre, saludo="Hola"):
  print(f"{saludo} {nombre}!")
saludo_personalizado("Vanina")
saludo_personalizado("Vanina", "Buen día")

#%%
#Ejercicio 5
def promedio(lista):
  suma=0
  for i in lista:
    suma=suma+i
  return suma/len(lista)
rt= promedio([1,2,3,4])
print(rt)
rt= promedio([10,5,5,3])
print(rt)
rt= promedio([1,2,6,19])
print(rt)

#%%
#Ejercicio 6
def factorial(numero):
  if(numero<=1):
    return 1
  return numero * factorial(numero-1)

rt=factorial(5)
print(rt)
rt=factorial(1)
print(rt)
rt=factorial(0)
print(rt)
rt=factorial(10)
print(rt)

#%%
#ejercicio 7
def ordenar_lista(lista):
  lista.sort()
  return lista
rt= ordenar_lista([1,2,3,4])
print(rt)
rt= ordenar_lista([10,5,5,3])
print(rt)
rt= ordenar_lista([8,2,6,1])
print(rt)

#%%
#ejercicio 8
def dividir(num1,num2):
  try:
    return num1/num2
  except ZeroDivisionError:
    print("No se puede dividir por cero")
rt= dividir(10,2)
print(rt)
dividir(10,0)
rt= dividir(20,4)
print(rt)

#%%
#ejercicio 9
def informacion_persona(nombre, edad, ciudad):
  print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

informacion_persona("Vanina", 21,"Buenos Aires")
informacion_persona("Iliana", 18,"Buenos Aires")

#%%
#ejercicio 10
def dividir(num1,num2):
  try:
    return num1/num2
  except ZeroDivisionError:
    print("No se puede dividir por cero")
rt= dividir(10,2)
print(rt)
dividir(10,0)
rt= dividir(20,4)
print(rt)

#%%
#ejercicio 11
def concatenar_strings(cadena):
  return " ".join(cadena)
concatenar_strings(["Vanina", "juega", "visual", "movil"])

#%%
#ejercicio 12
def eliminar_duplicados(lista):
  return list(set(lista))
eliminar_duplicados([1,5,3,3,3,45,6,7,8,8,8])

#%%
#ejercicio 13
def fibonacci(n):
  if n < 0:
      print("Numero incorrecto")
  elif n == 0:
      return 0
  elif(n == 1 or n == 2):
      return 1
  else:
      return fibonacci(n-1) + fibonacci(n-2)
fibonacci(10)

#%%
#ejercicio 14
import random
def generar_numero_aleatorio(start, finish):
  return random.randint(start,finish)
rt=generar_numero_aleatorio(1,10)
print(rt)
rt=generar_numero_aleatorio(10,20)
print(rt)
rt=generar_numero_aleatorio(20,30)
print(rt)

#%%
#ejercicio 15
def contar_lineas(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        return len(lineas)

with open("samsung.txt", 'w') as f:
    f.write("Esto es una prueba.\n")
    f.write("Son las 11 de  la noche.\n")
rt= contar_lineas("samsung.txt")
print(rt)
with open("escuela.txt", 'w') as f:
    f.write("Kittens\n")
    f.write("Old Prince\n")
    f.write("Machine Learning\n")
rt=contar_lineas("escuela.txt")
print(rt)

#%%
#ejercicio 16
def calcular_estadisticas(tupla):
  print(f"Suma:{sum(tupla)}")
  print(f"Promedio:{sum(tupla)/len(tupla)}")
  print(f"Mayor:{max(tupla)}")

print("primera tupla")
calcular_estadisticas((1,2,3,4))
print("segunda tupla")
calcular_estadisticas((10,5,5,3))
print("tercera tupla")
calcular_estadisticas((8,2,6,1))
