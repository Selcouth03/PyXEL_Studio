"""Módulo de lógica de negocio y estado de la aplicación (Modelo).

Este módulo actúa como la única fuente de verdad para el estado de la aplicación.
Gestiona la matriz de colores del lienzo, el color actualmente seleccionado por
el usuario y la paleta de colores disponible.

No contiene lógica de interfaz de usuario ni de acceso a archivos, manteniendo
una alta cohesión y bajo acoplamiento.
"""

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

# Matriz que representa el estado de cada píxel en el lienzo.
matriz_colores: list[list[str]] = [
    ["#FFFFFF" for _ in range(COLUMNAS_LIENZO)] for _ in range(FILAS_LIENZO)
]
# Color seleccionado actualmente por el usuario.
color_actual: str = "#FFFFFF"


def actualizar_pixel(fila: int, columna: int, color: str) -> None:
    """Actualiza el color de un único píxel en la matriz de estado.

    Args:
        fila (int): El índice de la fila del píxel a actualizar.
        columna (int): El índice de la columna del píxel a actualizar.
        color (str): El nuevo color en formato hexadecimal (ej. "#FFFFFF").
    """
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
    """Devuelve una referencia a la matriz de colores completa."""
    return matriz_colores


def remplazar_matriz(nueva_matriz: list[list[str]]) -> None:
    """Reemplaza la matriz de estado actual con una nueva.

    Utilizado al cargar un archivo.

    Args:
        nueva_matriz (list[list[str]]): La nueva matriz de colores que
            reemplazará a la actual.
    """
    global matriz_colores
    matriz_colores = nueva_matriz
