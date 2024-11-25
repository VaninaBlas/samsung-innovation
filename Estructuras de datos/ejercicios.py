##Listas

#%%
#ejercicio 1
frutas= ["manzana", "banana", "naranja", "pera"]
print(frutas)

#%%
#ejercicio 2
print(frutas[1])

#%%
#ejercicio 3
frutas[0]= "cereza"
print(frutas)

#%%
#ejercicio 4
frutas.append("sandia")
print(frutas)

#%%
#ejercicio 5
frutas.remove("naranja")
print(frutas)

# %%
#ejercicio 6
numeros=[3,4,2,1,5,2,2,1]
cant=len(numeros)
for i in range(cant):
  print(numeros[i])

# %%
#ejercicio 7
pares=[4,2,8,6,10]
invert=pares.reverse()
print(pares)
orden=pares.sort()
print(pares)

# %%
#ejercicio 8
cuadrados=[x**2 for x in range(1, 6)]
print(cuadrados)

#%%
#ejercicio 9
nombres=["vanina", "priscila", "jasmin"]
dato= input("Ingrese un nombre: ")
if dato.lower() in nombres:
  print("El nombre se encuentra en la lista")
else:
  print("El nombre no se encuentra en la lista")

#%%
#ejercicio 10
numeros=[1,2,3,4,5,6,7,8,9,10]
lista1=numeros[0:3]
lista2=numeros[3:6]
lista3=numeros[6:10]
print(lista1)
print(lista2)
print(lista3)

#Diccionarios
#%%
#ejercicio 1
alumno={"nombre": "Vanina", "edad": 18, "carerra": "Tecnologia Digital"}
print(alumno.values())

#%%
#ejercicio 2
alumno["edad"]=19
print(alumno.values())

#%%
#ejercicio 3
alumno.update({"universidad": "Di Tella"})
print(alumno.values())

# %%
#ejercicio 4
calificaciones={"matematicas": "9", "fisica": "7", "quimica": "10"}
for x,y in calificaciones.items():
  print(x,y)

#%%
#ejercicio 5
calificaciones.pop("quimica")
for x,y in calificaciones.items():
  print(x,y)

#%%
#ejercicio 6
print(calificaciones.keys())
print(calificaciones.values())

# %%
#ejercicio 7
agenda={
    "contacto1":{
      "nombre": "Vanina",
      "telefono": "1132675353",
      "email":"vanyabrilconblas@gmail.com"
    },

    "contacto2":{
      "nombre":"iliana",
      "telefono":"1156234533",
      "email":"ilianaduartesa@gmail.com"
    },

    "contacto3":{
        "nombre":"jasmin",
        "telefono":"1276823761",
        "email" : "jasmin@gmail.com"
    }
}
for x, obj in agenda.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

##Tuplas
# %%
#ejercicio 1
meses=("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
print(meses)

#%%
#ejercicio 2
print(meses[2])

#%%
#ejercicio 3
print(meses[-1])

#%%
#ejercicio 4
meses[0]="abril"
"""
TypeError: 'tuple' object does not support item assignment
las tuplas no se pueden modificar
"""

# %%
#ejercicio 5
tupla1=(18,19,20)
tupla2=("Vanina", "gatos", "bachata")
tupla_concatenada=tupla1+tupla2
print(tupla_concatenada)

#%%
#ejercicio 6
coordenadas=(2,5,7)
x,y,z=coordenadas
print(x)
print(y)
print(z)

#%%
#ejercicio 7
alumnos=[
    ("Vanina", 18)
    ,("Priscila", 18)
    ,("Jasmin", 18)
]
for x,y in alumnos:
  print(x,y)

#Sets
#%%
#ejercicio 1
frutas={"manzana", "banana", "naranja", "pera"}
print(frutas)

#%%
#ejercicio 2
fruta1= {"manzana", "banana", "pera"}
frutas2= {"naranja", "sandia"}
frutas_unidas= fruta1.union(frutas2)
print(frutas_unidas)
frutas_interseccion= fruta1.intersection(frutas2)
print(frutas_interseccion)
frutas_dif_f1= fruta1.difference(frutas2)
frutas_dif_f2= frutas2.difference(fruta1)
print(frutas_dif_f1 | frutas_dif_f2)

#%%
#ejercicio 3
numeros=set()
for i in range(1,6):
  numeros.add(i)
numeros.remove(3)
print(numeros)

# %%
#ejercicio 4
vocales={"a", "e", "i", "o", "u"}
dato=input("Ingrese una letra: ")
if dato.lower() in vocales:
  print("La letra se encuentra en las vocales")
else:
  print("La letra no se encuentra en las vocales")

#%%
#ejercicio 5
numeros_repetidos=(1,4,4,1,4,5,6,7,21,2,3,4,343,5,6,3,4,7,2,6,5)
numeros_unicos=set(numeros_repetidos)
numeros=list(numeros_unicos)
print(numeros)

#%%
#ejercicio 6
set1={1,2,3,4,5}
set2={4,5,6,7,8}
diferencia_simetrica=set1.symmetric_difference(set2)
print("Diferencia simetrica:", diferencia_simetrica)
es_subconjunto= set1.issubset(set2)
print("Set 1 es subconjunto de set 2?", es_subconjunto)
es_conjunto_propio= set2.issubset(set1) and set2 != set1
print("set 2 es subconjunto propio de set 1?",es_conjunto_propio)

#%%
#ejercicio 7
set_a={1,2,4,6,7}
set_b={4,3,8,9,1}
set_a.difference_update(set_b)
print(set_a)