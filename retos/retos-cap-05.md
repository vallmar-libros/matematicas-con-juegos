# Retos · Capítulo 5. Azar y estrategia

Retos M-05-01 a M-05-12. Las soluciones están en [soluciones/soluciones-cap-05.md](../soluciones/soluciones-cap-05.md).

## M-05-01 · ¿Es justo con la suma?

Nivel 1 · práctica guiada · Sentido E: Experimentos simples y regla de Laplace (RD 217/2022)

Ana y Bea tiran dos dados normales y miran la suma de los dos. Ana gana si sale 6 o menos; Bea gana si sale más de 7; si no gana ninguna, se vuelve a tirar. Antes de calcular, juega 20 tiradas y apunta. ¿Es un juego justo? Haz la tabla de las 36 tiradas posibles.

**Comprueba:** tabla de 36 casos y 100 tiradas reales o simuladas con el programa del repositorio.

```text
python programas/azar.py M-05-01 --tiradas 100
```

## M-05-02 · Carrera contra la IA

Nivel 1 · práctica guiada · Sentido D: Pensamiento computacional: estrategias y algoritmos (RD 217/2022)

Carrera al 21. Dos jugadores dicen números por turnos. El primero dice un número del 1 al 4; cada uno, en su turno, suma al número anterior entre 1 y 4. Gana quien diga 21. ¿Te conviene empezar? ¿Qué números tienes que decir para ganar seguro?

**Duda con IA** (rival, instrucción P-02, en [instrucciones-ia/instrucciones-ia-2026-11-09.md](../instrucciones-ia/instrucciones-ia-2026-11-09.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 12 o 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Juega contra un adulto o un amigo; también puede jugar el programa del repositorio.

**Comprueba:** jugar contra alguien siguiendo la estrategia; programa del repositorio.

```text
python programas/rival.py M-05-02
```

## M-05-03 · La suma favorita de dos dados

Nivel 2 · práctica guiada · Sentido E: Experimentos simples y regla de Laplace (RD 217/2022)

Tiras dos dados de 6 caras y sumas. ¿Qué suma o sumas salen con más probabilidad? ¿Con qué probabilidad? Apuesta primero, luego cuenta todos los casos posibles con una tabla o un árbol.

**Comprueba:** tabla de casos y simulación con el programa del repositorio.

```text
python programas/azar.py M-05-03 --tiradas 100
```

## M-05-04 · Montones contra la IA

Nivel 2 · práctica guiada · Sentido D: Pensamiento computacional: estrategias y algoritmos (RD 217/2022)

Hay tres montones con 2, 3 y 5 fichas. Por turnos, cada jugador quita todas las que quiera (al menos una) de un solo montón. Gana quien se lleve la última ficha. ¿Te conviene empezar? Si sí, ¿qué primeras jugadas te hacen ganar? Puede haber más de una.

**Duda con IA** (rival, instrucción P-02, en [instrucciones-ia/instrucciones-ia-2026-11-09.md](../instrucciones-ia/instrucciones-ia-2026-11-09.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 12 o 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Juega contra un adulto o un amigo; también puede jugar el programa del repositorio.

**Comprueba:** jugar contra alguien siguiendo la estrategia; programa del repositorio.

```text
python programas/rival.py M-05-04
```

## M-05-05 · ¿De qué bolsa saco?

Nivel 2 · práctica guiada · Sentido E: Experimentos simples y regla de Laplace (RD 217/2022)

Bolsa 1: 2 bolas rojas y 4 azules. Bolsa 2: 7 rojas y 15 azules. Sacas una bola sin mirar y ganas si es roja. ¿De qué bolsa te conviene sacar? Ojo: no basta con mirar qué bolsa tiene más rojas.

**Duda con IA** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-09.md](../instrucciones-ia/instrucciones-ia-2026-11-09.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 12 o 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la resolución del alumno imaginario que trae el juego: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

**OJO: RESOLUCIÓN CON ERROR A PROPÓSITO.** El alumno imaginario lo resolvió así y se equivocó adrede en un paso; los siguientes pueden arrastrar el error. No la copies: ¿cuál es el primer paso equivocado? ¿Por qué?

1. La bolsa 1 tiene 2 rojas y la bolsa 2 tiene 7 rojas.
2. La bolsa 2 tiene más rojas, así que conviene sacar de la bolsa 2.

**Comprueba:** comparar fracciones con la calculadora.

## M-05-06 · Dados que se ganan en círculo

Nivel 3 · práctica guiada · Sentido E: Experimentos simples y regla de Laplace (RD 217/2022)

Tres dados especiales: A tiene 1, 3, 12, 13, 14, 16; B tiene 6, 7, 8, 9, 11, 15; C tiene 2, 4, 5, 10, 17, 18. Tu rival elige un dado, tú eliges otro, y gana quien saque más. Calcula P(A gana a B), P(B gana a C) y P(C gana a A) con tablas de 6 × 6. ¿Hay un dado que sea el mejor?

**Comprueba:** tablas de 6 × 6; simulación con el programa del repositorio.

```text
python programas/azar.py M-05-06 --tiradas 100
```

## M-05-07 · ¿Es justo con el producto?

Nivel 1 · práctica guiada · Sentido E: Experimentos simples y regla de Laplace (RD 217/2022)

Ana y Bea tiran dos dados normales y miran el producto de los dos. Ana gana si sale 9 o menos; Bea gana si sale más de 9. Antes de calcular, juega 20 tiradas y apunta. ¿Es un juego justo? Haz la tabla de las 36 tiradas posibles.

**Comprueba:** tabla de 36 casos y 100 tiradas reales o simuladas con el programa del repositorio.

```text
python programas/azar.py M-05-07 --tiradas 100
```

## M-05-08 · ¿Es justo con la diferencia?

Nivel 2 · sin ayuda (sin IA y sin pistas) · Sentido E: Experimentos simples y regla de Laplace (RD 217/2022)

Ana y Bea tiran dos dados normales y miran la diferencia (el mayor menos el menor) de los dos. Ana gana si sale 1 o menos; Bea gana si sale más de 1. Antes de calcular, juega 20 tiradas y apunta. ¿Es un juego justo? Justifica la respuesta.

**Comprueba:** 100 tiradas reales o simuladas con el programa del repositorio.

```text
python programas/azar.py M-05-08 --tiradas 100
```

## M-05-09 · Carrera al número

Nivel 1 · sin ayuda (sin IA y sin pistas) · Sentido D: Pensamiento computacional: estrategias y algoritmos (RD 217/2022)

Carrera al 15. Dos jugadores dicen números por turnos. El primero dice un número del 1 al 3; cada uno, en su turno, suma al número anterior entre 1 y 3. Gana quien diga 15. ¿Te conviene empezar? ¿Qué números tienes que decir para ganar seguro?

**Comprueba:** jugar contra alguien siguiendo la estrategia; programa del repositorio.

```text
python programas/rival.py M-05-09
```

## M-05-10 · Cuatro montones

Nivel 3 · sin ayuda (sin IA y sin pistas) · Sentido D: Pensamiento computacional: estrategias y algoritmos (RD 217/2022)

Hay cuatro montones con 2, 3, 5 y 6 fichas. Por turnos, cada jugador quita todas las que quiera (al menos una) de un solo montón. Gana quien se lleve la última ficha. ¿Te conviene empezar? Si sí, ¿qué primeras jugadas te hacen ganar? Puede haber más de una.

**Comprueba:** jugar contra alguien siguiendo la estrategia; programa del repositorio.

```text
python programas/rival.py M-05-10
```

## M-05-11 · Repaso: balanzas

Nivel 1 · sin ayuda (sin IA y sin pistas) · Sentido D: Variable y ecuaciones lineales (RD 217/2022)

Todas las figuras iguales pesan lo mismo, y cada peso es un número entero de gramos entre 1 y 20 (círculos y cuadrados). Balanza 1: 1 círculo y 1 cuadrado pesan 15 g. Balanza 2: 2 círculos y 1 cuadrado pesan 22 g. ¿Cuánto pesa cada figura?

**Comprueba:** sustituir los pesos en cada balanza.

## M-05-12 · Repaso: ¿cuál es rectángulo?

Nivel 2 · sin ayuda (sin IA y sin pistas) · Sentido C: Relación pitagórica (RD 217/2022)

Solo uno de estos triángulos es rectángulo. ¿Cuál? Lados: A: 11, 23 y 27 cm; B: 10, 24 y 26 cm; C: 11, 25 y 27 cm; D: 9, 25 y 26 cm.

**Comprueba:** dibujar a escala con regla y escuadra, y medir.
