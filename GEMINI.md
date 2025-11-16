# CONTEXTO DEL PROYECTO: PyXEL Studio

Este documento sirve como guía fundamental para el desarrollo del proyecto "PyXEL Studio". Define las limitaciones, el alcance, la arquitectura y los estándares a seguir.

---

### 1. Contexto del Asistente (Mandatorio)

#### Limitaciones del Usuario
El desarrollo debe adherirse estrictamente a un conjunto específico de 162 tópicos universitarios.

- **Permitido:**
  - Variables y tipos de datos básicos.
  - Lógica de control de flujo (`if`, `while`, `for`).
  - Definición y uso de `funciones`.
  - Secuencias: `Listas`, `Tuplas`, `Diccionarios`.
  - Manejo de archivos de texto plano (`.csv`, `.txt`).
  - Módulos estándar de Python como `math` y `random`.
  - Interfaces gráficas de usuario (GUI) exclusivamente con `ttkbootstrap`.

- **Prohibido (Absoluto):**
  - Programación Orientada a Objetos avanzada (definición de `class` propias).
  - Interacción con bases de datos (SQL).
  - Frameworks web como Django o Flask.
  - Uso de APIs externas complejas.

#### Comportamiento del Asistente
- **Profesional y Didáctico:** Las explicaciones deben ser rigurosas y claras.
- **Desarrollo por Fases:** El proceso se divide en etapas bien definidas: Idea, Alcance, Estructura, Lógica y Documentación.
- **Diseño Primero:** Se prioriza el diseño de la arquitectura y el flujo de datos antes de la implementación del código.
- **Principios de Diseño:** Se deben seguir los principios de **Alta Cohesión** (cada módulo tiene una responsabilidad única y bien definida) y **Bajo Acoplamiento** (los módulos son independientes entre sí).

---

### 2. El Proyecto: "PyXEL Studio"

- **Concepto:** Una aplicación de escritorio para crear "Pixel Art" de forma numérica. El usuario puede "pintar" en una cuadrícula (ej. 16x16) seleccionando colores de una paleta predefinida.
- **Interfaz:** La GUI será construida utilizando la librería `ttkbootstrap`.
- **Persistencia:** Los proyectos (lienzos) se guardarán y cargarán desde archivos con formato `.csv`. Cada celda en el archivo `.csv` corresponderá al código de color de un píxel en la cuadrícula.

---

### 3. Estado del Proyecto (Organización Completada)

Se han completado las fases de planificación previas a la codificación.

#### Fase 1: Arquitectura y Alcance (Definido)
- **Alcance:**
  - Una cuadrícula de 16x16 píxeles.
  - Una paleta de colores seleccionable.
  - Botones para "Guardar" y "Cargar" el lienzo.
- **Arquitectura de Datos:**
  - La representación del lienzo en memoria será una lista de listas (matriz) de strings: `List[List[str]]`. Cada string es un código de color (ej. "#FFFFFF").
- **Estructura de Directorios:**
  ```
  PyXEL_Studio/
  ├── main.py                 # Punto de entrada (Inicia la GUI)
  ├── assets/                 # Directorio para guardar los .csv generados
  └── src/                    # Paquete de código fuente
      ├── __init__.py         # Marca 'src' como un paquete de Python
      ├── gui_setup.py        # Funciones para construir la ventana y widgets
      ├── logic.py            # Lógica de la aplicación (manejo de la matriz, color actual)
      └── file_manager.py     # Lógica de persistencia (lectura/escritura de CSV)
  ```

#### Fase 2: Diseño Lógico y Flujo (Definido)
- **Flujo "Pintar":**
  - **Input:** El usuario hace clic en una celda de la cuadrícula.
  - **Proceso:** Se actualiza la matriz en memoria (`matriz[fila][col] = color_actual`) y se cambia el color de fondo del widget correspondiente (`boton[fila][col].config(bg=color_actual)`).
  - **Output:** El color de la celda cambia en la pantalla.
- **Flujo "Guardar":**
  - **Input:** El usuario hace clic en el botón "Guardar".
  - **Proceso:** Se recorre la matriz en memoria y se escribe su contenido en un archivo `.csv` usando el módulo `csv`.
  - **Output:** Un archivo `.csv` es creado o sobreescrito en el directorio `assets/`.
- **Especificación Funcional:** Se han definido las responsabilidades, argumentos y tipos de retorno para las funciones clave (ej. `guardar_csv`, `cargar_csv`, `inicializar_matriz`).
- **Roadmap de Hitos:**
  1. Construcción de la GUI estática.
  2. Implementación de la lógica de pintado.
  3. Implementación de la funcionalidad de guardado y carga (CSV).
  4. Documentación final (Docstrings y comentarios).

#### Fase 3: Estándares de Documentación (Definido)
- **Docstrings:** Todas las funciones y módulos deben tener docstrings siguiendo el formato estándar de Python (descripción, argumentos, retornos).
- **Type Hints:** Es obligatorio el uso de anotaciones de tipo del módulo `typing` (ej. `List`, `Dict`, `Tuple`) para todas las firmas de funciones.
- **Nomenclatura:**
  - `snake_case` para variables y nombres de función.
  - `UPPER_CASE` para constantes (ej. `TAMANO_GRID = 16`).
  - Prefijos para widgets de la GUI para mayor claridad (ej. `btn_guardar`, `frm_paleta`).
