import ttkbootstrap as ttk

from . import logic

# Las constantes de la paleta se mantienen para la construcción de la GUI.
FILAS_PALETA = 8
COLUMNAS_PALETA = 3


def on_color_seleccionado(event, color: str, style: ttk.Style):  # type: ignore
    """
    Controlador de evento para cuando se selecciona un color de la paleta.
    Actualiza el estado de la lógica y la GUI para reflejar el nuevo color.
    """
    # 1. Actualizar el Modelo (la lógica)
    logic.cambiar_color_seleccionado(color)

    # 2. Actualizar la Vista (el cuadro de 'Color seleccionado')
    style.configure("EstiloCuadro.TButton", background=color)  # pyright: ignore[reportUnknownMemberType]
    style.map(
        "EstiloCuadro.TButton",
        background=[("active", color)],
        bordercolor=[("active", color)],
        lightcolor=[("active", color)],
        darkcolor=[("active", color)],
    )


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

    # Damos estilo al cuadro que muestra el color actual
    style.configure(  # type: ignore
        "EstiloCuadro.TButton",
        font=(None, 18),
        width=5,
        background=logic.color_actual,  # Inicia con el color por defecto
        bordercolor=logic.color_actual,
        focusthickness=0,
        lightcolor=logic.color_actual,
        darkcolor=logic.color_actual,
        relief="flat",
    )
    style.map(
        "EstiloCuadro.TButton",
        background=[("active", logic.color_actual)],
        bordercolor=[("active", logic.color_actual)],
        lightcolor=[("active", logic.color_actual)],
        darkcolor=[("active", logic.color_actual)],
    )
    cuadro_color_actual = ttk.Button(
        frame_color_actual,
        style="EstiloCuadro.TButton",
    )

    label_color_actual.pack()
    cuadro_color_actual.pack(pady=10)
    frame_color_actual.pack(side="top", pady=20, fill="x", padx=10)

    # Separador
    color_separador = style.lookup("light.TFrame", "background")
    style.configure("ColorContraste.TSeparator", background=color_separador)  # type: ignore
    separador = ttk.Separator(panel_paleta, style="ColorContraste.TSeparator")
    separador.pack(side="top", pady=10, fill="x", padx=20)

    # Frame para la paleta de colores
    frame_paleta_colores = ttk.Frame(panel_paleta, style="secondary")
    frame_paleta_colores.pack(side="top", fill="x", padx=10, pady=20, anchor="n")
    for j in range(COLUMNAS_PALETA):
        frame_paleta_colores.columnconfigure(j, weight=1)

    style.configure(  # type: ignore
        "Paleta.TButton",
        relief="flat",
        padding=(25, 10),
        borderwidth=0,
    )

    # Crear botones de la paleta
    indice_paleta_colores = -1
    for i in range(FILAS_PALETA):
        for j in range(COLUMNAS_PALETA):
            indice_paleta_colores += 1
            # Pasamos el 'style' para que los botones puedan interactuar con él
            crear_btn_paleta(
                panel_paleta=frame_paleta_colores,
                style=style,
                fila=i,
                columna=j,
                indice=indice_paleta_colores,
            )

    # Panel para manejo de archivos
    panel_manejo_archivos = ttk.Frame(panel_paleta, bootstyle="secondary")
    panel_manejo_archivos.pack(fill="x", side="bottom", pady=40)

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
    lienzo = ttk.Canvas(ventana, background="white", highlightthickness=0)
    lienzo.pack(fill="both", expand=True)
    lienzo.bind("<Configure>", lambda event: crear_grid_lienzo(lienzo))
    # Se actualiza el bind para usar el color de la lógica en lugar de uno harcodeado
    lienzo.bind(
        "<Button-1>",
        lambda event: on_lienzo_click(event, lienzo, logic.obtener_color_actual()),
    )

    ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")


def on_lienzo_click(event, lienzo: ttk.Canvas, color: str):  # type: ignore
    """Se ejecuta al hacer clic en el lienzo para pintar un píxel."""
    tamano_pixel, offset_x, offset_y = _calcular_geometria_lienzo(lienzo)
    if tamano_pixel == 0:
        return

    columna = int((event.x - offset_x) // tamano_pixel)  # type: ignore
    fila = int((event.y - offset_y) // tamano_pixel)  # type: ignore

    if 0 <= fila < logic.FILAS_LIENZO and 0 <= columna < logic.COLUMNAS_LIENZO:
        logic.actualizar_pixel(fila, columna, color)
        item_id = lienzo.find_closest(event.x, event.y)[0]  # type: ignore
        lienzo.itemconfig(item_id, fill=color)


def _calcular_geometria_lienzo(lienzo: ttk.Canvas):
    """Función auxiliar para calcular el tamaño y offset de los píxeles."""
    ancho_canvas = lienzo.winfo_width()
    alto_canvas = lienzo.winfo_height()
    if ancho_canvas <= 1 or alto_canvas <= 1:
        return 0, 0, 0
    tamano_pixel = min(
        ancho_canvas / logic.COLUMNAS_LIENZO, alto_canvas / logic.FILAS_LIENZO
    )
    offset_x = (ancho_canvas - (logic.COLUMNAS_LIENZO * tamano_pixel)) / 2
    offset_y = (alto_canvas - (logic.FILAS_LIENZO * tamano_pixel)) / 2
    return tamano_pixel, offset_x, offset_y


def crear_grid_lienzo(lienzo: ttk.Canvas):
    """Dibuja la cuadrícula de píxeles. Se llama cada vez que el lienzo se redimensiona."""
    lienzo.delete("all")
    tamano_pixel, offset_x, offset_y = _calcular_geometria_lienzo(lienzo)
    if tamano_pixel == 0:
        return
    for i in range(logic.FILAS_LIENZO):
        for j in range(logic.COLUMNAS_LIENZO):
            x1, y1 = (j * tamano_pixel) + offset_x, (i * tamano_pixel) + offset_y
            x2, y2 = x1 + tamano_pixel, y1 + tamano_pixel
            lienzo.create_rectangle(
                x1, y1, x2, y2, fill=logic.matriz_colores[i][j], outline="#E0E0E0"
            )


def crear_btn_paleta(
    panel_paleta: ttk.Frame, style: ttk.Style, fila: int, columna: int, indice: int
):
    """Crea y posiciona un botón individual de la paleta de colores."""
    color_fondo = logic.PALETA_COLORES[indice]
    nombre_estilo = f"Color{indice}.Paleta.TButton"

    style.configure(nombre_estilo, background=color_fondo)  # type: ignore
    style.map(nombre_estilo, background=[("active", color_fondo)])

    btn_panel = ttk.Button(panel_paleta, style=nombre_estilo)
    btn_panel.grid(row=fila, column=columna, padx=5, pady=15)

    # Se usa .bind() para vincular el clic a la función controladora.
    # La lambda es necesaria para "capturar" el valor actual de color_fondo
    # y pasarlo como argumento a la función.
    btn_panel.bind(
        "<Button-1>",
        lambda event, c=color_fondo: on_color_seleccionado(event, c, style),
    )
