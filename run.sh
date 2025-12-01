#!/bin/bash

# Encontrar la ruta de la librería Tcl dinámicamente
tcl_path=$(echo 'puts $tcl_library' | tclsh)

# Encontrar la ruta de la librería Tk dinámicamente usando tclsh
tk_path=$(echo 'package require Tk; wm withdraw .; puts $tk_library; exit' | tclsh)

# Verificar si las rutas se encontraron
if [ -z "$tcl_path" ] || [ -z "$tk_path" ]; then
    echo "Error: No se pudieron encontrar las librerías Tcl o Tk."
    echo "Asegúrate de que Tcl y Tk estén instalados correctamente."
    exit 1
fi

# Ejecutar la aplicación con las rutas encontradas
TCL_LIBRARY="$tcl_path" TK_LIBRARY="$tk_path" uv run main.py
