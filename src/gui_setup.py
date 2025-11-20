import ttkbootstrap as ttk


def crear_interfaz_completa(ventana: ttk.Window):
    #Panel para la seccion de herramientas
    panel_herramientas = ttk.Frame(ventana, width=400, bootstyle="success")

    #Panel seccion de paletas
    panel_paleta = ttk.Frame(
        panel_herramientas, bootstyle="light", width=400, height=1300
    )
    panel_paleta.pack_propagate(False)
    panel_paleta.pack()

    #Panel para manejo de archivos
    panel_manejo_archivos = ttk.Frame(panel_herramientas, bootstyle="primary")
    panel_manejo_archivos.pack(fill="both", expand=True)

    #Entrada y botones de panel manejo de archivos
    seccion_entrada_archivo = ttk.Labelframe(
        panel_manejo_archivos, text="Nombre del archivo", bootstyle="sec"
    )
    entrada_archivo = ttk.Entry(seccion_entrada_archivo)
    entrada_archivo.pack()

    btn_cargar = ttk.Button(panel_manejo_archivos, text="Cargar")
    btn_cargar.pack(side="bottom", anchor="center", pady=10)

    btn_guardar = ttk.Button(panel_manejo_archivos, text="Guardar")
    btn_guardar.pack(side="bottom", anchor="center", pady=10)

    seccion_entrada_archivo.pack(side="bottom", pady=10)

    #Mostrar el panel de herramientas
    panel_herramientas.pack(side="left", fill="y")

    #Panel del Lienzo
    panel_lienzo = ttk.Frame(ventana, bootstyle="success")
    panel_lienzo.pack(fill="both", expand=True)




# label_paleta = ttk.Label(panel_paleta,text="Paleta")

# label_paleta.pack(side="top")

# # creacion del panel de guardado
# panel_guardado = ttk.Frame(ventana)
# panel_guardado.pack(side="bottom", fill="both")

# frame_central = ttk.Frame(panel_guardado, bootstyle="dark")
# frame_central.pack(anchor="center", fill="x")

# creacion del panel de lienzo
# panel_lienzo.pack(anchor="nw")

# for fila in range(22):
#     for columna in range(50):
#         crear_btn_lienzo(panel_lienzo, fila, columna)


def crear_btn_lienzo(panel_lienzo: ttk.Frame, fila: int, columna: int):
    btn_lienzo = ttk.Button(panel_lienzo, width=1)

    btn_lienzo.grid(row=fila, column=columna, padx=3, pady=3)
