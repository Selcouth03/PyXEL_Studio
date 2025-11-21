import ttkbootstrap as ttk

from .logic import PALETA_COLORES

FILAS_LIENZO = 32
COLUMNAS_LIENZO = 32

FILAS_PALETA = 8
COLUMNAS_PALETA = 3

# --- Modelo de Datos del Lienzo ---
# Esta matriz 2D es la "única fuente de verdad" para los colores del lienzo.
lienzo_data = [["#FFFFFF" for _ in range(COLUMNAS_LIENZO)] for _ in range(FILAS_LIENZO)]


def crear_interfaz_completa(ventana: ttk.Window):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    style = ttk.Style()

    # Panel seccion de paletas
    panel_paleta = ttk.Frame(
        ventana,
        style="secondary",
        width=400,  # noqa: F405
    )
    panel_paleta.pack_propagate(False)
    panel_paleta.pack(side="left", fill="y")

    # Frame Color Actual
    frame_color_actual = ttk.Frame(panel_paleta, bootstyle="secondary")

    # Label y Boton de color actual
    label_color_actual = ttk.Label(
        frame_color_actual, text="Color seleccionado", style="secondary.Inverse.TLabel"
    )

    # Color blanco por defecto para el cuadro de color actual

    style.configure(  # type: ignore
        "EstiloCuadro.TButton",
        font=(None, 18),
        width=5,
        background="#FFFFFF",
        bordercolor="#FFFFFF",
        focusthickness=0,  # Elimina el anillo de enfoque
        lightcolor="#FFFFFF",  # Elimina el borde claro del relieve
        darkcolor="#FFFFFF",  # Elimina el borde oscuro del relieve
        relief="flat",  # Elimina el efecto 3D del botón
    )
    style.map(
        "EstiloCuadro.TButton",
        background=[("active", "#FFFFFF")],
        bordercolor=[("active", "#FFFFFF")],
        lightcolor=[("active", "#FFFFFF")],
        darkcolor=[("active", "#FFFFFF")],
    )  # Mantiene el color en hover para fondo y borde
    cuadro_color_actual = ttk.Button(
        frame_color_actual,
        style="EstiloCuadro.TButton",
    )

    label_color_actual.pack()
    cuadro_color_actual.pack(pady=10)
    # Empaquetamos el frame del color actual en la parte superior del panel de paleta
    frame_color_actual.pack(side="top", pady=20, fill="x", padx=10)

    # Creamos un estilo para el separador para que sea visible en el tema oscuro
    color_separador = style.lookup("light.TFrame", "background")
    style.configure("ColorContraste.TSeparator", background=color_separador)  # type: ignore

    # Separador del Frame color actual y el Frame paleta de colores
    separador_color_actual_paleta_colores = ttk.Separator(
        panel_paleta, style="ColorContraste.TSeparator"
    )
    # Empaquetamos el separador para que ocupe todo el ancho
    separador_color_actual_paleta_colores.pack(side="top", pady=10, fill="x", padx=20)

    # Frame para la paleta de colores
    frame_paleta_colores = ttk.Frame(panel_paleta, style="secondary")
    # Empaquetamos el frame ANTES de llenarlo
    frame_paleta_colores.pack(
        side="top", fill="x", expand=True, padx=10, pady=20, anchor="n"
    )

    # Hacemos que los botones se centren en el frame configurando las columnas que usamos
    for j in range(COLUMNAS_PALETA):
        frame_paleta_colores.columnconfigure(j, weight=1)

    # --- Estilo base para los botones de la paleta ---
    style.configure(  # type: ignore
        "Paleta.TButton",
        relief="flat",
        padding=(25, 10),
        borderwidth=0,
    )

    # crear botones de la paleta
    indice_paleta_colores = -1
    for i in range(FILAS_PALETA):
        for j in range(COLUMNAS_PALETA):
            crear_btn_paleta(
                frame_paleta_colores, style, i, j, indice_paleta_colores + 1
            )
            indice_paleta_colores += 1

    # Panel para manejo de archivos
    panel_manejo_archivos = ttk.Frame(panel_paleta, bootstyle="secondary")
    panel_manejo_archivos.pack(fill="x", expand=True, anchor="s", pady=40)

    # Entrada y botones de panel manejo de archivos
    seccion_entrada_archivo = ttk.Labelframe(
        panel_manejo_archivos, text="Nombre del archivo", bootstyle="sec"
    )
    seccion_entrada_archivo.pack(side="top", pady=10)

    entrada_archivo = ttk.Entry(seccion_entrada_archivo)
    entrada_archivo.pack()

    btn_guardar = ttk.Button(panel_manejo_archivos, text="Guardar")
    btn_guardar.pack(side="top", anchor="center", pady=10)

    btn_cargar = ttk.Button(panel_manejo_archivos, text="Cargar")
    btn_cargar.pack(side="top", anchor="center", pady=10)

    # Panel del Lienzo
    # Usamos un Canvas, que es mucho más eficiente para dibujar rejillas.
    lienzo = ttk.Canvas(ventana, background="white", highlightthickness=0)
    lienzo.pack(fill="both", expand=True)
    # Vinculamos el redibujado de la cuadrícula al evento de cambio de tamaño del lienzo.
    # Esto asegura que siempre se calcule con las dimensiones correctas.
    lienzo.bind("<Configure>", lambda event: crear_grid_lienzo(lienzo))
    # Vinculamos el evento de clic izquierdo del ratón a nuestra función de pintado.
    lienzo.bind(
        "<Button-1>", lambda event: on_lienzo_click(event, lienzo, "#FF0000")
    )  # Usamos Rojo como color de prueba

    ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")


def on_lienzo_click(event, lienzo: ttk.Canvas, color: str): # type: ignore
    """Se ejecuta al hacer clic en el lienzo para pintar un píxel."""
    # Obtenemos los cálculos de tamaño y posición de una función auxiliar
    tamano_pixel, offset_x, offset_y = _calcular_geometria_lienzo(lienzo)

    # Si el tamaño es 0, significa que el lienzo aún no es visible, no hacemos nada.
    if tamano_pixel == 0:
        return

    # Calculamos a qué fila y columna corresponde el clic
    columna = int((event.x - offset_x) // tamano_pixel) # type: ignore
    fila = int((event.y - offset_y) // tamano_pixel) # type: ignore

    # Verificamos que el clic esté dentro de los límites de la cuadrícula
    # Esto evita errores si se hace clic en el margen exterior.
    if 0 <= fila < FILAS_LIENZO and 0 <= columna < COLUMNAS_LIENZO:
        # 1. Actualizamos el Modelo (nuestra matriz de datos)
        lienzo_data[fila][columna] = color

        # Encontramos el ID del item más cercano a donde se hizo clic
        item_id = lienzo.find_closest(event.x, event.y)[0] # type: ignore
        # 2. Actualizamos la Vista (el color del rectángulo en el Canvas)
        lienzo.itemconfig(item_id, fill=color)


def _calcular_geometria_lienzo(lienzo: ttk.Canvas):
    """Función auxiliar para calcular el tamaño y offset de los píxeles."""
    ancho_canvas = lienzo.winfo_width()
    alto_canvas = lienzo.winfo_height()
    # Si el canvas no tiene tamaño, retornamos 0 para evitar división por cero.
    if ancho_canvas <= 1 or alto_canvas <= 1:
        return 0, 0, 0
    tamano_pixel = min(ancho_canvas / COLUMNAS_LIENZO, alto_canvas / FILAS_LIENZO)
    offset_x = (ancho_canvas - (COLUMNAS_LIENZO * tamano_pixel)) / 2
    offset_y = (alto_canvas - (FILAS_LIENZO * tamano_pixel)) / 2
    return tamano_pixel, offset_x, offset_y


def crear_grid_lienzo(lienzo: ttk.Canvas):
    """Dibuja la cuadrícula de píxeles. Se llama cada vez que el lienzo se redimensiona."""
    lienzo.delete("all")  # Limpiamos el lienzo antes de redibujar
    tamano_pixel, offset_x, offset_y = _calcular_geometria_lienzo(lienzo)
    if tamano_pixel == 0:
        return
    for i in range(FILAS_LIENZO):
        for j in range(COLUMNAS_LIENZO):
            x1, y1 = (j * tamano_pixel) + offset_x, (i * tamano_pixel) + offset_y
            x2, y2 = x1 + tamano_pixel, y1 + tamano_pixel
            lienzo.create_rectangle(
                x1, y1, x2, y2, fill=lienzo_data[i][j], outline="#E0E0E0"
            )


def crear_btn_paleta(
    panel_paleta: ttk.Frame, style: ttk.Style, fila: int, columna: int, indice: int
):
    color_fondo = PALETA_COLORES[indice]
    # Creamos un nombre de estilo único que hereda del estilo base "Paleta.TButton"
    nombre_estilo = f"Color{indice}.Paleta.TButton"

    # Configuramos solo las propiedades que cambian (el color)
    style.configure(nombre_estilo, background=color_fondo)  # type: ignore
    # Mapeamos el hover para que no cambie de color
    style.map(nombre_estilo, background=[("active", color_fondo)])

    # Creamos el botón con su estilo único y derivado
    btn_panel = ttk.Button(panel_paleta, style=nombre_estilo)

    btn_panel.grid(row=fila, column=columna, padx=5, pady=15)
