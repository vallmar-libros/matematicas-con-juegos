# Materiales de «Matemáticas con juegos»

*100 retos para jugar, dudar y comprobar, con y sin IA* — Leo Vallmar. Colección «Ciencias con juegos».

Materiales del libro, con la fecha de la edición de noviembre de 2026 (versión del 2026-11-09). El libro funciona entero sin ellos.

## Contenido

### Retos, con su código (M-capítulo-número)
- [retos/retos-cap-00.md](retos/retos-cap-00.md) — Capítulo 0. Cómo usar este libro: juega, duda, comprueba (3 retos)
- [retos/retos-cap-01.md](retos/retos-cap-01.md) — Capítulo 1. Detective de números (16 retos)
- [retos/retos-cap-02.md](retos/retos-cap-02.md) — Capítulo 2. Estimar antes de calcular (10 retos)
- [retos/retos-cap-03.md](retos/retos-cap-03.md) — Capítulo 3. Formas, giros y coordenadas (14 retos)
- [retos/retos-cap-04.md](retos/retos-cap-04.md) — Capítulo 4. Ecuaciones disfrazadas (12 retos)
- [retos/retos-cap-05.md](retos/retos-cap-05.md) — Capítulo 5. Azar y estrategia (12 retos)
- [retos/retos-cap-06.md](retos/retos-cap-06.md) — Capítulo 6. Datos, mapas y redes (10 retos)
- [retos/retos-cap-07.md](retos/retos-cap-07.md) — Capítulo 7. Retos finales sin IA (15 retos)
- [retos/retos-cap-08.md](retos/retos-cap-08.md) — Capítulo 8. Ampliación para 4.º (8 retos)

### Soluciones, en carpeta aparte
- [soluciones/soluciones-cap-00.md](soluciones/soluciones-cap-00.md)
- [soluciones/soluciones-cap-01.md](soluciones/soluciones-cap-01.md)
- [soluciones/soluciones-cap-02.md](soluciones/soluciones-cap-02.md)
- [soluciones/soluciones-cap-03.md](soluciones/soluciones-cap-03.md)
- [soluciones/soluciones-cap-04.md](soluciones/soluciones-cap-04.md)
- [soluciones/soluciones-cap-05.md](soluciones/soluciones-cap-05.md)
- [soluciones/soluciones-cap-06.md](soluciones/soluciones-cap-06.md)
- [soluciones/soluciones-cap-07.md](soluciones/soluciones-cap-07.md)
- [soluciones/soluciones-cap-08.md](soluciones/soluciones-cap-08.md)

### Instrucciones de IA
- [instrucciones-ia/instrucciones-ia-2026-11-09.md](instrucciones-ia/instrucciones-ia-2026-11-09.md)

### Programas de comprobación (Python 3.8 o posterior, sin instalar nada)
- [programas/azar.py](programas/azar.py) — dados, bolsas y bolas: simulación y recuento exacto de casos
- [programas/comun.py](programas/comun.py) — funciones comunes (lo usan los demás programas)
- [programas/letras.py](programas/letras.py) — sumas con letras: comprueba tu respuesta o cuenta las soluciones de una suma inventada
- [programas/recuento.py](programas/recuento.py) — recuentos: escribe y cuenta los casos uno a uno
- [programas/rejillas.py](programas/rejillas.py) — rejilla de cifras, rejilla de jaulas y sumas cruzadas: comprueba tu rejilla o cuenta soluciones
- [programas/rival.py](programas/rival.py) — carrera al número y montones de fichas: juega contra el ordenador o comprueba tu estrategia
- [programas/veraces.py](programas/veraces.py) — veraces y mentirosos: tabla de verdad con todos los casos

### Datos
- [datos/retos.json](datos/retos.json): datos de cada reto, sin soluciones; los leen los programas.

## Versión de esta edición
Esta carpeta corresponde a la edición de noviembre de 2026 del libro (materiales del 2026-11-09, corregidos el 2026-11-10 tras una revisión externa). Al publicar el repositorio, esta versión se fijará con una etiqueta (por ejemplo, `edicion-2026-11`): esa etiqueta es la que corresponde al libro impreso.

## Cómo usar los programas, paso a paso (no hace falta saber Python)
1. **Instala Python 3.8 o posterior** desde https://www.python.org/downloads/ (en Windows, al instalar, marca la casilla «Add Python to PATH»). Los programas solo usan lo que trae Python: no hay que instalar nada más.
2. **Comprueba que funciona.** Abre una terminal (en Windows, «Símbolo del sistema»; en macOS y Linux, «Terminal») y escribe `python --version`. Si no responde, prueba `python3 --version`. Debe salir 3.8 o un número mayor. Si te funciona `python3`, escribe `python3` en lugar de `python` en todas las órdenes.
3. **Descarga los materiales**: botón verde **Code** → **Download ZIP**, y descomprímelo.
4. **Abre la terminal en la carpeta correcta**: la que contiene este README.md y las carpetas `programas` y `datos` (no dentro de `programas`). En Windows, abre esa carpeta en el Explorador, escribe `cmd` en la barra de direcciones y pulsa Intro. En macOS, clic derecho sobre la carpeta → Servicios → Nueva terminal en la carpeta. En Linux, clic derecho → Abrir en una terminal.
5. **Escribe la orden que trae cada reto** y pulsa Intro, por ejemplo:

```text
python programas/rejillas.py M-01-01 "1 2 4 3 / 4 3 1 2 / 2 1 3 4 / 3 4 2 1"
```

6. **Lee la respuesta.** El programa dice si tu respuesta es correcta y, si no, qué regla falla.

**Cómo se escriben las respuestas.** Siempre entre comillas dobles, como en el ejemplo. Rejillas: las cifras separadas por espacios y las filas separadas por `/`; una casilla negra, con `-`. Sumas con letras: letra=cifra separadas por comas, como `"C=1, E=4, H=6"`. Carrera al número: los números separados por comas, como `"3, 7, 11, 15"`. Montones de fichas: el montón y las fichas que quitas, separados por un espacio, como `"3 4"`. Los programas no piden decimales; los que escriben probabilidades las dan como fracción (5/36). En el libro y en las soluciones, los decimales llevan coma (121,67), y «≈» indica un valor redondeado.

Cada programa explica su uso con `--ayuda`. Algunos pueden enseñarte la solución: úsalos después de intentarlo.

## Comprobar retos nuevos (instrucción P-04)
Si una IA o tú inventáis una suma con letras, `letras.py` cuenta sus soluciones y dice si no tiene ninguna, si tiene una sola o si tiene más de una:

```text
python programas/letras.py "SOL + SOL = MAR" --contar
```

Esa, por ejemplo, tiene más de una solución, así que no vale como reto. Solo las sumas con una sola solución son retos válidos. Para los demás tipos de reto no hay programa que compruebe retos inventados: resuélvelos y compara con otra persona.

## Antes de usar un chat de IA
Comprueba su edad mínima y sus condiciones vigentes. Con 12 o 13 años, usa la alternativa sin chat de cada reto. No escribas nunca tu nombre, tu centro, tu dirección ni fotos de personas.

## Licencia
Los retos, las soluciones, las instrucciones y los programas de este repositorio se publican con licencia CC BY 4.0 (texto legal completo en [LICENSE](LICENSE); cómo citar en [AVISO.md](AVISO.md); resumen en [LICENSE.md](LICENSE.md)). El texto del libro no se incluye y sigue protegido.
