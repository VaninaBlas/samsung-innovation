#%%
# Ejercicio 1
numeros= input("Ingrese una lista de numeros separados por espacios: ")
lista=numeros.split(" ")
def burbuja(arreglo):
    longitud = len(arreglo)
    for i in range(longitud):
        for indice_actual in range(longitud - 1):
            indice_siguiente_elemento = indice_actual + 1
            if arreglo[indice_actual] > arreglo[indice_siguiente_elemento]:
                arreglo[indice_siguiente_elemento], arreglo[indice_actual] = arreglo[indice_actual], arreglo[indice_siguiente_elemento]

print("Original: ")
print(lista)
burbuja(lista)
print("Ordenado: ")
print(lista)

#%%
# Ejercicio 2
palabras=input("Ingrese una lista de palabras separadas por espacios: ")
lista=palabras.split(" ")
lista.sort()
print(lista)
#%%
# Ejercicio 3
def insertion_sort(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_actual

numeros= input("Ingresa 8 numeros enteros separados por espacios: ")
elementos=numeros.split(" ")
error= False
try:
    lista = [int(num) for num in elementos]
except ValueError:
    print("Error: Asegúrese de ingresar solo números enteros.")
    error= True

if(error==False):
  insertion_sort(lista)
  print("Lista ordenada:", lista)
#%%
# Ejercicio 4
def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

numeros= input("Ingresa 8 numeros enteros separados por espacios: ")
elementos=numeros.split(" ")
error= False
try:
    lista = [int(num) for num in elementos]
except ValueError:
    print("Error: Asegúrese de ingresar solo números enteros.")
    error= True

if(error==False):
  selection_sort(lista)
  print("Lista ordenada:", lista)
#%%
# Ejercicio 5
def busqueda_lineal(lista, objetivo):
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False

# Ejemplo de uso
numeros = [3, 5, -1, 8, 2, 0, 4, 7]
objetivo = 5

if busqueda_lineal(numeros, objetivo):
    print("El valor", objetivo, "está en la lista.")
else:
    print("El valor", objetivo, "no está en la lista.")
#%%
# Ejercicio 6
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] > objetivo:
            fin = medio - 1
        else:
            inicio = medio + 1
    return False

numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
objetivo = 13

if busqueda_binaria(numeros, objetivo):
    print("El valor", objetivo, "está en la lista.")
else:
    print("El valor", objetivo, "no está en la lista.")
#%%
# Ejercicio 7
numeros = input("Ingrese una lista de números separados por espacios: ")
lista = [int(num) for num in numeros.split()]
objetivo = int(input("Ingrese el número que desea buscar en la lista: "))
try:
    indice = lista.index(objetivo)
    print(f"El índice de la primera aparición de {objetivo} es: {indice}")
except ValueError:
    print(f"El número {objetivo} no se encuentra en la lista.")
#%%
# Ejercicio 8
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

def buscar_objeto_por_atributo(lista, atributo, valor_objetivo):
    for objeto in lista:
        if hasattr(objeto, atributo) and getattr(objeto, atributo) == valor_objetivo:
            return True
    return False

productos = [
    Producto("Manzana", 1.5),
    Producto("Banana", 1.0),
    Producto("Naranja", 1.2)
]

valor_objetivo = 1.0
resultado = buscar_objeto_por_atributo(productos, 'precio', valor_objetivo)

if resultado:
    print(f"Se encontró un producto con precio {valor_objetivo}.")
else:
    print(f"No se encontró ningún producto con precio {valor_objetivo}.")
#%%