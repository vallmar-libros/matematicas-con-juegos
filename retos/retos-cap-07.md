# Retos · Capítulo 7. Retos finales sin IA

Retos M-07-01 a M-07-15. Las soluciones están en [soluciones/soluciones-cap-07.md](../soluciones/soluciones-cap-07.md).

## M-07-01 · Final 1: rejilla de cifras

Nivel 1 · sin ayuda (sin IA y sin pistas) · Sentido D: Pensamiento computacional: razonamiento y descomposición (RD 217/2022)

Completa la rejilla de 4×4 con las cifras del 1 al 4. Cada cifra va una sola vez en cada fila, en cada columna y en cada caja de borde grueso (2×2).

Rejilla (· = casilla vacía):

```text
· 3 · 1
· · 4 ·
· 4 · ·
1 · · ·
```

**Comprueba:** repasar cada fila, columna y caja; programa del repositorio.

```text
python programas/rejillas.py M-07-01 "tu rejilla, fila a fila, separadas por /"
```

## M-07-02 · Final 2: número misterioso

Nivel 1 · sin ayuda (sin IA y sin pistas) · Sentido A: Factores, múltiplos y divisores (RD 217/2022)

Estoy pensando un número entre 10 y 99. Al dividirlo entre 7 sobra 3. Sus cifras suman 12. ¿Qué número es? Escribe por qué descartas los demás.

**Comprueba:** comprobar cada pista con el número y repasar los números del intervalo del enunciado.

## M-07-03 · Final 3: media vuelta

Nivel 1 · sin ayuda (sin IA y sin pistas) · Sentido C: Giros, traslaciones y simetrías (RD 217/2022)

Dibuja la figura de vértices A(3, 5), B(4, 4), C(2, 4). Aplícale un giro de 180° con centro en el origen y escribe las coordenadas de la imagen de cada vértice.

**Comprueba:** GeoGebra (simetría, giro o traslación) o papel de calco.

## M-07-04 · Final 4: balanzas

Nivel 1 · sin ayuda (sin IA y sin pistas) · Sentido D: Variable y ecuaciones lineales (RD 217/2022)

Todas las figuras iguales pesan lo mismo, y cada peso es un número entero de gramos entre 1 y 20 (círculos y cuadrados). Balanza 1: 2 círculos y 3 cuadrados pesan 48 g. Balanza 2: 3 círculos y 2 cuadrados pesan 47 g. ¿Cuánto pesa cada figura?

**Comprueba:** sustituir los pesos en cada balanza.

## M-07-05 · Final 5: ¿es justo?

Nivel 1 · sin ayuda (sin IA y sin pistas) · Sentido E: Experimentos simples y regla de Laplace (RD 217/2022)

Ana y Bea tiran dos dados normales y miran la suma de los dos. Ana gana si sale par; Bea gana si sale impar. Antes de calcular, juega 20 tiradas y apunta. ¿Es un juego justo? Justifica la respuesta.

**Comprueba:** 100 tiradas reales o simuladas con el programa del repositorio.

```text
python programas/azar.py M-07-05 --tiradas 100
```

## M-07-06 · Final 6: sumas cruzadas

Nivel 2 · sin ayuda (sin IA y sin pistas) · Sentido A: Cálculo mental y relaciones inversas entre operaciones (RD 217/2022)

Escribe una cifra del 1 al 9 en cada casilla blanca. Cada tramo horizontal o vertical de casillas blancas suma el número de su pista, y dentro de un tramo no se repite ninguna cifra. La pista de un tramo horizontal está a su izquierda, por encima de la raya. La de un tramo vertical está encima, por debajo de la raya.

Plantilla (# = casilla negra, . = casilla blanca):

```text
..##
....
....
##..
```

Tramos (fila, columna de la primera casilla):

- Horizontal de 2 casillas desde (1, 1): suma 13
- Horizontal de 4 casillas desde (2, 1): suma 11
- Horizontal de 4 casillas desde (3, 1): suma 14
- Horizontal de 2 casillas desde (4, 3): suma 14
- Vertical de 3 casillas desde (1, 1): suma 9
- Vertical de 3 casillas desde (1, 2): suma 21
- Vertical de 3 casillas desde (2, 3): suma 14
- Vertical de 3 casillas desde (2, 4): suma 8

**Comprueba:** sumar cada tramo; programa del repositorio.

```text
python programas/rejillas.py M-07-06 "tu rejilla, fila a fila, separadas por /"
```

## M-07-07 · Final 7: palabras que suman

Nivel 2 · sin ayuda (sin IA y sin pistas) · Sentido A: Cálculo mental y relaciones inversas entre operaciones (RD 217/2022)

En la suma COSA + COSA = FOCA, cada letra es una cifra distinta y letras iguales son cifras iguales. Ninguna palabra empieza por 0. ¿Qué cifra es cada letra?

**Comprueba:** sustituir las cifras y hacer la suma con la calculadora; programa del repositorio para ver que no hay otra.

```text
python programas/letras.py M-07-07 "A=1, B=2, …"
```

## M-07-08 · Final 8: pasos hasta casa

Nivel 2 · sin ayuda (sin IA y sin pistas) · Sentido A, B: Estimación de cantidades y orden de magnitud (RD 217/2022)

Primero estima de cabeza el orden de magnitud: la potencia de 10 más cercana (¿10², 10³, 10⁶…?). Luego calcula. Un paso tuyo mide 75 cm. ¿Cuántos pasos das para recorrer 6 km? Los datos del juego son supuestos, no medidos.

**Comprueba:** calculadora; comparar el orden de magnitud con la estimación.

## M-07-09 · Final 9: las mochilas

Nivel 2 · sin ayuda (sin IA y sin pistas) · Sentido D: Pensamiento computacional: razonamiento y descomposición (RD 217/2022)

Dani, Eva, Fran y Gala: cada uno tiene un valor distinto de cada categoría (color de mochila y número favorito). Usa la tabla: pon una X donde no pueda ser y un círculo donde sí. Pistas: (1) Dani prefiere un número menor que Fran. (2) Quien lleva la mochila verde prefiere el 12. (3) Fran no lleva la mochila verde. (4) Quien prefiere el 20 no lleva la mochila roja. (5) Eva no lleva la mochila negra. (6) Fran no lleva la mochila negra. (7) Quien prefiere el 3 lleva la mochila azul.

**Comprueba:** comprobar cada pista con la tabla terminada.

## M-07-10 · Final 10: hexágonos

Nivel 2 · sin ayuda (sin IA y sin pistas) · Sentido D: Patrones y regla de formación (RD 217/2022)

Con palillos se construye una fila de hexágonos pegados por un lado. La figura 1 usa 6 palillos, la 2 usa 11 y la 3 usa 16. ¿Cuántos palillos usa la figura 15? ¿Qué figura usa exactamente 356 palillos? Escribe la regla para la figura n.

**Comprueba:** dibujar la figura 4 y contar; sustituir en la regla.

## M-07-11 · Final 11: múltiplos de 7

Nivel 2 · sin ayuda (sin IA y sin pistas) · Sentido A: Factores, múltiplos y divisores (RD 217/2022)

Ve de la casilla de arriba a la izquierda a la de abajo a la derecha (6×6 casillas) pisando solo múltiplos de 7. Te mueves en horizontal o en vertical, nunca en diagonal, y no pisas dos veces la misma casilla. Hay un único camino.

Rejilla:

```text
49 32 63 63 63 77
84 70 28 65 44 70
91 89 91 34 14 21
96 78 40 57 91 33
31 86 65 26 91 70
67 63 28 96 25 14
```

**Comprueba:** dividir cada número del camino entre el divisor con la calculadora.

## M-07-12 · Final 12: jaulas de seis

Nivel 3 · sin ayuda (sin IA y sin pistas) · Sentido A: Cálculo mental y relaciones inversas entre operaciones (RD 217/2022)

Completa la rejilla de 6×6 con las cifras del 1 al 6, sin repetir ninguna en una fila ni en una columna. Cada jaula (zona de borde grueso) lleva un número y una operación (multiplicación, resta y suma): sus cifras, operadas, dan ese número. En la resta y en la división se empieza por la cifra mayor. Una jaula de una sola casilla lleva solo un número: esa es su cifra. Dentro de una jaula sí se pueden repetir cifras si están en filas y columnas distintas.

Jaulas (fila, columna; la casilla de arriba a la izquierda es la 1, 1):

- Jaula 1: (6, 3), (6, 4) → 4 (resta)
- Jaula 2: (3, 5), (3, 6), (4, 6) → 8 (suma)
- Jaula 3: (3, 4), (4, 4) → 30 (multiplicación)
- Jaula 4: (1, 4), (2, 4) → 2 (resta)
- Jaula 5: (1, 1), (2, 1) → 4 (resta)
- Jaula 6: (4, 5), (5, 4), (5, 5) → 8 (suma)
- Jaula 7: (1, 5), (1, 6) → 2 (resta)
- Jaula 8: (6, 1), (6, 2) → 6 (multiplicación)
- Jaula 9: (2, 5), (2, 6) → 8 (suma)
- Jaula 10: (5, 1) → 4 (cifra dada)
- Jaula 11: (3, 3), (4, 3), (5, 3) → 11 (suma)
- Jaula 12: (1, 3), (2, 3) → 5 (suma)
- Jaula 13: (1, 2), (2, 2) → 6 (multiplicación)
- Jaula 14: (3, 1), (3, 2) → 18 (multiplicación)
- Jaula 15: (4, 1), (4, 2), (5, 2) → 11 (suma)
- Jaula 16: (5, 6), (6, 6) → 3 (resta)
- Jaula 17: (6, 5) → 6 (cifra dada)

**Comprueba:** operar cada jaula con la calculadora; programa del repositorio.

```text
python programas/rejillas.py M-07-12 "tu rejilla, fila a fila, separadas por /"
```

## M-07-13 · Final 13: cuadrado mágico de 4×4

Nivel 3 · sin ayuda (sin IA y sin pistas) · Sentido A: Patrones y regularidades numéricas (RD 217/2022)

Coloca los números 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 y 16 en el cuadrado de 4×4, cada uno una vez, para que todas las filas, todas las columnas y las dos diagonales sumen lo mismo. Algunos ya están puestos.

Rejilla (· = casilla vacía):

```text
· 5 · 4
· · 6 15
· 11 7 ·
· 8 12 ·
```

**Comprueba:** sumar las ocho líneas con la calculadora.

## M-07-14 · Final 14: la isla otra vez

Nivel 3 · sin ayuda (sin IA y sin pistas) · Sentido D: Pensamiento computacional: razonamiento y descomposición (RD 217/2022)

En la isla de las dos tribus, cada persona dice siempre la verdad o miente siempre. Ana dice: «David y yo somos de tipos distintos». Bruno dice: «Carla dice siempre la verdad». Carla dice: «Ana miente siempre». David dice: «Exactamente 3 de nosotros mienten siempre». ¿Quién dice la verdad y quién miente?

**Comprueba:** tabla de verdad con todos los casos; programa del repositorio.

```text
python programas/veraces.py M-07-14
```

## M-07-15 · Final 15: sumas cruzadas grandes

Nivel 3 · sin ayuda (sin IA y sin pistas) · Sentido A: Cálculo mental y relaciones inversas entre operaciones (RD 217/2022)

Escribe una cifra del 1 al 9 en cada casilla blanca. Cada tramo horizontal o vertical de casillas blancas suma el número de su pista, y dentro de un tramo no se repite ninguna cifra. La pista de un tramo horizontal está a su izquierda, por encima de la raya. La de un tramo vertical está encima, por debajo de la raya.

Plantilla (# = casilla negra, . = casilla blanca):

```text
..#..
.....
#...#
.....
..#..
```

Tramos (fila, columna de la primera casilla):

- Horizontal de 2 casillas desde (1, 1): suma 17
- Horizontal de 2 casillas desde (1, 4): suma 10
- Horizontal de 5 casillas desde (2, 1): suma 28
- Horizontal de 3 casillas desde (3, 2): suma 19
- Horizontal de 5 casillas desde (4, 1): suma 34
- Horizontal de 2 casillas desde (5, 1): suma 15
- Horizontal de 2 casillas desde (5, 4): suma 5
- Vertical de 2 casillas desde (1, 1): suma 9
- Vertical de 2 casillas desde (4, 1): suma 17
- Vertical de 5 casillas desde (1, 2): suma 35
- Vertical de 3 casillas desde (2, 3): suma 13
- Vertical de 5 casillas desde (1, 4): suma 24
- Vertical de 2 casillas desde (1, 5): suma 17
- Vertical de 2 casillas desde (4, 5): suma 13

**Comprueba:** sumar cada tramo; programa del repositorio.

```text
python programas/rejillas.py M-07-15 "tu rejilla, fila a fila, separadas por /"
```
