#%%
import pandas as pd
import matplotlib.pyplot as plt
#Ejercicio 1
data={"Año":[2015, 2016, 2017,2018,2019], "Ventas":[200,240,300,330,400]}

df= pd.DataFrame(data)

plt.plot(df["Año"] , df["Ventas"])
plt.title('Economia')
plt.xlabel('Años')
plt.ylabel('Ventas')
plt.show()
#%%
# ejercicio 2
plt.bar(df['Año'], df["Ventas"])
plt.title('Ventas por Año')
plt.xlabel('Año')
plt.ylabel('Ventas')
plt.show()
#%%
# ejercicio 3
df['Gastos'] = [150, 180, 210, 220, 300]
plt.scatter(df["Ventas"], df["Gastos"])
plt.title('Gráfico de Dispersión')
plt.xlabel('Ventas')
plt.ylabel('Gastos')
plt.show()
#%%
# Ejercicio 4
plt.subplot(1, 2, 1)
plt.plot(df['Año'], df["Ventas"])
plt.title('Gráfico de Líneas')

plt.subplot(1, 2, 2)
plt.bar(df['Año'], df["Ventas"])
plt.title('Gráfico de Barras')

plt.show()
#%%
# Ejercicio 5
plt.hist(df["Ventas"], bins=3, edgecolor='black')
plt.title('Histograma')
plt.xlabel('Ventas')
plt.ylabel('Frecuencia')
plt.show()
#%%
#Ejercicio 6

plt.style.use('_mpl-gallery')

# plot
fig, ax = plt.subplots(figsize=(8, 5))  

df["Ganancias"]=df["Ventas"]-df["Gastos"]
ax.plot()
ax.plot(df["Año"], df["Ventas"], '-', linewidth=2, label="Ventas")  # Ventas
ax.plot(df["Año"], df["Gastos"], '-', linewidth=2, label="Gastos") 
ax.plot(df["Año"], df["Ganancias"], '-', linewidth=2, label="Ganancias") 

ax.set_title("Comparativa de Ventas, Gastos y Ganancias", fontsize=14)
ax.set_xlabel("Año", fontsize=12)
ax.legend() 
plt.show()
#%%
#Ejercicio 7 y 8
import seaborn as sns

dfcount = df.groupby("Ventas").size()
colores = sns.color_palette("Set1", len(dfcount)) 
fig, ax = plt.subplots(figsize=(5, 8))
ax.pie(dfcount, labels=dfcount.index, autopct='%1.1f%%', colors=colores)

ax.set_title("Porcentaje Ventas del total")

plt.savefig("grafico_Ventas.jpg") 
plt.show()
#%%