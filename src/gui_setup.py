"""Módulo para la construcción de la interfaz de usuario (Vista y Controlador).

Este módulo es responsable de crear todos los widgets de la interfaz gráfica
utilizando ttkbootstrap. También contiene las funciones controladoras que
responden a los eventos del usuario (clics de botón, etc.), conectando la
interfaz con la lógica de negocio (`logic`) y la persistencia de archivos
(`file_manager`).
"""

import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from . import logic
from . import file_manager

# Las constantes de la paleta se mantienen para la construcción de la GUI.
FILAS_PALETA = 8
COLUMNAS_PALETA = 3


def crear_interfaz_completa(ventana: ttk.Window):
    """Construye y orquesta la creación de toda la interfaz gráfica de la aplicación."""
    ventana.geometry(f"{ventana.winfo_screenwidth()}x{ventana.winfo_screenheight()}")
    style = ttk.Style()

    panel_lateral = _crear_panel_lateral(ventana)
    lienzo = _crear_lienzo(ventana)

    # --- Rellenar el panel lateral ---
    _crear_seccion_color_actual(panel_lateral, style)
    _crear_separador(panel_lateral, style)
    _crear_seccion_paleta(panel_lateral, style)
    _crear_seccion_limpieza(panel_lateral, lienzo)
    _crear_seccion_archivos(panel_lateral, ventana, lienzo)


def _crear_panel_lateral(ventana: ttk.Window) -> ttk.Frame:
    """Crea el panel lateral principal que contiene los controles."""
    panel_lateral = ttk.Frame(ventana, style="secondary", width=400)
    panel_lateral.pack_propagate(False)
    panel_lateral.pack(side="left", fill="y")
    return panel_lateral


def _crear_lienzo(ventana: ttk.Window) -> ttk.Canvas:
    """Crea el lienzo principal para dibujar."""
    lienzo = ttk.Canvas(ventana, background="white", highlightthickness=0)
    lienzo.pack(fill="both", expand=True)
    lienzo.bind("<Configure>", lambda _event: crear_grid_lienzo(lienzo))
    lienzo.bind(
        "<Button-1>",
        lambda event: on_lienzo_click(event, lienzo, logic.obtener_color_actual()),
    )
    return lienzo


def _crear_seccion_color_actual(parent: ttk.Frame, style: ttk.Style):
    """Crea la sección de UI que muestra el color actualmente seleccionado."""
    frame_color_actual = ttk.Frame(parent, bootstyle="secondary")
    frame_color_actual.pack(side="top", pady=20, fill="x", padx=10)

    label_color_actual = ttk.Label(
        frame_color_actual, text="Color seleccionado", style="secondary.Inverse.TLabel"
    )
    label_color_actual.pack()

    # Estilo y creación del cuadro que muestra el color actual
    style.configure(
        "EstiloCuadro.TButton",
        font=(None, 18),
        width=5,
        background=logic.color_actual,
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
    cuadro_color_actual = ttk.Button(frame_color_actual, style="EstiloCuadro.TButton")
    cuadro_color_actual.pack(pady=10)


def _crear_separador(parent: ttk.Frame, style: ttk.Style):
    """Crea un separador visual."""
    color_separador = style.lookup("light.TFrame", "background")
    style.configure("ColorContraste.TSeparator", background=color_separador)
    separador = ttk.Separator(parent, style="ColorContraste.TSeparator")
    separador.pack(side="top", pady=10, fill="x", padx=20)


def _crear_seccion_paleta(parent: ttk.Frame, style: ttk.Style):
    """Crea la sección de UI que contiene la paleta de colores."""
    frame_paleta = ttk.Frame(parent, style="secondary")
    frame_paleta.pack(side="top", fill="x", padx=10, pady=20, anchor="n")

    for j in range(COLUMNAS_PALETA):
        frame_paleta.columnconfigure(j, weight=1)

    style.configure("Paleta.TButton", relief="flat", padding=(25, 10), borderwidth=0)

    # Crear botones de la paleta
    for i in range(FILAS_PALETA):
        for j in range(COLUMNAS_PALETA):
            indice = i * COLUMNAS_PALETA + j
            crear_btn_paleta(
                panel_paleta=frame_paleta, style=style, fila=i, columna=j, indice=indice
            )


def _crear_seccion_limpieza(parent: ttk.Frame, lienzo: ttk.Canvas):
    """Crea la sección con el botón para limpiar el lienzo."""
    frame_limpieza = ttk.Frame(parent, bootstyle="secondary")
    frame_limpieza.pack(side="top", fill="x", padx=10, pady=10)

    btn_limpiar = ttk.Button(
        frame_limpieza,
        text="Limpiar Lienzo",
        bootstyle="light",
    )
    btn_limpiar.pack(fill="x")
    btn_limpiar.bind(
        "<Button-1>",
        lambda _event: on_limpiar_lienzo(lienzo),
    )


def _crear_seccion_archivos(parent: ttk.Frame, ventana: ttk.Window, lienzo: ttk.Canvas):
    """Crea la sección de UI para guardar, cargar y eliminar archivos."""
    panel_archivos = ttk.Frame(parent, bootstyle="secondary")
    panel_archivos.pack(fill="x", side="bottom", pady=20)

    seccion_entrada = ttk.Labelframe(
        panel_archivos, text="Nombre del archivo", bootstyle="sec"
    )
    seccion_entrada.pack(side="top", pady=10)

    entrada_archivo = ttk.Entry(seccion_entrada)
    entrada_archivo.pack()

    btn_guardar = ttk.Button(panel_archivos, text="Guardar")
    btn_guardar.pack(side="top", anchor="center", pady=10)
    btn_guardar.bind(
        "<Button-1>",
        lambda _event: atrapar_nombre_archivo(entrada_archivo, ventana),
    )

    btn_cargar = ttk.Button(panel_archivos, text="Cargar")
    btn_cargar.pack(side="top", anchor="center", pady=10)
    btn_cargar.bind(
        "<Button-1>",
        lambda _evento: cargar_archivo_guardado(entrada_archivo, ventana, lienzo),
    )

    btn_eliminar = ttk.Button(panel_archivos, text="Eliminar", bootstyle="danger")
    btn_eliminar.pack(side="top", anchor="center", pady=10)
    btn_eliminar.bind(
        "<Button-1>",
        lambda _evento: eliminar_archivo_guardado(entrada_archivo, ventana, lienzo),
    )


def on_limpiar_lienzo(lienzo: ttk.Canvas):
    """Limpia el lienzo y lo restablece a su estado inicial (blanco)."""
    logic.limpiar_lienzo()
    crear_grid_lienzo(lienzo)


def on_color_seleccionado(_event, color: str, style: ttk.Style):  # type: ignore
    """
    Controlador de evento para cuando se selecciona un color de la paleta.
    Actualiza el estado de la lógica y la GUI para reflejar el nuevo color.
    """
    logic.cambiar_color_seleccionado(color)
    style.configure("EstiloCuadro.TButton", background=color)  # pyright: ignore[reportUnknownMemberType]
    style.map(
        "EstiloCuadro.TButton",
        background=[("active", color)],
        bordercolor=[("active", color)],
        lightcolor=[("active", color)],
        darkcolor=[("active", color)],
    )


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
    if indice >= len(logic.PALETA_COLORES):
        return  # No crear botón si no hay color para él

    color_fondo = logic.PALETA_COLORES[indice]
    nombre_estilo = f"Color{indice}.Paleta.TButton"

    style.configure(nombre_estilo, background=color_fondo)  # type: ignore
    style.map(nombre_estilo, background=[("active", color_fondo)])

    btn_panel = ttk.Button(panel_paleta, style=nombre_estilo)
    btn_panel.grid(row=fila, column=columna, padx=5, pady=15)
    btn_panel.bind(
        "<Button-1>",
        lambda _event, c=color_fondo: on_color_seleccionado(_event, c, style),
    )


def atrapar_nombre_archivo(entrada_archivo: ttk.Entry, ventana: ttk.Window):
    """
    Controlador para el botón Guardar. Gestiona la lógica de guardado y la
    retroalimentación al usuario.
    """
    nombre = entrada_archivo.get()
    matriz_a_guardar = logic.obtener_matriz_completa()

    # 1. Primer intento de guardado (sin sobreescribir)
    estado = file_manager.guardar_csv(nombre, matriz_a_guardar, sobreescribir=False)

    # 2. Gestionar si el archivo ya existe
    if estado == "archivo_existe":
        confirmar = Messagebox.okcancel(
            parent=ventana,
            title="Confirmar Sobrescritura",
            message=f"El archivo '{nombre}.csv' ya existe.\n¿Desea sobrescribirlo?",
        )
        if confirmar:
            # Si el usuario confirma, se intenta guardar de nuevo forzando la sobreescritura
            estado = file_manager.guardar_csv(
                nombre, matriz_a_guardar, sobreescribir=True
            )
        else:
            # Si el usuario cancela, la operación termina aquí.
            return

    # 3. Mostrar resultado final de la operación
    if estado == "exito":
        Messagebox.showinfo(
            parent=ventana,
            title="Guardado Exitoso",
            message=f"El lienzo se ha guardado como '{nombre}.csv'.",
        )
        entrada_archivo.delete(0, "end")
    elif estado == "nombre_vacio":
        Messagebox.show_warning(
            parent=ventana,
            title="Nombre inválido",
            message="El nombre del archivo no puede estar vacío.",
        )
    elif estado == "error_escritura":
        Messagebox.show_error(
            parent=ventana,
            title="Error de Guardado",
            message="Ocurrió un error inesperado al intentar guardar el archivo.",
        )


def cargar_archivo_guardado(
    entrada_archivo: ttk.Entry, ventana: ttk.Window, lienzo: ttk.Canvas
):
    """
    Controlador para el botón Cargar. Gestiona la lógica de carga y la
    retroalimentación al usuario.
    """
    nombre = entrada_archivo.get()
    resultado = file_manager.cargar_csv(nombre)

    # Caso de éxito: el resultado es una lista (la matriz)
    if isinstance(resultado, list):
        logic.remplazar_matriz(resultado)
        crear_grid_lienzo(lienzo)
        Messagebox.showinfo(
            parent=ventana,
            title="Carga Exitosa",
            message=f"Se ha cargado el lienzo desde '{nombre}.csv'.",
        )
        entrada_archivo.delete(0, "end")
        return

    # Casos de error: el resultado es un string con un código
    if resultado == "nombre_vacio":
        Messagebox.show_warning(
            parent=ventana,
            title="Nombre inválido",
            message="El nombre del archivo no puede estar vacío.",
        )
    elif resultado == "archivo_no_existe":
        Messagebox.show_warning(
            parent=ventana,
            title="Archivo no encontrado",
            message=f"El archivo '{nombre}.csv' no fue encontrado.",
        )
    elif resultado == "archivo_vacio":
        Messagebox.show_warning(
            parent=ventana,
            title="Archivo Vacío",
            message=f"El archivo '{nombre}.csv' está vacío y no se puede cargar.",
        )
    elif resultado == "formato_invalido":
        Messagebox.show_error(
            parent=ventana,
            title="Formato Inválido",
            message=f"El archivo '{nombre}.csv' está corrupto o no tiene el formato esperado (32x32, colores hexadecimales).",
        )
    elif resultado == "error_lectura":
        Messagebox.show_error(
            parent=ventana,
            title="Error de Carga",
            message="Ocurrió un error inesperado al intentar cargar el archivo.",
        )


def eliminar_archivo_guardado(
    entrada_archivo: ttk.Entry, ventana: ttk.Window, lienzo: ttk.Canvas
):
    """
    Controlador para el botón Eliminar. Gestiona la lógica de eliminación y la
    retroalimentación al usuario.
    """
    nombre = entrada_archivo.get()

    if not nombre:
        Messagebox.show_warning(
            parent=ventana,
            title="Nombre inválido",
            message="El nombre del archivo no puede estar vacío.",
        )
        return

    confirmar = Messagebox.okcancel(
        parent=ventana,
        title="Confirmar Eliminación",
        message=f"¿Está seguro de que desea eliminar el archivo '{nombre}.csv'?\nEsta acción no se puede deshacer.",
        alert=True,
    )

    if not confirmar:
        return

    resultado = file_manager.eliminar_csv(nombre)

    if resultado == "exito":
        logic.remplazar_matriz(logic.crear_matriz_inicial())
        crear_grid_lienzo(lienzo)
        Messagebox.showinfo(
            parent=ventana,
            title="Eliminación Exitosa",
            message=f"El archivo '{nombre}.csv' ha sido eliminado.",
        )
        entrada_archivo.delete(0, "end")
    elif resultado == "archivo_no_existe":
        Messagebox.show_warning(
            parent=ventana,
            title="Archivo no encontrado",
            message=f"El archivo '{nombre}.csv' no fue encontrado.",
        )
    elif resultado == "error_eliminacion":
        Messagebox.show_error(
            parent=ventana,
            title="Error de Eliminación",
            message="Ocurrió un error inesperado al intentar eliminar el archivo.",
        )
