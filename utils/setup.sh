#!/bin/bash

./utils/venv.sh

if [ -d ".venv" ]; then
    echo "venv creado con éxito."

    # Activar venv
    source .venv/bin/activate

    # Instalar librerías
    pip install flet
    pip install pandas

    echo "Librerías instaladas."

else
    echo "Hubo un problema ejecutando venv.sh."

fi