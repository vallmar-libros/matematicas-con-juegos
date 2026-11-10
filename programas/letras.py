#!/usr/bin/env python3
"""Sumas con letras: comprueba tu respuesta o cuenta cuántas soluciones tiene una suma (también las que inventes tú o una IA).

Cada letra es una cifra distinta, letras iguales son cifras iguales y ninguna palabra de más de una letra empieza por 0.

Uso:
  python programas/letras.py M-01-08 "C=1, E=4, H=6, I=0, L=8, O=2"
      dice si tu respuesta cumple las reglas.
  python programas/letras.py M-01-08 --contar
      cuenta las soluciones del reto (deben ser exactamente 1). ¡Si hay una, te la enseña!
  python programas/letras.py "SOL + SOL = MAR" --contar
      lo mismo con una suma inventada: así compruebas si una variante tiene una sola solución.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import cargar, salir  # noqa: E402


def partir(texto):
    t = texto.upper().replace(" ", "")
    if "=" not in t:
        salir("Escribe la suma así: \"SOL + SOL = MAR\".")
    izq, res = t.split("=")
    sumandos = [w for w in izq.split("+") if w]
    for w in sumandos + [res]:
        if not w.isalpha():
            salir(f"«{w}» no es una palabra: usa solo letras.")
    return sumandos, res


def contar(sumandos, resultado, tope=2):
    L = len(resultado)
    if any(len(w) > L for w in sumandos) or len(set("".join(sumandos) + resultado)) > 10:
        return []
    iniciales = {w[0] for w in sumandos + [resultado] if len(w) > 1}
    cols = [[w[-1 - i] for w in sumandos if i < len(w)] for i in range(L)]
    asig, usados, sols = {}, set(), []

    def col(i, lleva):
        if len(sols) >= tope:
            return
        if i == L:
            if lleva == 0:
                sols.append(dict(sorted(asig.items())))
            return

        def poner(k, s):
            if k == len(cols[i]):
                tot = s + lleva
                cifra, nueva = tot % 10, tot // 10
                r = resultado[-1 - i]
                if r in asig:
                    if asig[r] == cifra:
                        col(i + 1, nueva)
                elif cifra not in usados and not (cifra == 0 and r in iniciales):
                    asig[r] = cifra
                    usados.add(cifra)
                    col(i + 1, nueva)
                    del asig[r]
                    usados.discard(cifra)
                return
            x = cols[i][k]
            if x in asig:
                poner(k + 1, s + asig[x])
                return
            for cifra in range(10):
                if cifra in usados or (cifra == 0 and x in iniciales):
                    continue
                asig[x] = cifra
                usados.add(cifra)
                poner(k + 1, s + cifra)
                del asig[x]
                usados.discard(cifra)

        poner(0, 0)

    col(0, 0)
    return sols


def valor(w, a):
    return int("".join(str(a[ch]) for ch in w))


def fallos(sumandos, resultado, a):
    letras = set("".join(sumandos) + resultado)
    p = []
    if set(a) != letras:
        falta = sorted(letras - set(a))
        sobra = sorted(set(a) - letras)
        if falta:
            p.append("falta la cifra de " + ", ".join(falta))
        if sobra:
            p.append("estas letras no están en la suma: " + ", ".join(sobra))
        return p
    if len(set(a.values())) != len(a):
        p.append("dos letras distintas tienen la misma cifra")
    for w in sumandos + [resultado]:
        if len(w) > 1 and a[w[0]] == 0:
            p.append(f"{w} empieza por 0")
    if not p and sum(valor(w, a) for w in sumandos) != valor(resultado, a):
        cuenta = " + ".join(str(valor(w, a)) for w in sumandos)
        p.append(f"la cuenta no sale: {cuenta} = {sum(valor(w, a) for w in sumandos)}, no {valor(resultado, a)}")
    return p


def leer_respuesta(txt):
    a = {}
    for parte in txt.replace(";", ",").split(","):
        if not parte.strip():
            continue
        if "=" not in parte:
            salir(f"No entiendo «{parte.strip()}»: escribe letra=cifra, por ejemplo \"C=1, E=4\".")
        k, v = parte.split("=")
        k, v = k.strip().upper(), v.strip()
        if len(k) != 1 or not k.isalpha() or not v.isdigit() or len(v) != 1:
            salir(f"No entiendo «{parte.strip()}»: cada letra lleva una sola cifra.")
        a[k] = int(v)
    return a


def main(argv):
    if len(argv) < 3 or argv[1] in ("-h", "--ayuda"):
        salir(__doc__, 0)
    if argv[1].upper().startswith("M-"):
        d = cargar(argv[1], ("criptoaritmetica",))["datos"]
        sumandos, resultado = d["sumandos"], d["resultado"]
    else:
        sumandos, resultado = partir(argv[1])
    if argv[2] == "--contar":
        sols = contar(sumandos, resultado)
        if not sols:
            print("Esta suma no tiene solución.")
        elif len(sols) == 1:
            s = sols[0]
            print("Esta suma tiene una sola solución: " + ", ".join(f"{k}={v}" for k, v in s.items())
                  + f". La cuenta: {' + '.join(str(valor(w, s)) for w in sumandos)} = {valor(resultado, s)}.")
        else:
            print("Esta suma tiene más de una solución. Dos de ellas:")
            for s in sols:
                print(" -", ", ".join(f"{k}={v}" for k, v in s.items()))
        return 0
    p = fallos(sumandos, resultado, leer_respuesta(argv[2]))
    if p:
        print("Tu respuesta no es correcta:")
        for x in p:
            print(" -", x)
        return 1
    print("Respuesta correcta: la cuenta sale y se cumplen todas las reglas.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
