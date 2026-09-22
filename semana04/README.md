## Semana 4 — Redes Neuronales Artificiales (Keras)

Se construyó un clasificador binario que predice si un día será lluvioso en
Huancayo, usando un perceptrón multicapa (MLP) con Keras/TensorFlow.

- `ampliar_dataset.py`: amplía el histórico climático consultando la API
  histórica de Open-Meteo (91 días).
- `preparar_dataset.py`: limpia, escala y particiona el dataset en train/test.
- `perceptron_sintetico.py`: primer MLP de práctica sobre datos sintéticos
  (precisión en test: 0.88).
- `clasificador_lluvia.py`: MLP real comparado contra un baseline de regresión
  logística (ambos con precisión 0.7368 en test — con un dataset pequeño el
  MLP no siempre supera al baseline, y eso es esperado).
- `predecir.py`: carga el modelo guardado y predice sobre observaciones nuevas.
- `tests/test_preparacion.py`: 3 pruebas con pytest sobre la función
  `calcular_dia_lluvioso`.

**Nota de diseño:** al importar `preparar_dataset` en las pruebas, Python
ejecuta todo el script (carga y procesamiento del CSV). En un proyecto
profesional, la lógica reutilizable se separaría en un módulo sin efectos
secundarios al importarse. Se deja como mejora futura identificada.