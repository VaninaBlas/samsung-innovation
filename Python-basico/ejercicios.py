#%%
#ejercicio 1
num=int(input("Ingresa un numero: "))
if(num<0):
  print("El numero es negativo")
else:
  print("El numero es positivo")

#%%
#ejercicio 2
num= int(input("Ingresa un valor: "))
if(num%2==0):
 print("Es par")
else:
 print("es impar")

#%%
#ejercicio 3
radio=float(input("Ingresa el radio: "))
perim = 2 * 3.14 * radio
super= 3.14 * (radio**2)
print("Superficie: ", super)
print("Perimetro: ", perim)

# %%
#ejercico 4
mayor=0
menor= 99999
for i in range(10):
 valor= int(input("Ingresa el valor: "))
 if(valor>mayor):
    mayor=valor
 elif(valor<menor):
    menor=valor
print("Mayor: ", mayor)
print("Menor: ", menor)

#%%
#ejercicio 5
cant= int(input("Ingresar la cantidad de solicitudes: "))
suma=0
resta=0
multi=1
for i in range(cant):
  num=float(input("Ingresar el numero: "))
  suma=suma+num
  if(i==0):
    resta=num
  else:
    resta-=num
  multi=multi*num

promedio=suma/cant
2
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multi)
print("Promedio:", promedio)

# %%
#ejercicio 6
usuario=input("Ingresar el usuario: ")
contra= input("Ingresar la contraseña: ")
if(usuario.lower()=="vanina" and contra.lower()=="vaniblas"):
  print("Bienvenida", usuario)
else:
  print("Datos incorrectos")

#%%
#ejercicio 7
suma=0
valor=1
while(valor!=0):
  valor=int(input("Ingresa un valor: "))
  suma=suma+valor
print("Suma: ", suma)

#%%
#ejercicio 8
lista=[]
for i in range(3):
  nombre=input("Ingresa tu nombre: ")
  lista.append(nombre)
print(lista)

#%%
#ejercicio 9
lista=[]
for i in range(3):
  nombre=input("Ingresa un nombre:")
  lista.append(nombre)
lista.sort()
print(lista)
