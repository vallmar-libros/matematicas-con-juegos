#!/usr/bin/env python3
"""Comprueba tu respuesta a una rejilla del libro: rejilla de cifras, rejilla de jaulas o sumas cruzadas.

Uso:
  python programas/rejillas.py M-01-01 "1 2 4 3 / 4 3 1 2 / 2 1 3 4 / 3 4 2 1"
      dice si tu rejilla cumple todas las reglas del reto y, si no, cuál falla.
  python programas/rejillas.py M-01-01 --contar
      cuenta las soluciones del reto (deben ser exactamente 1). ¡Ojo: si hay una, te la enseña!
En las sumas cruzadas, escribe las casillas negras con un guion: "5 1 - / 3 2 1 / - 9 3".
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import cargar, leer_rejilla, salir  # noqa: E402

TIPOS = ("rejilla-cifras", "rejilla-jaulas", "sumas-cruzadas")
CAJAS = {4: (2, 2), 6: (2, 3), 9: (3, 3)}


# ------------------------------------------------------------ reglas


def fallos_latino(g, n):
    p = []
    for i in range(n):
        if sorted(g[i]) != list(range(1, n + 1)):
            p.append(f"la fila {i + 1} no tiene las cifras del 1 al {n} una vez cada una")
        if sorted(g[f][i] for f in range(n)) != list(range(1, n + 1)):
            p.append(f"la columna {i + 1} no tiene las cifras del 1 al {n} una vez cada una")
    return p


def jaula_ok(op, valor, vals):
    if op == "=":
        return vals[0] == valor
    if op == "+":
        return sum(vals) == valor
    if op == "x":
        return math.prod(vals) == valor
    a, b = max(vals), min(vals)
    return a - b == valor if op == "-" else a == b * valor


SIMBOLO = {"+": "+", "-": "−", "x": "×", "/": ":", "=": ""}


def fallos(r, g):
    d, t = r["datos"], r["tipo"]
    if t == "sumas-cruzadas":
        pl = d["plantilla"]
        if [len(f) for f in g] != [len(f) for f in pl]:
            return [f"la rejilla debe tener {len(pl)} filas de {len(pl[0])} casillas"]
        p = []
        for f, fila in enumerate(pl):
            for c, ch in enumerate(fila):
                if ch == "#" and g[f][c]:
                    p.append(f"la casilla de la fila {f + 1}, columna {c + 1} es negra: escribe un guion")
                if ch == "." and not 1 <= g[f][c] <= 9:
                    p.append(f"la casilla de la fila {f + 1}, columna {c + 1} necesita una cifra del 1 al 9")
        for tr in d["tramos"]:
            vals = [g[f][c] for f, c in tr["celdas"]]
            donde = f"el tramo {'horizontal' if tr['dir'] == 'h' else 'vertical'} que empieza en la fila {tr['celdas'][0][0] + 1}, columna {tr['celdas'][0][1] + 1}"
            if sum(vals) != tr["suma"]:
                p.append(f"{donde} suma {sum(vals)} y debe sumar {tr['suma']}")
            if len(set(vals)) != len(vals):
                p.append(f"{donde} repite una cifra")
        return p
    n = d["n"]
    if len(g) != n or any(len(f) != n for f in g):
        return [f"la rejilla debe tener {n} filas de {n} cifras"]
    p = fallos_latino(g, n)
    if t == "rejilla-cifras":
        for f in range(n):
            for c in range(n):
                if d["puzzle"][f][c] and d["puzzle"][f][c] != g[f][c]:
                    p.append(f"la casilla de la fila {f + 1}, columna {c + 1} ya venía con un {d['puzzle'][f][c]}")
        bf, bc = CAJAS[n]
        for f0 in range(0, n, bf):
            for c0 in range(0, n, bc):
                caja = sorted(g[f][c] for f in range(f0, f0 + bf) for c in range(c0, c0 + bc))
                if caja != list(range(1, n + 1)):
                    p.append(f"la caja que empieza en la fila {f0 + 1}, columna {c0 + 1} repite una cifra")
    else:
        for j in d["jaulas"]:
            vals = [g[f][c] for f, c in j["celdas"]]
            if not jaula_ok(j["op"], j["valor"], vals):
                f, c = j["celdas"][0]
                p.append(f"la jaula «{j['valor']}{SIMBOLO[j['op']]}» que empieza en la fila {f + 1}, columna {c + 1} no da {j['valor']}")
    return p


# ------------------------------------------------------------ contar soluciones (búsqueda con vuelta atrás)


def contar(r, tope=2):
    d, t = r["datos"], r["tipo"]
    if t == "sumas-cruzadas":
        pl = d["plantilla"]
        celdas = [(f, c) for f in range(len(pl)) for c in range(len(pl[0])) if pl[f][c] == "."]
        g = [[0] * len(pl[0]) for _ in pl]
        de = {x: [tr for tr in d["tramos"] if list(x) in tr["celdas"]] for x in celdas}

        def ok(tr):
            vals = [g[f][c] for f, c in tr["celdas"] if g[f][c]]
            if len(set(vals)) != len(vals):
                return False
            falta = len(tr["celdas"]) - len(vals)
            libres = sorted(set(range(1, 10)) - set(vals))
            if falta == 0:
                return sum(vals) == tr["suma"]
            return sum(vals) + sum(libres[:falta]) <= tr["suma"] <= sum(vals) + sum(libres[-falta:])
    else:
        n = d["n"]
        celdas = [(f, c) for f in range(n) for c in range(n)]
        g = [list(f) for f in d["puzzle"]] if t == "rejilla-cifras" else [[0] * n for _ in range(n)]
        jaula_de = {}
        for j in d.get("jaulas", []):
            for f, c in j["celdas"]:
                jaula_de[(f, c)] = j

        def ok(_):
            return True
    sols = []

    def rec(k):
        if len(sols) >= tope:
            return
        if k == len(celdas):
            sols.append([list(f) for f in g])
            return
        f, c = celdas[k]
        if t == "rejilla-cifras" and d["puzzle"][f][c]:
            rec(k + 1)
            return
        for v in range(1, 10 if t == "sumas-cruzadas" else d["n"] + 1):
            if t != "sumas-cruzadas":
                if v in g[f] or any(g[i][c] == v for i in range(d["n"])):
                    continue
                if t == "rejilla-cifras":
                    bf, bc = CAJAS[d["n"]]
                    f0, c0 = f - f % bf, c - c % bc
                    if any(g[a][b] == v for a in range(f0, f0 + bf) for b in range(c0, c0 + bc)):
                        continue
            g[f][c] = v
            bien = True
            if t == "sumas-cruzadas":
                bien = all(ok(tr) for tr in de[(f, c)])
            elif t == "rejilla-jaulas":
                j = jaula_de[(f, c)]
                vals = [g[a][b] for a, b in j["celdas"] if g[a][b]]
                if len(vals) == len(j["celdas"]):
                    bien = jaula_ok(j["op"], j["valor"], vals)
                elif j["op"] == "+":
                    bien = sum(vals) < j["valor"]
                elif j["op"] == "x":
                    bien = j["valor"] % math.prod(vals) == 0
            if bien:
                rec(k + 1)
            g[f][c] = 0

    rec(0)
    return sols


def main(argv):
    if len(argv) < 3 or argv[1] in ("-h", "--ayuda"):
        salir(__doc__, 0)
    r = cargar(argv[1], TIPOS)
    if argv[2] == "--contar":
        sols = contar(r)
        if not sols:
            print("Este reto no tiene solución.")
        elif len(sols) == 1:
            print("Este reto tiene una sola solución:")
            print(" / ".join(" ".join(str(v) if v else "-" for v in f) for f in sols[0]))
        else:
            print("Este reto tiene más de una solución.")
        return 0
    p = fallos(r, leer_rejilla(argv[2]))
    if p:
        print("Tu respuesta no es correcta:")
        for x in p:
            print(" -", x)
        return 1
    print("Respuesta correcta: cumple todas las reglas del reto.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
