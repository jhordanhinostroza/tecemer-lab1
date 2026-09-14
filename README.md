## Flujo de datos (Semana 2)

- **Fuente:** API pública Open-Meteo (`https://api.open-meteo.com/v1/forecast`), pronóstico de 7 días para Huancayo (temperatura máxima, mínima y precipitación).
- **Transformación:** los datos crudos en JSON se guardan en `pronostico_huancayo.json` y se convierten a `pronostico_huancayo.csv`. Luego, con Pandas, se calculan columnas derivadas (amplitud térmica, día lluvioso, categoría de clima) y se agregan estadísticas por categoría con `groupby`.
- **Salida:** `pronostico_huancayo_procesado.csv` (datos enriquecidos) y `resumen_por_categoria.csv` (resumen agregado por categoría de clima).
