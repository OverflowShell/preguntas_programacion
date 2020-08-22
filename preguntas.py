#!/usr/bin/python3

import howdoi
import os
import time
import sys
from requests.exceptions import ConnectionError

# Colores
colores = {
        "M" :  "\033[1;31m",
        "H" :  "\033[1;32m",
        "K" :  "\033[1;33m",
        "U" :  "\033[1;34m",
        "P" :  "\033[1;35m",
        "C" :  "\033[1;36m",
        "W":  "\033[1;37m",
        "A" :  "\033[90m",

}

# Banner
def banner():
    print(colores["P"]+"""

             
    
________                                  _____               
___  __ \__________________ ____  __________  /______ ________
__  /_/ /_  ___/  _ \_  __ `/  / / /_  __ \  __/  __ `/_  ___/
_  ____/_  /   /  __/  /_/ // /_/ /_  / / / /_ / /_/ /_(__  ) 
/_/     /_/    \___/_\__, / \__,_/ /_/ /_/\__/ \__,_/ /____/  
                    /____/                                    


""")

banner()
time.sleep(0.5)

# Proceso :v
try:
    while True:
        pregunta = str(input(colores["K"]+"\tIngresa tu pregunta: "))
        print("")

        os.system("howdoi "+pregunta)
        time.sleep(2)
        print("")
except KeyboardInterrupt:
        print("[+]Proceso detenido por el usuario")
        sys.exit(1)
except ConnectionError:
        print("[+]Error de conexión")
        sys.exit(2)


