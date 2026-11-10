"""Funciones comunes de los programas de comprobación de «Matemáticas con juegos» (Leo Vallmar).
Solo usan la biblioteca estándar de Python 3.8 o posterior."""
import json
import sys
from pathlib import Path

RETOS = Path(__file__).resolve().parent.parent / "datos" / "retos.json"


def cargar(codigo, tipos=None):
    """Datos de un reto del libro por su código (por ejemplo, M-01-02)."""
    retos = json.loads(RETOS.read_text(encoding="utf-8"))["retos"]
    codigo = codigo.strip().upper()
    if codigo not in retos:
        salir(f"No hay ningún reto con el código {codigo}. Los códigos son como M-01-02.")
    r = retos[codigo]
    if tipos and r["tipo"] not in tipos:
        salir(f"El reto {codigo} es de tipo «{r['tipo']}» y este programa no lo comprueba.")
    return r


def salir(msg, codigo=2):
    print(msg)
    sys.exit(codigo)


def leer_rejilla(txt):
    """«1 2 4 3 / 4 3 1 2 / …» → [[1, 2, 4, 3], [4, 3, 1, 2], …]. Las casillas negras se escriben con - o —."""
    filas = []
    for f in txt.replace("—", "-").replace("–", "-").split("/"):
        fila = []
        for x in f.split():
            if x in ("-", "#"):
                fila.append(0)
            elif x.isdigit():
                fila.append(int(x))
            else:
                salir(f"No entiendo «{x}»: escribe cifras separadas por espacios y las filas separadas por /.")
        filas.append(fila)
    return filas
