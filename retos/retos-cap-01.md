# Retos · Capítulo 1. Detective de números

Retos M-01-01 a M-01-16. Las soluciones están en [soluciones/soluciones-cap-01.md](../soluciones/soluciones-cap-01.md).

## M-01-01 · Cuatro cifras, cuatro filas

Nivel 1 · práctica guiada · Sentido D: Pensamiento computacional: razonamiento y descomposición (RD 217/2022)

Completa la rejilla de 4×4 con las cifras del 1 al 4. Cada cifra va una sola vez en cada fila, en cada columna y en cada caja de borde grueso (2×2).

Rejilla (· = casilla vacía):

```text
· · · ·
· 3 1 ·
2 · 3 ·
· · 2 1
```

**Comprueba:** repasar cada fila, columna y caja; programa del repositorio.

```text
python programas/rejillas.py M-01-01 "tu rejilla, fila a fila, separadas por /"
```

## M-01-02 · Jaulas que suman

Nivel 1 · práctica guiada · Sentido A: Cálculo mental y relaciones inversas entre operaciones (RD 217/2022)

Completa la rejilla de 4×4 con las cifras del 1 al 4, sin repetir ninguna en una fila ni en una columna. Cada jaula (zona de borde grueso) lleva un número y una operación (suma): sus cifras, operadas, dan ese número. Una jaula de una sola casilla lleva solo un número: esa es su cifra. Dentro de una jaula sí se pueden repetir cifras si están en filas y columnas distintas.

Jaulas (fila, columna; la casilla de arriba a la izquierda es la 1, 1):

- Jaula 1: (1, 1), (2, 1) → 3 (suma)
- Jaula 2: (3, 2), (4, 2) → 5 (suma)
- Jaula 3: (3, 1), (4, 1) → 7 (suma)
- Jaula 4: (2, 4), (3, 3), (3, 4) → 6 (suma)
- Jaula 5: (1, 3), (2, 2), (2, 3) → 7 (suma)
- Jaula 6: (1, 2) → 3 (cifra dada)
- Jaula 7: (4, 3), (4, 4) → 5 (suma)
- Jaula 8: (1, 4) → 4 (cifra dada)

**Comprueba:** operar cada jaula con la calculadora; programa del repositorio.

```text
python programas/rejillas.py M-01-02 "tu rejilla, fila a fila, separadas por /"
```

## M-01-03 · El cuadrado que siempre suma igual

Nivel 1 · práctica guiada · Sentido A: Patrones y regularidades numéricas (RD 217/2022)

Coloca los números 1, 2, 3, 4, 5, 6, 7, 8 y 9 en el cuadrado de 3×3, cada uno una vez, para que todas las filas, todas las columnas y las dos diagonales sumen lo mismo. Algunos ya están puestos. Primero averigua cuánto debe sumar cada línea.

Rejilla (· = casilla vacía):

```text
· · ·
· 5 ·
4 9 ·
```

**Comprueba:** sumar las ocho líneas con la calculadora.

## M-01-04 · Triángulo de lados iguales

Nivel 1 · práctica guiada · Sentido A: Cálculo mental y relaciones inversas entre operaciones (RD 217/2022)

Coloca los números 1, 2, 3, 4, 5 y 6 en los seis círculos del triángulo (tres en los vértices y tres en medio de los lados), cada uno una vez, para que cada lado sume 10. Los números ya escritos no se mueven.

Círculos (desde arriba, en el sentido de las agujas del reloj):

- vértice de arriba: vacío
- en medio del lado derecho: vacío
- vértice de abajo a la derecha: vacío
- en medio del lado de abajo: 6
- vértice de abajo a la izquierda: 1
- en medio del lado izquierdo: vacío

**Comprueba:** sumar los tres lados.

## M-01-05 · ¿Quién es el número?

Nivel 2 · práctica guiada · Sentido A: Factores, múltiplos y divisores (RD 217/2022)

Estoy pensando un número entre 10 y 99. Al dividirlo entre 4 sobra 2. Termina en 6. Al dividirlo entre 7 sobra 2. ¿Qué número es? Escribe por qué descartas los demás.

**Duda con IA** (pista graduada, instrucción P-01, en [instrucciones-ia/instrucciones-ia-2026-11-09.md](../instrucciones-ia/instrucciones-ia-2026-11-09.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 12 o 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Pistas impresas del juego, de una en una y en orden; o un adulto que las lee.

<details><summary>Pistas impresas (léelas de una en una)</summary>

1. Empieza por la pista que deja menos números posibles.
2. Escribe la lista de números que cumplen esa pista y tacha los que no cumplen las otras pistas.
3. ¿Has comprobado tu número con cada una de las pistas, una por una?

</details>

**Comprueba:** comprobar cada pista con el número y repasar los números del intervalo del enunciado.

## M-01-06 · Jaulas con tres operaciones

Nivel 2 · práctica guiada · Sentido A: Cálculo mental y relaciones inversas entre operaciones (RD 217/2022)

Completa la rejilla de 4×4 con las cifras del 1 al 4, sin repetir ninguna en una fila ni en una columna. Cada jaula (zona de borde grueso) lleva un número y una operación (división, multiplicación y suma): sus cifras, operadas, dan ese número. En la resta y en la división se empieza por la cifra mayor. Una jaula de una sola casilla lleva solo un número: esa es su cifra. Dentro de una jaula sí se pueden repetir cifras si están en filas y columnas distintas.

Jaulas (fila, columna; la casilla de arriba a la izquierda es la 1, 1):

- Jaula 1: (2, 2), (3, 1), (3, 2) → 7 (suma)
- Jaula 2: (2, 3), (3, 3) → 12 (multiplicación)
- Jaula 3: (1, 2), (1, 3), (1, 4) → 7 (suma)
- Jaula 4: (4, 4) → 4 (cifra dada)
- Jaula 5: (2, 4), (3, 4) → 6 (multiplicación)
- Jaula 6: (1, 1), (2, 1) → 3 (división)
- Jaula 7: (4, 1), (4, 2), (4, 3) → 6 (suma)

**Comprueba:** operar cada jaula con la calculadora; programa del repositorio.

```text
python programas/rejillas.py M-01-06 "tu rejilla, fila a fila, separadas por /"
```

## M-01-07 · Sumas que se cruzan

Nivel 2 · práctica guiada · Sentido A: Cálculo mental y relaciones inversas entre operaciones (RD 217/2022)

Escribe una cifra del 1 al 9 en cada casilla blanca. Cada tramo horizontal o vertical de casillas blancas suma el número de su pista, y dentro de un tramo no se repite ninguna cifra. La pista de un tramo horizontal está a su izquierda, por encima de la raya. La de un tramo vertical está encima, por debajo de la raya.

Plantilla (# = casilla negra, . = casilla blanca):

```text
..#
...
#..
```

Tramos (fila, columna de la primera casilla):

- Horizontal de 2 casillas desde (1, 1): suma 6
- Horizontal de 3 casillas desde (2, 1): suma 6
- Horizontal de 2 casillas desde (3, 2): suma 12
- Vertical de 2 casillas desde (1, 1): suma 8
- Vertical de 3 casillas desde (1, 2): suma 12
- Vertical de 2 casillas desde (2, 3): suma 4

**Comprueba:** sumar cada tramo; programa del repositorio.

```text
python programas/rejillas.py M-01-07 "tu rejilla, fila a fila, separadas por /"
```

## M-01-08 · Palabras que suman

Nivel 2 · práctica guiada · Sentido A: Cálculo mental y relaciones inversas entre operaciones (RD 217/2022)

En la suma HILO + HILO = COCHE, cada letra es una cifra distinta y letras iguales son cifras iguales. Ninguna palabra empieza por 0. ¿Qué cifra es cada letra? Pista de método: empieza por la columna de la izquierda y piensa en las que se llevan.

**Duda con IA** (generadora de variantes, instrucción P-04, en [instrucciones-ia/instrucciones-ia-2026-11-09.md](../instrucciones-ia/instrucciones-ia-2026-11-09.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 12 o 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Inventa tú una variante y mira si tiene una sola solución: python programas/letras.py "TU + SUMA = NUEVA" --contar

**Comprueba:** sustituir las cifras y hacer la suma con la calculadora; programa del repositorio para ver que no hay otra.

```text
python programas/letras.py M-01-08 "A=1, B=2, …"
```

## M-01-09 · Tres clubes, tres horas

Nivel 2 · práctica guiada · Sentido D: Pensamiento computacional: razonamiento y descomposición (RD 217/2022)

Ana, Bruno y Carla: cada uno tiene un valor distinto de cada categoría (club y hora de salida). Usa la tabla: pon una X donde no pueda ser y un círculo donde sí. Pistas: (1) Quien va al club de teatro no sale a las 17:00. (2) Carla no sale a las 16:00. (3) Quien sale a las 18:00 no va al club de teatro. (4) Ana no sale a las 17:00. (5) Bruno sale antes que Ana. (6) Quien va al club de ajedrez no sale a las 17:00.

**Comprueba:** comprobar cada pista con la tabla terminada.

## M-01-10 · La isla de las dos tribus

Nivel 3 · práctica guiada · Sentido D: Pensamiento computacional: razonamiento y descomposición (RD 217/2022)

En la isla de las dos tribus, cada persona dice siempre la verdad o miente siempre. Ana dice: «Carla dice siempre la verdad». Bruno dice: «Ana y David son de tipos distintos». Carla dice: «David dice siempre la verdad». David dice: «Ana y Carla son del mismo tipo». ¿Quién dice la verdad y quién miente?

**Duda con IA** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-09.md](../instrucciones-ia/instrucciones-ia-2026-11-09.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 12 o 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la resolución del alumno imaginario que trae el juego: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

**OJO: RESOLUCIÓN CON ERROR A PROPÓSITO.** El alumno imaginario lo resolvió así y se equivocó adrede en un paso; los siguientes pueden arrastrar el error. No la copies: ¿cuál es el primer paso equivocado? ¿Por qué?

1. Pruebo este reparto: Ana dice la verdad, Bruno dice la verdad, Carla dice la verdad, David dice la verdad.
2. Ana dice: «Carla dice siempre la verdad». Con mi reparto la frase es verdadera y Ana dice la verdad: encaja.
3. Bruno dice: «Ana y David son de tipos distintos». Con mi reparto la frase es verdadera y Bruno dice la verdad: encaja.
4. Carla dice: «David dice siempre la verdad». Con mi reparto la frase es verdadera y Carla dice la verdad: encaja.
5. David dice: «Ana y Carla son del mismo tipo». Con mi reparto la frase es verdadera y David dice la verdad: encaja.
6. Todas las frases encajan, así que mi reparto es la solución.

**Comprueba:** tabla de verdad con todos los casos; programa del repositorio.

```text
python programas/veraces.py M-01-10
```

## M-01-11 · Jaulas de cinco

Nivel 3 · práctica guiada · Sentido A: Cálculo mental y relaciones inversas entre operaciones (RD 217/2022)

Completa la rejilla de 5×5 con las cifras del 1 al 5, sin repetir ninguna en una fila ni en una columna. Cada jaula (zona de borde grueso) lleva un número y una operación (división, multiplicación, resta y suma): sus cifras, operadas, dan ese número. En la resta y en la división se empieza por la cifra mayor. Una jaula de una sola casilla lleva solo un número: esa es su cifra. Dentro de una jaula sí se pueden repetir cifras si están en filas y columnas distintas.

Jaulas (fila, columna; la casilla de arriba a la izquierda es la 1, 1):

- Jaula 1: (3, 3), (4, 3), (5, 3) → 11 (suma)
- Jaula 2: (3, 1), (3, 2) → 1 (resta)
- Jaula 3: (4, 1), (5, 1) → 3 (división)
- Jaula 4: (1, 3), (1, 4), (2, 3) → 12 (multiplicación)
- Jaula 5: (3, 4), (4, 4), (5, 4) → 10 (suma)
- Jaula 6: (1, 5), (2, 4), (2, 5) → 6 (suma)
- Jaula 7: (4, 2), (5, 2) → 5 (suma)
- Jaula 8: (3, 5), (4, 5) → 3 (resta)
- Jaula 9: (1, 2), (2, 2) → 3 (resta)
- Jaula 10: (1, 1), (2, 1) → 9 (suma)
- Jaula 11: (5, 5) → 5 (cifra dada)

**Comprueba:** operar cada jaula con la calculadora; programa del repositorio.

```text
python programas/rejillas.py M-01-11 "tu rejilla, fila a fila, separadas por /"
```

## M-01-12 · El camino de los múltiplos de 3

Nivel 1 · sin ayuda (sin IA y sin pistas) · Sentido A: Factores, múltiplos y divisores (RD 217/2022)

Ve de la casilla de arriba a la izquierda a la de abajo a la derecha (5×5 casillas) pisando solo múltiplos de 3. Te mueves en horizontal o en vertical, nunca en diagonal, y no pisas dos veces la misma casilla. Hay un único camino.

Rejilla:

```text
54 42 72 93 82
94 90 38 80 63
96 93 30 86 86
36 98 19 79 38
99 12 12 15 24
```

**Comprueba:** dividir cada número del camino entre el divisor con la calculadora.

## M-01-13 · El candado de tres cifras

Nivel 2 · sin ayuda (sin IA y sin pistas) · Sentido D: Pensamiento computacional: razonamiento y descomposición (RD 217/2022)

El candado tiene un código de 3 cifras distintas. Cada intento dice cuántas cifras están bien colocadas y cuántas son del código pero están en otro sitio. 765: una cifra está bien colocada. 083: una cifra está bien colocada. 648: una cifra es del código pero está mal colocada. 853: una cifra está bien colocada. 251: ninguna cifra es del código. ¿Cuál es el código?

**Comprueba:** comprobar cada intento con el código.

## M-01-14 · Suma de palabras distintas

Nivel 3 · sin ayuda (sin IA y sin pistas) · Sentido A: Cálculo mental y relaciones inversas entre operaciones (RD 217/2022)

En la suma MONTE + ENTE = CANOA, cada letra es una cifra distinta y letras iguales son cifras iguales. Ninguna palabra empieza por 0. ¿Qué cifra es cada letra?

**Comprueba:** sustituir las cifras y hacer la suma con la calculadora; programa del repositorio para ver que no hay otra.

```text
python programas/letras.py M-01-14 "A=1, B=2, …"
```

## M-01-15 · Repaso: estimar productos

Nivel 1 · sin ayuda (sin IA y sin pistas) · Sentido A: Estimaciones con la precisión requerida (RD 217/2022)

Batalla de estimación por parejas. Para cada cuenta, cada jugador escribe una estimación en 10 segundos, sin calcular con lápiz: 58 × 5; 71 × 6; 916 : 5; 639 : 6. Después se calcula. Gana un punto quien quede a menos del 10 % del valor exacto; si los dos, quien esté más cerca. Si empatáis, ambos ganáis un punto.

**Comprueba:** calculadora; anotar el error relativo de la estimación.

## M-01-16 · Repaso: rejilla de cifras

Nivel 1 · sin ayuda (sin IA y sin pistas) · Sentido D: Pensamiento computacional: razonamiento y descomposición (RD 217/2022)

Completa la rejilla de 4×4 con las cifras del 1 al 4. Cada cifra va una sola vez en cada fila, en cada columna y en cada caja de borde grueso (2×2).

Rejilla (· = casilla vacía):

```text
· · · ·
3 · · 2
· 2 · 3
1 · · ·
```

**Comprueba:** repasar cada fila, columna y caja; programa del repositorio.

```text
python programas/rejillas.py M-01-16 "tu rejilla, fila a fila, separadas por /"
```
