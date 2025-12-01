import csv
import re
from pathlib import Path
from typing import List, Union

from src.logic import COLUMNAS_LIENZO, FILAS_LIENZO

# Expresión regular para validar un código de color hexadecimal de 6 dígitos.
_HEX_COLOR_RE = re.compile(r"^#[0-9a-fA-F]{6}$")


def _es_color_hex_valido(color: str) -> bool:
    """Verifica si un string es un código de color hexadecimal válido."""
    return isinstance(color, str) and _HEX_COLOR_RE.match(color) is not None


def guardar_csv(
    nombre_archivo: str,
    matriz: List[List[str]],
    sobreescribir: bool = False,
) -> str:
    """Guarda la matriz del lienzo en un archivo CSV.

    Args:
        nombre_archivo (str): El nombre base del archivo a guardar.
        matriz (List[List[str]]): La matriz de colores que representa el lienzo.
        sobreescribir (bool, optional): Si es True, sobrescribe el archivo si
            ya existe. Defaults to False.

    Returns:
        str: Un código de estado: "exito", "nombre_vacio", "archivo_existe",
             o "error_escritura".
    """
    nombre_archivo = nombre_archivo.strip()
    if not nombre_archivo:
        return "nombre_vacio"

    # Añadimos la extensión .csv automáticamente
    nombre_archivo_con_extension = f"{nombre_archivo}.csv"

    try:
        directorio_actual = Path(__file__).resolve().parent
        directorio_assets = directorio_actual.parent / "assets"

        directorio_assets.mkdir(parents=True, exist_ok=True)

        ruta_archivo = directorio_assets / nombre_archivo_con_extension

        if ruta_archivo.is_file() and not sobreescribir:
            return "archivo_existe"

        with open(ruta_archivo, mode="w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(matriz)

        return "exito"

    except IOError:
        return "error_escritura"


def cargar_csv(nombre_archivo: str) -> Union[List[List[str]], str]:
    """Carga una matriz desde un archivo CSV en el directorio 'assets'.

    Args:
        nombre_archivo (str): El nombre base del archivo a cargar (sin extensión).

    Returns:
        Union[List[List[str]], str]: La matriz de colores si la carga es exitosa,
        o un código de error como string en caso contrario.
        Códigos de error:
        - "nombre_vacio": El nombre del archivo está en blanco.
        - "archivo_no_existe": El archivo no se encuentra en 'assets/'.
        - "archivo_vacio": El archivo existe pero está vacío.
        - "formato_invalido": El archivo no tiene las dimensiones correctas o
          contiene códigos de color no válidos.
        - "error_lectura": Ocurrió un error de E/S al leer el archivo.
    """
    nombre_archivo = nombre_archivo.strip()
    if not nombre_archivo:
        return "nombre_vacio"

    nombre_archivo_con_extension = f"{nombre_archivo}.csv"

    try:
        directorio_actual = Path(__file__).resolve().parent
        directorio_assets = directorio_actual.parent / "assets"
        ruta_archivo = directorio_assets / nombre_archivo_con_extension

        if not ruta_archivo.is_file():
            return "archivo_no_existe"

        if ruta_archivo.stat().st_size == 0:
            return "archivo_vacio"

        with open(ruta_archivo, mode="r", newline="") as archivo:
            lector = csv.reader(archivo)
            matriz_cargada: List[List[str]] = list(lector)

        # Validación de dimensiones
        if (
            not matriz_cargada
            or len(matriz_cargada) != FILAS_LIENZO
            or any(len(fila) != COLUMNAS_LIENZO for fila in matriz_cargada)
        ):
            return "formato_invalido"

        # Validación del contenido (códigos de color)
        if not all(
            _es_color_hex_valido(color) for fila in matriz_cargada for color in fila
        ):
            return "formato_invalido"

        return matriz_cargada

    except IOError:
        return "error_lectura"


def eliminar_csv(nombre_archivo: str) -> str:
    """Elimina un archivo CSV del directorio 'assets'.

    Args:
        nombre_archivo (str): El nombre base del archivo a eliminar (sin extensión).

    Returns:
        str: Un código de estado: "exito", "nombre_vacio", "archivo_no_existe",
             o "error_eliminacion".
    """
    nombre_archivo = nombre_archivo.strip()
    if not nombre_archivo:
        return "nombre_vacio"

    nombre_archivo_con_extension = f"{nombre_archivo}.csv"

    try:
        directorio_actual = Path(__file__).resolve().parent
        directorio_assets = directorio_actual.parent / "assets"
        ruta_archivo = directorio_assets / nombre_archivo_con_extension

        if not ruta_archivo.is_file():
            return "archivo_no_existe"

        ruta_archivo.unlink(missing_ok=True)

        return "exito"

    except OSError:
        return "error_eliminacion"
