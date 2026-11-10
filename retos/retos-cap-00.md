# Retos · Capítulo 0. Cómo usar este libro: juega, duda, comprueba

Retos M-00-01 a M-00-03. Las soluciones están en [soluciones/soluciones-cap-00.md](../soluciones/soluciones-cap-00.md).

## M-00-01 · Ejemplo resuelto: la rejilla de cifras

Nivel 1 · ejemplo resuelto · Sentido D: Pensamiento computacional: razonamiento y descomposición (RD 217/2022)

Completa la rejilla de 4×4 con las cifras del 1 al 4. Cada cifra va una sola vez en cada fila, en cada columna y en cada caja de borde grueso (2×2).

Rejilla (· = casilla vacía):

```text
2 · 1 ·
· · · 3
· 4 · ·
· · 4 1
```

**Comprueba:** repasar cada fila, columna y caja; programa del repositorio.

```text
python programas/rejillas.py M-00-01 "tu rejilla, fila a fila, separadas por /"
```

## M-00-02 · ¿Se ha equivocado la máquina?

Nivel 1 · práctica guiada · Sentido A: Estimaciones con la precisión requerida (RD 217/2022)

Batalla de estimación por parejas. Para cada cuenta, cada jugador escribe una estimación en 10 segundos, sin calcular con lápiz: 29 × 7; 19 × 6; 44 × 6; 365 : 3. Después se calcula. Gana un punto quien quede a menos del 10 % del valor exacto; si los dos, quien esté más cerca. Si empatáis, ambos ganáis un punto.

**Duda con IA** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-09.md](../instrucciones-ia/instrucciones-ia-2026-11-09.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 12 o 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la resolución del alumno imaginario que trae el juego: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

**OJO: RESOLUCIÓN CON ERROR A PROPÓSITO.** El alumno imaginario lo resolvió así y se equivocó adrede en un paso; los siguientes pueden arrastrar el error. No la copies: ¿cuál es el primer paso equivocado? ¿Por qué?

1. 29 × 7 = 20 × 7 + 9 × 7 = 140 + 63 = 103
2. 19 × 6 = 114
3. 44 × 6 = 264
4. 365 : 3 ≈ 121,67

**Comprueba:** calculadora; anotar el error relativo de la estimación.

## M-00-03 · Primer reto sin IA: el número escondido

Nivel 1 · sin ayuda (sin IA y sin pistas) · Sentido A: Factores, múltiplos y divisores (RD 217/2022)

Estoy pensando un número entre 10 y 60. Al dividirlo entre 5 sobra 2. Sus cifras suman 9. ¿Qué número es? Escribe por qué descartas los demás.

**Comprueba:** comprobar cada pista con el número y repasar los números del intervalo del enunciado.
