# CONTEXTO DEL PROYECTO: PyXEL Studio

Este documento sirve como guía fundamental para el desarrollo del proyecto "PyXEL Studio". Define las limitaciones, el alcance, la arquitectura y los estándares seguidos.

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

- **Concepto:** Una aplicación de escritorio para crear "Pixel Art" de forma numérica. El usuario puede "pintar" en una cuadrícula (ej. 32x32) seleccionando colores de una paleta predefinida.
- **Interfaz:** La GUI será construida utilizando la librería `ttkbootstrap`.
- **Persistencia:** Los proyectos (lienzos) se guardarán y cargarán desde archivos con formato `.csv`. Cada celda en el archivo `.csv` corresponderá al código de color de un píxel en la cuadrícula.

---

### 3. Estado del Proyecto (Implementación y Documentación Completadas)

Se ha completado el ciclo de desarrollo de la aplicación, incluyendo la implementación de todas las funcionalidades y la documentación completa del código fuente.

#### Cómo Ejecutar la Aplicación
Para ejecutar la aplicación, asegúrate de tener todas las dependencias instaladas (principalmente `ttkbootstrap`) y luego ejecuta el archivo `main.py` desde la raíz del proyecto:
```bash
python main.py
```

#### Arquitectura Final
La arquitectura del software sigue el diseño planificado, separando las responsabilidades en tres módulos principales dentro del paquete `src`:

- **`logic.py` (Modelo):** Contiene el estado de la aplicación. Gestiona la matriz de colores del lienzo (`matriz_colores`), el color actual seleccionado (`color_actual`) y la paleta de colores (`PALETA_COLORES`). Proporciona funciones para modificar y acceder a estos datos de forma segura.

- **`file_manager.py` (Persistencia):** Se encarga de la lógica de guardado y carga. Sus funciones `guardar_csv` y `cargar_csv` interactúan con el sistema de archivos para persistir y recuperar el estado del lienzo en formato `.csv`, incluyendo validaciones robustas de los datos.

- **`gui_setup.py` (Vista y Controlador):** Es responsable de construir y gestionar la interfaz gráfica. Crea todos los widgets, los posiciona y define los controladores de eventos (`on_click`, `atrapar_nombre_archivo`, etc.) que conectan las acciones del usuario con las funciones de los módulos `logic` y `file_manager`.

- **`main.py` (Punto de Entrada):** Es un script simple que inicializa la ventana principal de `ttkbootstrap` y delega la construcción de la interfaz a `gui_setup.py`, iniciando el bucle de la aplicación.

#### Roadmap de Hitos
Todos los hitos planificados para la versión 1.0 han sido completados.

1.  **Construcción de la GUI estática:** `(Completado)`
2.  **Implementación de la lógica de pintado:** `(Completado)`
3.  **Implementación de la funcionalidad de guardado y carga (CSV):** `(Completado)`
4.  **Documentación final (Docstrings y comentarios):** `(Completado)`