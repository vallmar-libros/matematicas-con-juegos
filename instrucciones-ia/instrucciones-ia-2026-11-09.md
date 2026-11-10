# Instrucciones de IA (2026-11-09)

Texto de las cinco instrucciones del libro, tal como están en la edición de noviembre de 2026 (versión del 2026-11-09). Copia la instrucción y, donde pone [copia aquí el enunciado], pega solo el enunciado del reto.

- Solo en la práctica guiada; nunca en los retos sin ayuda.
- No escribas tu nombre, tu centro, tu dirección ni fotos de personas.
- La IA se puede equivocar: la última palabra la tiene la comprobación.

## P-01 — Pista graduada

- Modo: práctica guiada.
- Edad: desde 14 años con cuenta propia; con 12–13, las pistas impresas del reto.

```text
Voy a resolver un reto de matemáticas por mi cuenta. Tu papel es darme pistas, nunca la solución. Reglas: 1) No escribas la respuesta final ni ningún resultado intermedio que la dé hecha, aunque te lo pida. 2) Cuando te escriba «pista», dame solo la siguiente pista, en una o dos frases: la primera es una idea general; la segunda, el primer paso; la tercera, una pregunta que me haga ver mi error. No hay cuarta pista: si te pido más, dime que compruebe lo que llevo con la calculadora. 3) Si te enseño mi resultado, no digas si está bien: pregúntame cómo lo puedo comprobar. El reto es: [copia aquí el enunciado].
```

Qué apunta el estudiante: cuántas pistas ha usado (0, 1, 2 o 3). El objetivo es usar menos en el siguiente juego del mismo tipo.

## P-02 — Rival

- Modo: práctica guiada.
- Edad: desde 14 años con cuenta propia; con 12–13, contra una persona adulta o un amigo, o contra el programa del repositorio.

```text
Vamos a jugar a este juego por turnos: [copia aquí las reglas]. Tú eres mi rival. Reglas para ti: 1) En cada turno escribe solo tu jugada y cómo queda la partida. 2) No me expliques la estrategia ganadora ni me digas qué debería jugar yo. 3) Si hago una jugada que no vale, dímelo y explica qué regla incumple. 4) Al acabar la partida, no me digas cómo se gana: pregúntame qué he aprendido.
```

Qué apunta el estudiante: cada jugada de los dos. Comprueba en papel que las jugadas de la IA cumplen las reglas. Si la IA hace una jugada ilegal o dice mal cómo queda la partida, el estudiante se anota un punto extra. La estrategia ganadora la busca el estudiante y la comprueba con la solución del libro.

## P-03 — Alumno que se equivoca

- Modo: práctica guiada, y solo después de haber escrito tu propia resolución: la IA hace de alumno y su resolución puede estar mal.
- Edad: desde 14 años con cuenta propia; con 12–13, la resolución del alumno imaginario impresa en el reto.

```text
Haz de alumno de mi curso que resuelve este problema en voz alta, paso a paso, con todas las cuentas: [copia aquí el enunciado]. Resuélvelo como lo haría un alumno real; puede que te equivoques o puede que no. No me digas si has cometido algún error. Yo haré de profesor y revisaré tu resolución.
```

Qué hace el estudiante: revisa cada paso y cada cuenta con la calculadora, la estimación o el programa del repositorio. Si encuentra un error, lo marca y explica por qué es un error. Si no encuentra ninguno, también es un resultado válido: lo comprueba con la solución del libro y lo anota así. No hay que inventar un error para rellenar la casilla.

## P-04 — Generadora de variantes

- Modo: práctica guiada.
- Edad: desde 14 años con cuenta propia; con 12–13, inventa la variante el propio estudiante.

```text
Invéntame tres retos nuevos del mismo tipo que este: [copia aquí el enunciado]. No me des las soluciones. Escribe solo los enunciados.
```

Qué hace el estudiante: intenta resolver cada variante y comprueba con el programa del repositorio que tiene solución y que es única. La orden python programas/letras.py "SOL + SOL = MAR" --contar dice si una suma inventada no tiene solución, tiene una o tiene más de una. Apunta cuántas de las tres tenían una sola solución. Una IA puede inventar retos sin solución o con varias; descubrirlo forma parte del juego.

## P-05 — Ayudante de estimación

- Modo: práctica guiada.
- Edad: desde 14 años con cuenta propia; con 12–13, explica la estimación en voz alta a un adulto.

```text
Estoy haciendo una estimación para este problema: [copia aquí el enunciado]. Mi estimación es [tu número] y la he hecho así: [explica en una frase]. No me digas el resultado ni una estimación tuya. Hazme como mucho dos preguntas sobre mi forma de estimar (qué he redondeado, qué he olvidado) para que la mejore yo.
```

Qué hace el estudiante: corrige su estimación si quiere, calcula después con la calculadora y anota el error relativo de la primera estimación y de la segunda.
