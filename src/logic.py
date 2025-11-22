# --- Constantes de la Aplicación ---
FILAS_LIENZO = 32
COLUMNAS_LIENZO = 32

PALETA_COLORES = [
    # --- Escala de Grises ---
    "#FFFFFF",  # Blanco
    "#C0C0C0",  # Plata
    "#808080",  # Gris
    "#000000",  # Negro
    # --- Rojos, Rosas y Piel ---
    "#FFC0CB",  # Rosa
    "#FF0000",  # Rojo
    "#A52A2A",  # Marrón
    "#800000",  # Marrón (Maroon)
    # --- Naranjas y Amarillos ---
    "#F5DEB3",  # Trigo (Tono piel claro)
    "#D2691E",  # Chocolate (Tono piel oscuro)
    "#FFA500",  # Naranja
    "#FFD700",  # Dorado
    "#FFFF00",  # Amarillo
    # --- Verdes ---
    "#808000",  # Oliva
    "#00FF00",  # Lima
    "#008000",  # Verde Oscuro
    # --- Azules y Cianes ---
    "#ADD8E6",  # Azul Claro
    "#00FFFF",  # Cyan
    "#008080",  # Verde Azulado (Teal)
    "#0000FF",  # Azul
    "#000080",  # Azul Marino
    # --- Púrpuras y Magentas ---
    "#FF00FF",  # Magenta
    "#800080",  # Púrpura
    "#4B0082",  # Índigo (Púrpura oscuro)
]

# import file_manager

# Se inicializa la matriz directamente, haciendo innecesaria la función inicializar_matriz.
matriz_colores: list[list[str]] = [
    ["#FFFFFF" for _ in range(COLUMNAS_LIENZO)] for _ in range(FILAS_LIENZO)
]
# Se establece un color por defecto al iniciar la aplicación.
color_actual: str = "#FFFFFF"  # Negro


# La función se modifica para aceptar un color y no depender del estado global COLOR_ACTUAL.
def actualizar_pixel(fila: int, columna: int, color: str) -> None:
    if 0 <= fila < FILAS_LIENZO and 0 <= columna < COLUMNAS_LIENZO:
        matriz_colores[fila][columna] = color


def cambiar_color_seleccionado(nuevo_color: str) -> None:
    """Actualiza la variable global que almacena el color seleccionado."""
    global color_actual
    color_actual = nuevo_color


def obtener_color_actual() -> str:
    """Devuelve el color actualmente seleccionado."""
    return color_actual


def obtener_matriz_completa() -> list[list[str]]:
    return matriz_colores


def remplazar_matriz(nueva_matriz: list[list[str]]) -> None:
    global matriz_colores
    matriz_colores = nueva_matriz
