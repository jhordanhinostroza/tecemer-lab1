# tecemer-lab1

Proyecto de prÃ¡ctica de la Semana 1 del curso TecnologÃ­as Emergentes (ISO46B) â€” UNCP.
Consume una API pÃºblica de chistes como ejercicio de configuraciÃ³n de entorno.

## InstalaciÃ³n

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
```

## Uso

```bash
python -m tecemer_lab1.app
```

## Estructura del repositorio

```
tecemer-lab1/
â”œâ”€â”€ src/tecemer_lab1/   # cÃ³digo fuente
â”œâ”€â”€ pyproject.toml      # metadatos y dependencias
â”œâ”€â”€ README.md
â””â”€â”€ .gitignore
```

## Autor

Curso: TecnologÃ­as Emergentes (ISO46B) â€” Facultad de IngenierÃ­a de Sistemas, UNCP.


## Flujo de datos â€” Semana 2

Esta secciÃ³n documenta el pipeline de datos construido en la Semana 2 (LibrerÃ­as para Datos y AutomatizaciÃ³n).

**Fuente:** API pÃºblica Open-Meteo (`https://api.open-meteo.com/v1/forecast`), sin necesidad de clave de acceso. Se consulta el pronÃ³stico de 7 dÃ­as para Huancayo (latitud -12.07, longitud -75.21): temperatura mÃ¡xima, temperatura mÃ­nima y precipitaciÃ³n diaria.

**TransformaciÃ³n:**
1. `clima.py` consume la API con `requests` (timeout de 5s y manejo de excepciones) y guarda la respuesta cruda en `pronostico_huancayo.json`.
2. La misma respuesta se convierte a `pronostico_huancayo.csv` con el mÃ³dulo estÃ¡ndar `csv`.
3. `analisis.py` carga el CSV en un DataFrame de Pandas, agrega las columnas derivadas `amplitud_termica`, `dia_lluvioso` y `categoria` (frÃ­o/templado/cÃ¡lido), y calcula un resumen agrupado por categorÃ­a con `groupby`.

**Salida:**
- `pronostico_huancayo.json` â€” respuesta cruda de la API (trazabilidad del dato original).
- `pronostico_huancayo.csv` â€” datos tabulares sin procesar.
- `pronostico_huancayo_procesado.csv` â€” datos con las columnas derivadas.
- `resumen_por_categoria.csv` â€” agregaciÃ³n por categorÃ­a de temperatura.

**CÃ³mo reproducirlo:**
```bash
python clima.py
python analisis.py
```

## Cierre de la Unidad I - Semana 3
Herramienta de automatizaci¢n: organizador.py clasifica y mueve archivos
de una carpeta en subcarpetas por tipo (Documentos, Imagenes, Videos,
Comprimidos, Otros), con modo de simulacion (--dry-run) mediante argparse.
Uso:
```
python organizador.py <carpeta> [--dry-run]
```
Pruebas: test_organizador.py cubre clasificacion, movimiento real y modo
simulacion, usando la fixture tmp_path de pytest para no afectar el
sistema de archivos real. Ejecutar con: pytest -v
