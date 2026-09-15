# --- Paso 1.4 Mini-reto: estadística descriptiva con NumPy ---
import numpy as np


temperaturas = np.array([12.5, 14.0, 11.8, 13.2, 15.1, 10.9, 12.7])
print('Promedio:', temperaturas.mean())
print('Desviación estándar:', temperaturas.std())
print('Mínima:', temperaturas.min())
print('Máxima:', temperaturas.max())        


import time
import numpy as np

# Paso 1.3: Operaciones vectorizadas vs. bucles
n = 1_000_000
lista = list(range(n))
array = np.arange(n)

inicio = time.time()
resultado_lista = [x + 10 for x in lista]
print("Bucle for:", time.time() - inicio, "segundos")

inicio = time.time()
resultado_array = array + 10
print("Vectorizado:", time.time() - inicio, "segundos")



# --- Paso 1.4: Mini-reto: estadística descriptiva ---
temperaturas = np.array([12.5, 14.0, 11.8, 13.2, 15.1, 10.9, 12.7])
print("Promedio:", temperaturas.mean())
print("Desviación estándar:", temperaturas.std())
print("Mínima:", temperaturas.min())
print("Máxima:", temperaturas.max())