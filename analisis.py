import pandas as pd

df = pd.read_csv("pronostico_huancayo.csv")

print("--- Primeras filas ---")
print(df.head())
print("\n--- Informacion del DataFrame ---")
print(df.info())
print("\n--- Estadisticas descriptivas ---")
print(df.describe())




import pandas as pd

# Paso 3.1: Cargar el CSV
df = pd.read_csv("pronostico_huancayo.csv")

# Paso 3.2: Exploración y transformación
df["amplitud_termica"] = df["temp_max"] - df["temp_min"]
df["dia_lluvioso"] = df["precipitacion"] > 0
df["categoria"] = df["temp_max"].apply(
    lambda t: "cálido" if t >= 20 else ("templado" if t >= 15 else "frío")
)

print("--- DataFrame con columnas derivadas ---")
print(df)

print("\n--- Estadísticas descriptivas de variables numéricas ---")
print(df.describe())



# Paso 3.3: Agregaciones con groupby
resumen = df.groupby("categoria").agg(
    dias=("categoria", "count"),
    temp_max_promedio=("temp_max", "mean"),
    precipitacion_total=("precipitacion", "sum"),
)

print("--- Resumen por Categoría ---")
print(resumen)



# Paso 3.4: Exportar DataFrames procesados
df.to_csv("pronostico_huancayo_procesado.csv", index=False)
resumen.to_csv("resumen_por_categoria.csv")

print("\nArchivos 'pronostico_huancayo_procesado.csv' y 'resumen_por_categoria.csv' generados con éxito.")