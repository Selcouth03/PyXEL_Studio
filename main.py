"""Punto de entrada principal para la aplicación PyXEL Studio.

Este script se encarga de inicializar la ventana principal de la aplicación,
configurar el tema y delegar la construcción de la interfaz de usuario al módulo
`gui_setup`.
"""

import ttkbootstrap as ttk
from src import gui_setup


def main() -> None:
    """Inicializa y ejecuta la aplicación PyXEL Studio.

    Crea la ventana principal, establece el tema 'superhero' de ttkbootstrap,
    asigna un título y luego llama a la función que construye todos los
    widgets y la lógica de la interfaz. Finalmente, inicia el bucle principal
    de la aplicación.
    """
    ventana = ttk.Window(themename="superhero", title="PyXEL STUDIO v1.0")
    gui_setup.crear_interfaz_completa(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
