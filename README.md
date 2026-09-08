(
echo # tecemer-lab1
echo.
echo Laboratorio N.º 1 de Tecnologías Emergentes. Proyecto en Python estructurado utilizando el formato `src` layout y configurado para instalación editable mediante `pyproject.toml`.
echo.
echo ---
echo.
echo ## Instrucciones de Instalación
echo.
echo 1. **Clonar el repositorio y acceder a la carpeta:**
echo    ```bash
echo    git clone [https://github.com/jhordanhinostroza/tecemer-lab1.git](https://github.com/jhordanhinostroza/tecemer-lab1.git)
echo    cd tecemer-lab1
echo    ```
echo.
echo 2. **Crear y activar el entorno virtual:**
echo    ```cmd
echo    python -m venv .venv
echo    .venv\Scripts\activate
echo    ```
echo.
echo 3. **Instalar las dependencias y el paquete en modo editable:**
echo    ```cmd
echo    pip install -e .
echo    ```
echo.
echo ---
echo.
echo ## Ejemplo de Uso
echo.
echo Para ejecutar el módulo principal de la aplicación:
echo ```cmd
echo python src/tecemer_lab1/app.py
echo ```
echo.
echo O realizar la importación desde Python:
echo ```python
echo from tecemer_lab1 import app
echo ```
echo.
echo ---
echo.
echo ## Estructura del Repositorio
echo.
echo ```text
echo tecemer-lab1/
echo ├── src/
echo │   └── tecemer_lab1/
echo │       ├── __init__.py
echo │       └── app.py
echo ├── .venv/
echo ├── .gitignore
echo ├── pyproject.toml
echo ├── requirements.txt
echo └── README.md
echo ```
echo.
echo ---
echo.
echo ## Autor y Curso
echo.
echo - **Curso:** Tecnologías Emergentes — ISO46B
echo - **Institución:** Universidad Nacional del Centro del Perú ^(UNCP^)
echo - **Facultad:** Facultad de Ingeniería de Sistemas ^(FIS^)
) > README.md

git add README.md
git commit -m "docs: actualiza README con secciones requeridas"
git push origin master
