#%%
import pandas as  pd
#Ejercicio 1
empleados= ({'Nombre': ['Ana', 'Luis', 'Marta', 'Carlos', 'Marcos'],
            'Edad': [28,35,42, 30,18],
            'Departamento':['Ventas', 'Finanzas', 'IT', 'Ventas', 'Administración']})
df = pd.DataFrame(empleados)
df

#%%

#Ejercicio 2
mayores_30=df[df['Edad']>30]
print(mayores_30)

#%%
#Ejercicio 3
df['Años_experiencia']=[5,10,15,3,8]
print(df)
#%%
#Ejercicio 4
df['Años_hasta_jubilacion']= 60-df['Edad']
print(df)
#%%

#Ejercicio 5
grupo=df.groupby('Nombre')['Departamento']
print(grupo.head())
#%%
#Ejercicio 6
ventas=df[df['Departamento']== 'Ventas']
print(ventas)
#%%
#Ejercicio 7
df['Edad'][1]=36
print(df)
#%%
#Ejercicio 8
promedio=df['Edad'].mean()
print(promedio)

#%%
#Ejercicio 9
promedio_exp=df['Años_experiencia'].mean()
print(promedio_exp)
#%%