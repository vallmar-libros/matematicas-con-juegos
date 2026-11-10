#!/usr/bin/env python3
"""Simula los retos de azar del libro (¿es justo?, la suma más probable, dados que se ganan en círculo y bolas sin devolver)
y cuenta todos los casos posibles.

Uso:
  python programas/azar.py M-05-01
      simula 100 tiradas (o 1000 extracciones) y cuenta cuántas veces pasa cada cosa.
  python programas/azar.py M-05-01 --tiradas 5000 --semilla 7
      más tiradas; con la misma semilla sale siempre la misma simulación.
  python programas/azar.py M-05-01 --exacto
      cuenta todos los casos posibles y da las probabilidades exactas, en fracción. ¡Esto ya es la solución!
"""
import itertools
import random
import sys
from pathlib import Path
from collections import Counter
from fractions import Fraction

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import cargar, salir  # noqa: E402

TIPOS = ("dados-justo", "suma-probable", "dados-no-transitivos", "probabilidad-compuesta")
OPERACION = {"suma": lambda a, b: a + b, "producto": lambda a, b: a * b, "diferencia": lambda a, b: abs(a - b)}


def gana(regla, r):
    t = regla[0]
    if t == "par":
        return r % 2 == 0
    if t == "impar":
        return r % 2 == 1
    if t == "menor_igual":
        return r <= regla[1]
    if t == "mayor":
        return r > regla[1]
    if t == "multiplo":
        return r % regla[1] == 0
    return r in regla[1]


def fr(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def opciones(argv):
    tiradas, semilla = None, None
    if "--tiradas" in argv:
        tiradas = int(argv[argv.index("--tiradas") + 1])
    if "--semilla" in argv:
        semilla = int(argv[argv.index("--semilla") + 1])
    return tiradas, random.Random(semilla), "--exacto" in argv


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--ayuda"):
        salir(__doc__, 0)
    r = cargar(argv[1], TIPOS)
    d, t = r["datos"], r["tipo"]
    tiradas, rng, exacto = opciones(argv)
    if t == "dados-justo":
        f = OPERACION[d["op"]]
        if exacto:
            res = [f(a, b) for a in range(1, 7) for b in range(1, 7)]
            pa = Fraction(sum(gana(d["A"], x) for x in res), 36)
            pb = Fraction(sum(gana(d["B"], x) for x in res), 36)
            print(f"De 36 tiradas posibles, gana Ana en {pa * 36} y Bea en {pb * 36}.")
            print(f"P(gana Ana) = {fr(pa)} y P(gana Bea) = {fr(pb)} en cada tirada.")
            return 0
        n = tiradas or 100
        c = Counter()
        for _ in range(n):
            x = f(rng.randint(1, 6), rng.randint(1, 6))
            c["Ana" if gana(d["A"], x) else "Bea" if gana(d["B"], x) else "nadie (se repite)"] += 1
        print(f"{n} tiradas simuladas: " + ", ".join(f"{k}: {v}" for k, v in sorted(c.items())))
        return 0
    if t == "suma-probable":
        caras = d["dados"]
        if exacto:
            c = Counter(sum(x) for x in itertools.product(*[range(1, k + 1) for k in caras]))
            total = sum(c.values())
            for s in sorted(c):
                print(f"suma {s}: {c[s]} de {total} casos (P = {fr(Fraction(c[s], total))})")
            return 0
        n = tiradas or 1000
        c = Counter(sum(rng.randint(1, k) for k in caras) for _ in range(n))
        print(f"{n} tiradas simuladas:")
        for s in sorted(c):
            print(f"suma {s}: {c[s]} veces")
        return 0
    if t == "dados-no-transitivos":
        dados = {k: d[k] for k in "ABC"}
        for x, y in (("A", "B"), ("B", "C"), ("C", "A")):
            if exacto:
                p = Fraction(sum(a > b for a in dados[x] for b in dados[y]), 36)
                print(f"P({x} gana a {y}) = {fr(p)}")
            else:
                n = tiradas or 1000
                g = sum(rng.choice(dados[x]) > rng.choice(dados[y]) for _ in range(n))
                print(f"{x} contra {y}: {x} gana {g} de {n} partidas simuladas")
        return 0
    bolsa = ["roja"] * d["rojas"] + ["azul"] * d["azules"]
    evento = (lambda a, b: a == b) if d["evento"] == "mismo" else (lambda a, b: "roja" in (a, b))
    texto = "las dos del mismo color" if d["evento"] == "mismo" else "al menos una roja"
    if exacto:
        pares = [(bolsa[i], bolsa[j]) for i in range(len(bolsa)) for j in range(len(bolsa)) if i != j]
        p = Fraction(sum(evento(a, b) for a, b in pares), len(pares))
        print(f"De {len(pares)} extracciones posibles (primera y segunda bola), salen {texto} en {p * len(pares)}: P = {fr(p)}")
        return 0
    n = tiradas or 1000
    g = sum(evento(*rng.sample(bolsa, 2)) for _ in range(n))
    print(f"{n} extracciones simuladas de dos bolas sin devolver: {texto} en {g} ({100 * g / n:.1f} %)".replace(".", ","))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
