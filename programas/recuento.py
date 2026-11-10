#!/usr/bin/env python3
"""Cuenta uno a uno los casos de los retos de recuento del libro, para comprobar la regla que has encontrado.

Uso:
  python programas/recuento.py M-08-04
      escribe los primeros casos y cuenta todos (¡el total ya es la solución!).
  python programas/recuento.py M-08-04 --lista
      escribe todos los casos.
"""
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import cargar, salir  # noqa: E402


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--ayuda"):
        salir(__doc__, 0)
    d = cargar(argv[1], ("recuento",))["datos"]
    p, t = d["p"], d["plantilla"]
    if t == "codigos":
        casos = ["".join(map(str, c)) for c in itertools.permutations(range(1, p["n"] + 1), p["k"])]
        extra = f"De ellos, {sum(int(c[-1]) % 2 == 0 for c in casos)} son pares."
    elif t == "saludos":
        casos = [f"{a}-{b}" for a, b in itertools.combinations(range(1, p["n"] + 1), 2)]
        extra = ""
    else:
        casos = sorted({"".join(s) for s in itertools.permutations("D" * p["n"] + "A" * p["k"])})
        extra = "D es un paso a la derecha y A, un paso hacia arriba."
    lista = casos if "--lista" in argv else casos[:12]
    print("Casos: " + ", ".join(lista) + ("" if len(lista) == len(casos) else ", …"))
    print(f"Total: {len(casos)}. {extra}".strip())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
