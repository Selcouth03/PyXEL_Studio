# PyXEL Studio

¡Una sencilla aplicación de escritorio para crear pixel art, construida con Python y `ttkbootstrap` delightful!

## ✨ Características

- **Lienzo de 32x32:** Un lienzo de tamaño clásico para tus creaciones de pixel art.
- **Paleta de Colores Predefinida:** Una paleta cuidadosamente seleccionada para empezar a crear de inmediato.
- **Guardado y Carga:** Guarda tu progreso en archivos `.csv` y cárgalos más tarde para continuar donde lo dejaste.
- **Interfaz Limpia:** Una interfaz de usuario simple y moderna gracias a `ttkbootstrap`.

## 🛠️ Tecnologías Utilizadas

- **Python:** El lenguaje principal de la aplicación.
- **ttkbootstrap:** Para la creación de la interfaz gráfica de usuario.
- **uv:** Para la gestión del entorno virtual y las dependencias del proyecto.

## 🚀 Instalación y Ejecución (Automatizado)

Hemos simplificado todo el proceso para que puedas empezar en segundos. Solo necesitas tener **Python 3.8+** y **Git** instalados en tu sistema.

### Paso 1: Configurar el Entorno

Ejecuta el script de configuración. Este se encargará de todo lo necesario:
- Verificará e instalará `Tkinter` (la dependencia base para la GUI).
- Instalará `uv` (el gestor de paquetes y entorno virtual).
- Sincronizará las dependencias de Python del proyecto.

```bash
bash setup.sh
```
*El script podría pedirte tu contraseña para instalar paquetes del sistema (`python3-tk`) si es necesario.*

### Paso 2: Ejecutar la Aplicación

Una vez finalizada la configuración, ejecuta la aplicación con el siguiente comando:

```bash
bash run.sh
```
Este script se encarga de encontrar automáticamente las librerías necesarias y lanzar la aplicación. ¡Y listo! La ventana de PyXEL Studio debería aparecer en tu pantalla.

---

<details>
<summary><b>(Alternativa) Instalación y Ejecución Manual</b></summary>

Estos pasos son una alternativa manual, **solo necesarios si el script `setup.sh` no funciona o si deseas un control más granular sobre la instalación.**

### 1. Prerrequisitos

Asegúrate de tener instalada una versión reciente de **Python** (3.8 o superior). Puedes descargarla desde [python.org](https://www.python.org/).

**Si el script `setup.sh` falla en instalar `tkinter` automáticamente, aquí tienes las instrucciones manuales:**

- **Ubuntu/Debian:** `sudo apt-get install python3-tk`
- **Fedora/RHEL:** `sudo dnf install python3-tkinter`
- **Arch Linux:** `sudo pacman -S tk`

### 2. Instala `uv`

**Si el script `setup.sh` falla en instalar `uv` automáticamente, puedes instalarlo manualmente así:**

- **Opción A (Recomendada): Usando `curl` (Linux, macOS, WSL)**

  Abre tu terminal y ejecuta el siguiente comando. Este método descarga e instala `uv` de forma aislada en tu sistema.

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

- **Opción B: Usando `pip`**

      Si prefieres, también puedes instalarlo a través de `pip` (asegúrate de tener `pip` actualizado).
      ```bash
      pip install uv
      ```

  Después de la instalación, cierra y vuelve a abrir tu terminal, o ejecuta `source $HOME/.cargo/env` para que el comando `uv` esté disponible.

### 3. Crea y Sincroniza el Entorno Virtual

Con `uv` instalado, navega a la raíz del proyecto y ejecuta:

```bash
uv sync
```
Este comando crea un entorno virtual (`.venv`) e instala `ttkbootstrap` y sus dependencias.

### 4. Ejecuta la Aplicación

Para lanzar la aplicación, recomendamos usar `bash run.sh`, ya que soluciona problemas de rutas de librerías automáticamente.

</details>

## 🎨 Archivo de Muestra

Dentro de la carpeta `assets`, encontrarás un archivo llamado `teacher.csv`. Este es un lienzo de ejemplo que puedes cargar en la aplicación para ver una demostración de lo que se puede crear.

Para cargarlo:
1. Ejecuta la aplicación.
2. En el campo "Nombre del Archivo", escribe `teacher`.
3. Haz clic en el botón **"Cargar"**.

## 📁 Estructura del Proyecto

```
PyXEL_Studio/
├── main.py                 # Punto de entrada para ejecutar la aplicación.
├── setup.sh                # Script de configuración automatizada.
├── run.sh                  # Script de ejecución automatizada.
├── README.md               # Este archivo.
├── pyproject.toml          # Define las dependencias del proyecto para uv.
├── uv.lock                 # Fija las versiones exactas de las dependencias.
├── assets/                 # Directorio para guardar los .csv generados.
│   └── teacher.csv         # Archivo de ejemplo para cargar.
└── src/                    # Paquete principal del código fuente.
    ├── gui_setup.py        # Módulo para la construcción de la UI (Vista/Controlador).
    ├── logic.py            # Módulo para el estado y la lógica de negocio (Modelo).
    └── file_manager.py     # Módulo para la persistencia (guardado/carga de archivos).
```

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
