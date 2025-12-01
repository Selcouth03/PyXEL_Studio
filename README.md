# PyXEL Studio

¡Una sencilla aplicación de escritorio para crear pixel art, construida con Python y `ttkbootstrap`!

![PyXEL Studio Screenshot](https://raw.githubusercontent.com/abrahamselcouth/PyXEL_Studio/main/assets/readme/screenshot.png)

## ✨ Características

*   **Lienzo de 32x32:** Un lienzo de tamaño clásico para tus creaciones de pixel art.
*   **Paleta de Colores Predefinida:** Una paleta cuidadosamente seleccionada para empezar a crear de inmediato.
*   **Guardado y Carga:** Guarda tu progreso en archivos `.csv` y cárgalos más tarde para continuar donde lo dejaste.
*   **Interfaz Limpia:** Una interfaz de usuario simple y moderna gracias a `ttkbootstrap`.

## 🛠️ Tecnologías Utilizadas

*   **Python:** El lenguaje principal de la aplicación.
*   **ttkbootstrap:** Para la creación de la interfaz gráfica de usuario.
*   **uv:** Para la gestión del entorno virtual y las dependencias del proyecto.

## 🚀 Instalación y Ejecución

Para ejecutar PyXEL Studio en tu máquina local, sigue estos pasos.

### 1. Prerrequisitos

Asegúrate de tener instalada una versión reciente de **Python** (3.8 o superior). Puedes descargarla desde [python.org](https://www.python.org/).

### 2. Instala `uv`

Este proyecto utiliza `uv`, un instalador y resolutor de paquetes de Python extremadamente rápido, escrito en Rust. Necesitas instalarlo para manejar el entorno virtual y las dependencias.

Puedes instalar `uv` de dos maneras:

*   **Opción A (Recomendada): Usando `curl` (Linux, macOS, WSL)**

    Abre tu terminal y ejecuta el siguiente comando. Este método descarga e instala `uv` de forma aislada en tu sistema.
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

*   **Opción B: Usando `pip`**

    Si prefieres, también puedes instalarlo a través de `pip` (asegúrate de tener `pip` actualizado).
    ```bash
    pip install uv
    ```
Después de la instalación, cierra y vuelve a abrir tu terminal, o ejecuta `source $HOME/.cargo/env` para que el comando `uv` esté disponible.

### 3. Crea y Sincroniza el Entorno Virtual

Con `uv` instalado, el siguiente paso es crear un entorno virtual y sincronizar las dependencias del proyecto. Este proceso leerá los archivos `pyproject.toml` y `uv.lock` para instalar exactamente las mismas versiones de las librerías con las que se desarrolló el proyecto.

Navega hasta la raíz del proyecto en tu terminal y ejecuta:

```bash
uv sync
```

Este único comando se encargará de:
1.  Crear un entorno virtual en una carpeta llamada `.venv` (si no existe).
2.  Instalar `ttkbootstrap` y todas sus dependencias de forma muy rápida.

### 4. Ejecuta la Aplicación

Una vez que el entorno esté sincronizado, puedes ejecutar la aplicación. La forma recomendada es usar `uv` para que se encargue de activar el entorno virtual por ti.

```bash
uv run python main.py
```

¡Y listo! La ventana de PyXEL Studio debería aparecer en tu pantalla.

## 📁 Estructura del Proyecto

```
PyXEL_Studio/
├── main.py                 # Punto de entrada para ejecutar la aplicación.
├── README.md               # Este archivo.
├── pyproject.toml          # Define las dependencias del proyecto para uv.
├── uv.lock                 # Fija las versiones exactas de las dependencias.
├── assets/                 # Directorio para guardar los .csv generados.
└── src/                    # Paquete principal del código fuente.
    ├── gui_setup.py        # Módulo para la construcción de la UI (Vista/Controlador).
    ├── logic.py            # Módulo para el estado y la lógica de negocio (Modelo).
    └── file_manager.py     # Módulo para la persistencia (guardado/carga de archivos).
```

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
