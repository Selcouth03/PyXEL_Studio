import ttkbootstrap as ttk
import src.gui_setup


def main():
    ventana = ttk.Window(themename="litera", title="PyXEL STUDIO v1.0")

    src.gui_setup.crear_interfaz_completa(ventana)

    ventana.mainloop()


main()
