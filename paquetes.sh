#!/usr/bin/bash
echo "-----------------------------------------------------"
echo "Iniciando instalación de los paquetes requeridos :)"
echo "-----------------------------------------------------"


sudo apt-get update && sudo apt-get upgrade -y
apt-get install python
apt-get install python-pip
pip install howdoi
pip install requests

echo "Loa paquetes han sido instalados con éxito por favor ejecute la herramienta con python3 preguntas.py"
