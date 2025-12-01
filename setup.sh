#!/bin/bash

# --- Script de Configuración de PyXEL Studio ---
# Este script verifica e instala todas las dependencias necesarias
# tanto del sistema (Tkinter) como de Python (usando uv).

echo "--- 🚀 Iniciando configuración de PyXEL Studio ---"
echo ""

# --- PASO 1: VERIFICAR E INSTALAR TKINTER ---
echo "➡️  Paso 1 de 3: Verificando la dependencia del sistema 'Tkinter'..."

if python3 -c "import tkinter" &> /dev/null; then
    echo "✅ Tkinter ya está instalado y funcionando correctamente."
else
    echo "⚠️  Tkinter no está instalado o no funciona. Se requiere instalación."
    
    # Detectar el sistema operativo
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS_ID=$ID
    else
        echo "❌ No se pudo detectar la distribución de Linux. Por favor, instala 'python3-tk' o 'tk-dev' manually y vuelve a ejecutar el script."
        exit 1
    fi

    # Lógica de instalación por SO
    if [[ "$OS_ID" == "ubuntu" || "$OS_ID" == "debian" || "$ID_LIKE" == *"debian"* || "$ID_LIKE" == *"ubuntu"* ]]; then
        echo "   -> Sistema Debian/Ubuntu detectado."
        echo "   -> Instalando 'python3-tk' (paquete minimalista confirmado)..."
        sudo apt-get update > /dev/null && sudo apt-get install -y python3-tk

    elif [[ "$OS_ID" == "fedora" || "$OS_ID" == "rhel" ]]; then
        echo "   -> Sistema Fedora/RHEL detectado. Instalando 'python3-tkinter'..."
        sudo dnf install -y python3-tkinter
    
    elif [[ "$OS_ID" == "arch" ]]; then
        echo "   -> Sistema Arch Linux detectado. Instalando 'tk'..."
        sudo pacman -S --noconfirm tk
    
    else
        echo "❌ Tu sistema operativo ($OS_ID) no es compatible con este script de instalación automática."
        echo "   Por favor, consulta el README.md para instalar Tkinter manualmente."
        exit 1
    fi

    # Verificación final
    if python3 -c "import tkinter" &> /dev/null; then
        echo "✅ Tkinter se ha instalado correctamente en el sistema."
    else
        echo "❌ La instalación automática de Tkinter ha fallado. Revisa los mensajes de error."
        echo "   Puede que necesites buscar cómo instalar Tk para tu versión específica de Python y sistema operativo."
        exit 1
    fi
fi
echo ""

# --- PASO 2: VERIFICAR E INSTALAR UV ---
echo "➡️  Paso 2 de 3: Verificando el gestor de paquetes 'uv'..."

if command -v uv &> /dev/null; then
    echo "✅ 'uv' ya está instalado."
else
    echo "⚠️  'uv' no encontrado. Instalando la última versión a través de Astral..."
    if curl -LsSf https://astral.sh/uv/install.sh | sh; then
        # Añadir uv al PATH para la sesión actual
        source "$HOME/.cargo/env"
        echo "✅ 'uv' se ha instalado correctamente."
    else
        echo "❌ La instalación de 'uv' ha fallado. Por favor, instálalo manualmente desde https://astral.sh"
        exit 1
    fi
fi
echo ""

# --- PASO 3: SINCRONIZAR DEPENDENCIAS DE PYTHON ---
echo "➡️  Paso 3 de 3: Sincronizando las dependencias de Python con 'uv'..."

if uv sync; then
    echo "✅ Las dependencias de Python se han instalado correctamente."
else
    echo "❌ La sincronización con 'uv sync' ha fallado. Revisa los errores."
    exit 1
fi
echo ""

# --- FINALIZACIÓN ---
echo "--- 🎉 Configuración completada con éxito ---"
echo ""
echo "Todo está listo para empezar. Para ejecutar la aplicación, usa el siguiente comando:"
echo "bash run.sh"
echo ""
