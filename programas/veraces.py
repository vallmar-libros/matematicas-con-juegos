#!/usr/bin/env python3
"""Veraces y mentirosos: escribe la tabla de verdad con todos los casos de un reto del libro.

En cada fila, cada persona dice la verdad (V) o miente (M). Una frase «encaja» si es verdadera y la dice alguien que dice la
verdad, o si es falsa y la dice alguien que miente. La solución es la fila en la que encajan todas las frases.

Uso:
  python programas/veraces.py M-01-10
      escribe la tabla completa (¡la última columna te dice qué filas valen!).
  python programas/veraces.py M-01-10 "Ana, Carla y David"
      comprueba tu respuesta: escribe quiénes dicen la verdad.
"""
import itertools
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import cargar, salir  # noqa: E402


def verdad(frase, tipos):
    t = frase[0]
    if t == "es":
        return tipos[frase[2]] == frase[3]
    if t == "mismo":
        return (tipos[frase[2]] == tipos[frase[3]]) == frase[4]
    return sum(not x for x in tipos) == frase[2]


def encajan(frases, tipos):
    return [verdad(f, tipos) == tipos[f[1]] for f in frases]


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--ayuda"):
        salir(__doc__, 0)
    d = cargar(argv[1], ("veraces-mentirosos",))["datos"]
    nombres, frases = d["nombres"], d["frases"]
    if len(argv) > 2:
        dicen = {x.strip().capitalize() for x in re.split(r",| y ", argv[2]) if x.strip()}
        desconocidos = dicen - set(nombres)
        if desconocidos:
            salir("No conozco a: " + ", ".join(sorted(desconocidos)))
        tipos = [n in dicen for n in nombres]
        ok = encajan(frases, tipos)
        if all(ok):
            print("Respuesta correcta: con ese reparto encajan todas las frases.")
            return 0
        print("Tu respuesta no es correcta: con ese reparto no encaja la frase de " + ", ".join(
            nombres[f[1]] for f, b in zip(frases, ok) if not b) + ".")
        return 1
    print(" | ".join(nombres) + " || " + " | ".join(f"frase de {nombres[f[1]]}" for f in frases) + " || ¿encajan todas?")
    for tipos in itertools.product([True, False], repeat=len(nombres)):
        ok = encajan(frases, list(tipos))
        print(" | ".join("V" if t else "M" for t in tipos) + " || " + " | ".join("encaja" if b else "no" for b in ok)
              + " || " + ("SÍ" if all(ok) else "no"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
