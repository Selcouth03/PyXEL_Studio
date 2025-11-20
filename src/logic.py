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