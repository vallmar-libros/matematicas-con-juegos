#!/usr/bin/env python3
"""Juega contra el ordenador a la carrera al número o a los montones de fichas, o comprueba tu estrategia.

El ordenador juega lo mejor posible: si tu estrategia le gana, es que funciona.

Uso:
  python programas/rival.py M-05-09
      partida contra el ordenador; te pregunta quién empieza y tus jugadas.
  python programas/rival.py M-05-09 --comprobar "3, 7, 11, 15"
      carrera: comprueba que diciendo esos números ganas siempre, juegue lo que juegue el rival.
  python programas/rival.py M-05-04 --comprobar "3 4"
      montones: comprueba que quitando 4 fichas del montón 3 ganas si después sigues jugando bien.
"""
import random
import sys
from pathlib import Path
from functools import lru_cache

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import cargar, salir  # noqa: E402


# ------------------------------------------------------------ carrera al número


def carrera_gana(N, k):
    """gana[t] = quien tiene que jugar cuando el último número dicho es t puede ganar."""
    gana = {N: False}
    for t in range(N - 1, -1, -1):
        gana[t] = any(not gana[t + m] for m in range(1, k + 1) if t + m <= N)
    return gana


def comprobar_carrera(N, k, claves):
    claves = sorted(set(claves))
    if not claves or claves[-1] != N:
        return f"Tu lista tiene que acabar en {N}: gana quien lo dice."

    def responde(t):   # tu jugada cuando el rival ha dicho t
        alcanzables = [c for c in claves if t < c <= t + k]
        return alcanzables[0] if alcanzables else None

    empiezas = claves[0] <= k
    pendientes = [0] if empiezas else [m for m in range(1, k + 1)]
    for t in pendientes:
        estado = [t]
        while estado:
            t = estado.pop()
            mio = responde(t)
            if mio is None:
                return f"Si el rival dice {t}, ninguno de tus números está a tu alcance (de {t + 1} a {min(t + k, N)})."
            if mio == N:
                continue
            for m in range(1, k + 1):
                if mio + m <= N:
                    if mio + m == N:
                        return f"Después de que digas {mio}, el rival puede decir {N} y gana."
                    estado.append(mio + m)
    return None


def jugar_carrera(N, k, rng):
    gana = carrera_gana(N, k)
    quien = input("¿Quién empieza? Escribe yo o programa: ").strip().lower()
    t, turno = 0, ("yo" if quien.startswith("y") else "programa")
    while t < N:
        if turno == "programa":
            buenas = [t + m for m in range(1, k + 1) if t + m <= N and not gana[t + m]]
            t = buenas[0] if buenas else t + rng.randint(1, min(k, N - t))
            print(f"El programa dice {t}.")
            if t == N:
                print("Ha ganado el programa.")
                return 1
            turno = "yo"
        else:
            x = input(f"Tu número (de {t + 1} a {min(t + k, N)}): ").strip()
            if not x.isdigit() or not t < int(x) <= min(t + k, N):
                print("Esa jugada no vale.")
                continue
            t = int(x)
            if t == N:
                print("¡Has ganado!")
                return 0
            turno = "programa"
    return 0


# ------------------------------------------------------------ montones de fichas


@lru_cache(maxsize=None)
def nim_gana(estado):
    for i, m in enumerate(estado):
        for q in range(1, m + 1):
            nuevo = list(estado)
            nuevo[i] -= q
            if not nim_gana(tuple(sorted(nuevo))):
                return True
    return False


def comprobar_nim(montones, jugada):
    try:
        i, q = [int(x) for x in jugada.replace(",", " ").split()]
    except ValueError:
        return "Escribe la jugada como «montón fichas», por ejemplo \"3 4\"."
    if not 1 <= i <= len(montones) or not 1 <= q <= montones[i - 1]:
        return "Esa jugada no vale: no hay tantas fichas en ese montón."
    nuevo = list(montones)
    nuevo[i - 1] -= q
    if nim_gana(tuple(sorted(nuevo))):
        return f"Después de esa jugada quedan {nuevo}: el rival puede ganar si juega bien."
    return None


def jugar_nim(montones, rng):
    m = list(montones)
    quien = input("¿Quién empieza? Escribe yo o programa: ").strip().lower()
    turno = "yo" if quien.startswith("y") else "programa"
    while sum(m):
        print("Montones:", " ".join(str(x) for x in m))
        if turno == "programa":
            jugadas = [(i, q) for i in range(len(m)) for q in range(1, m[i] + 1)]
            buenas = [(i, q) for i, q in jugadas if not nim_gana(tuple(sorted(m[:i] + [m[i] - q] + m[i + 1:])))]
            i, q = buenas[0] if buenas else rng.choice(jugadas)
            m[i] -= q
            print(f"El programa quita {q} del montón {i + 1}.")
            if not sum(m):
                print("Ha ganado el programa.")
                return 1
            turno = "yo"
        else:
            x = input("Tu jugada (montón y fichas, por ejemplo 2 3): ").replace(",", " ").split()
            if len(x) != 2 or not all(v.isdigit() for v in x) or not 1 <= int(x[0]) <= len(m) or not 1 <= int(x[1]) <= m[int(x[0]) - 1]:
                print("Esa jugada no vale.")
                continue
            m[int(x[0]) - 1] -= int(x[1])
            if not sum(m):
                print("¡Has ganado!")
                return 0
            turno = "programa"
    return 0


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--ayuda"):
        salir(__doc__, 0)
    r = cargar(argv[1], ("carrera-n", "nim"))
    d = r["datos"]
    if "--comprobar" in argv:
        arg = argv[argv.index("--comprobar") + 1]
        if r["tipo"] == "carrera-n":
            claves = [int(x) for x in arg.replace(",", " ").split() if x.isdigit()]
            fallo = comprobar_carrera(d["N"], d["k"], claves)
        else:
            fallo = comprobar_nim(d["montones"], arg)
        if fallo:
            print("Tu estrategia no gana siempre:", fallo)
            return 1
        print("Tu estrategia gana siempre, juegue lo que juegue el rival.")
        return 0
    rng = random.Random()
    try:
        return jugar_carrera(d["N"], d["k"], rng) if r["tipo"] == "carrera-n" else jugar_nim(d["montones"], rng)
    except EOFError:
        return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
