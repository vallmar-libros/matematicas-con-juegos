# Retos · Capítulo 8. Ampliación para 4.º

Retos M-08-01 a M-08-08. Las soluciones están en [soluciones/soluciones-cap-08.md](../soluciones/soluciones-cap-08.md).

## M-08-01 · El huerto

Nivel 2 · práctica guiada · Sentido D: Ecuaciones de segundo grado (4.º) (RD 217/2022)

Un huerto rectangular mide 5 m más de largo que de ancho y tiene 696 m² de área. ¿Cuánto mide de ancho? Plantea la ecuación de segundo grado. ¿Qué haces con la solución negativa?

**Comprueba:** sustituir en el enunciado; calculadora.

## M-08-02 · Las entradas del cine

Nivel 2 · práctica guiada · Sentido D: Sistemas de ecuaciones (RD 217/2022)

En el cine, la entrada de adulto cuesta 8 € y la infantil 5 €. Entraron 19 personas y se recaudaron 131 €. ¿Cuántos adultos y cuántos niños entraron? Plantea un sistema de dos ecuaciones.

**Duda con IA** (pista graduada, instrucción P-01, en [instrucciones-ia/instrucciones-ia-2026-11-09.md](../instrucciones-ia/instrucciones-ia-2026-11-09.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 12 o 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Pistas impresas del juego, de una en una y en orden; o un adulto que las lee.

<details><summary>Pistas impresas (léelas de una en una)</summary>

1. Llama a al número de adultos y n al de niños.
2. Una ecuación sale de contar personas y otra de contar euros.
3. Si sustituyes tus números, ¿salen las personas y los euros del enunciado?

</details>

**Comprueba:** sustituir en las dos condiciones.

## M-08-03 · Dos bolas sin devolver

Nivel 3 · práctica guiada · Sentido E: Experimentos compuestos y árboles (4.º) (RD 217/2022)

Una bolsa tiene 6 bolas rojas y 6 azules. Sacas dos, una detrás de otra, sin devolver la primera. ¿Qué probabilidad hay de que las dos sean del mismo color? Haz un diagrama de árbol con las probabilidades en cada rama.

**Duda con IA** (alumno que se equivoca, instrucción P-03, en [instrucciones-ia/instrucciones-ia-2026-11-09.md](../instrucciones-ia/instrucciones-ia-2026-11-09.md)).

- Edad: Desde 14 años: Gemini con tu propia cuenta de Google (no una cuenta supervisada por tu familia), o ChatGPT con permiso de tu madre, padre o tutor. Con 12 o 13 años: la alternativa sin chat. Nunca entres con la cuenta de otra persona.
- Sin chat: Revisa la resolución del alumno imaginario que trae el juego: tiene un paso equivocado. Búscalo y corrígelo.

Con chat (P-03): úsalo solo después de escribir tu propia resolución.

**OJO: RESOLUCIÓN CON ERROR A PROPÓSITO.** El alumno imaginario lo resolvió así y se equivocó adrede en un paso; los siguientes pueden arrastrar el error. No la copies: ¿cuál es el primer paso equivocado? ¿Por qué?

1. P(roja y roja) = 6/12 · 6/12 = 1/4.
2. P(azul y azul) = 6/12 · 6/12 = 1/4.
3. P(mismo color) = 1/4 + 1/4 = 1/2.

**Comprueba:** diagrama de árbol; simulación con el programa del repositorio.

```text
python programas/azar.py M-08-03 --tiradas 100
```

## M-08-04 · Códigos sin repetir

Nivel 2 · sin ayuda (sin IA y sin pistas) · Sentido E: Técnicas de recuento (4.º) (RD 217/2022)

¿Cuántos códigos de 3 cifras distintas puedes formar con las cifras del 1 al 6? ¿Cuántos de ellos son pares?

**Comprueba:** escribir los primeros casos; programa del repositorio.

```text
python programas/recuento.py M-08-04
```

## M-08-05 · La altura del árbol

Nivel 3 · sin ayuda (sin IA y sin pistas) · Sentido C: Razones trigonométricas (4.º, Matemáticas B) (RD 217/2022)

Un árbol vertical crece en un terreno horizontal. Para medir su altura te pones a 32 m de su tronco, medidos en horizontal, y ves la copa con un ángulo de 35° sobre la horizontal. Tus ojos están a 1,65 m del suelo. ¿Cuánto mide el árbol? Usa la calculadora en modo grados (DEG).

**Comprueba:** calculadora en modo grados (DEG).

## M-08-06 · Distancia en el plano

Nivel 3 · sin ayuda (sin IA y sin pistas) · Sentido C: Geometría analítica: distancia y punto medio (4.º, Matemáticas B) (RD 217/2022)

Marca A(1, 4) y B(−3, −4). Calcula la distancia de A a B (exacta y con dos decimales) y el punto medio del segmento.

**Comprueba:** calculadora y GeoGebra.

## M-08-07 · Repaso: tres dados

Nivel 3 · sin ayuda (sin IA y sin pistas) · Sentido E: Experimentos simples y regla de Laplace (RD 217/2022)

Tiras tres dados de 6 caras y sumas. ¿Qué suma o sumas salen con más probabilidad? ¿Con qué probabilidad? Apuesta primero, luego cuenta todos los casos posibles con una tabla o un árbol.

**Comprueba:** tiradas reales o simuladas con el programa del repositorio.

```text
python programas/azar.py M-08-07 --tiradas 100
```

## M-08-08 · Repaso: el adivino

Nivel 3 · sin ayuda (sin IA y sin pistas) · Sentido D: Variable y ecuaciones lineales (RD 217/2022)

Truco de adivinación: pide a alguien que piense un número, y luego: multiplícalo por 3, súmale 3, multiplícalo por 3, réstale 36, divide entre 9. Te dice el resultado. ¿Qué tienes que hacer con ese resultado para adivinar su número? Demuéstralo con álgebra.

**Comprueba:** probar con tres números y con la expresión algebraica.
