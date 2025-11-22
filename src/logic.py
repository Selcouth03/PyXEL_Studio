
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

import ttkbootstrap as ttk
import gui_setup
import file_manager

MATRIZ_COLORES: list[list[str]] = []
COLOR_ACTUAL: str = ""

def inicializar_matriz(filas: int, columnas: int):
    global MATRIZ_COLORES
    COLOR_POR_DEFECTO = "#FFFFF"

    MATRIZ_COLORES = [[COLOR_POR_DEFECTO for columna in range(columnas)]for fila in range(filas)]

def actualizar_pixel(fila:int, columnas:int) -> str:
    nuevo_color = COLOR_ACTUAL
    MATRIZ_COLORES[fila][columnas] = nuevo_color
    return nuevo_color

def cambiar_color_seleccionado(nuevo_color:str) -> None:
    global COLOR_ACTUAL
    COLOR_ACTUAL = nuevo_color

def obtener_color_actual() -> str:
    return COLOR_ACTUAL

def obtener_matriz_completa() -> list[list[str]]:
    return MATRIZ_COLORES

def remplazar_matriz(nueva_matriz:list[list[str]]) -> None:
    global MATRIZ_COLORES
    MATRIZ_COLORES = nueva_matriz

