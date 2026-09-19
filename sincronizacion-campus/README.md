# Sincronizacion con el campus (Moodle FRSR-UTN)

Herramienta para mantener esta carpeta al dia con el campus de **Gestion Gerencial 2026**
(curso `1556` en https://campus.frsr.utn.edu.ar/moodle).

Es la misma herramienta que usan las carpetas de Inteligencia Artificial e Ingenieria y
Calidad de Software, con tres diferencias: apunta al curso 1556, las secciones del campus
(`Clase 1`, `Proyecto Final`, ...) se mapean a carpetas por `organizacion.secciones` en vez
de asumir "Unidad N", y ademas vuelca los foros a texto.

## Como se usa

```bash
cd "sincronizacion-campus"

python3 sync.py                # sincroniza y regenera ESTADO.md
python3 sync.py --descargar    # ademas baja a ../Material Campus/ lo que falte
python3 sync.py --login        # renueva el token si dejo de funcionar
python3 sync.py --curso 1340   # sincroniza otra materia (ids en config.json)
```

Cada corrida compara contra la anterior y avisa por consola lo que aparecio nuevo o lo que
cambio de fecha, ademas de listar los TP sin entregar. Volver a correr `--descargar` no
duplica nada: salta los archivos que ya estan.

## Que hay en la carpeta

| Archivo | Que es |
|---|---|
| `sync.py` | el sincronizador (solo libreria estandar de Python) |
| `texto.py` | pasa los PDF y apuntes a Markdown en `00-TEXTO/` |
| `config.json` | url del campus, id del curso, organizacion de carpetas |
| `ESTADO.md` | **reporte generado**: TPs, vencimientos, notas, avisos, contenido |
| `data/snapshot-1556.json` | volcado crudo de la ultima sincronizacion (detecta novedades) |
| `.secrets/wstoken` | token de web service, permisos 600 |

`ESTADO.md`, `../Material Campus/00-INDICE.md` y `00-TEXTO/00-INDICE.md` se reescriben
enteros en cada corrida: no editarlos a mano.

## Como quedan los archivos bajados

En `../Material Campus/`, aplanado a un solo nivel (mas simple que el campus):

- `Catedra/` - lo administrativo (presentacion introductoria) y el enlace a la clase virtual.
- `Clase N/` - las diapositivas de esa clase.
- `Proyecto Final/` - la consigna del TP final y los ejemplos de la catedra.
- `Foros/` - un `.md` por foro con todos los hilos y respuestas.
- `00-TEXTO/` - un `.md` por cada PDF o apunte, para leer o buscar rapido.

Donde va cada cosa sale de `organizacion` en `config.json`:

- `secciones` mapea una seccion del campus a su carpeta local. Sin regla explicita,
  `Clase 3` y `Unidad N 3` conservan el numero, `General` y las secciones vacias de Moodle
  (`Tema 7`) caen en `Catedra`, y cualquier otra seccion usa su propio nombre.
- `archivos` renombra y reubica archivos puntuales por su nombre en el campus
  (`slides_clase_1.pdf` -> `Clase 1/Diapositivas Clase 1.pdf`).

Si se cambia donde va o como se llama un archivo hay que volver a correr `--descargar`; el
archivo con el nombre viejo queda: se borra a mano.

### Texto

`00-TEXTO/` tiene un `.md` por cada PDF y por cada apunte que el campus publica ya en
`.md`/`.txt`, con nombre plano y un encabezado que dice de que archivo salio. Es la forma
comoda de buscar:

```bash
grep -ril "modelo de madurez" "Material Campus/00-TEXTO"
```

Un `.md` se regenera solo si su original es mas nuevo. Los PDF de mas de 20 MB no se
convierten; el limite se cambia con `limite_texto_mb` en `config.json`.

Para el texto hace falta `pdftotext` (`brew install poppler`). Si no esta, el sync avisa y
sigue sin generar `00-TEXTO/`.

Los foros no pasan por `00-TEXTO/`: ya se escriben como Markdown en `Foros/`.

## Autenticacion

Usa el web service `moodle_mobile_app` de Moodle. El token se obtiene una vez con `--login`
y queda en `.secrets/wstoken` (es el mismo token de la cuenta del campus que usan las otras
materias). **La contrasena no se guarda en ningun lado.** Tambien se puede pasar el token
por la variable de entorno `MOODLE_WSTOKEN`.

Si el token se invalida (cambio de clave, revocacion desde el campus), `sync.py` avisa y hay
que correr `python3 sync.py --login`.

> El token da acceso completo a la cuenta del campus. No subir `.secrets/` a ningun
> repositorio ni compartir la carpeta con ese archivo adentro.

## Limitaciones

- Es **solo lectura**: baja informacion, no sube entregas.
- La asistencia (modulo `attendance`) solo figura como nota: el detalle queda online.
- En este curso no hay tareas (`assign`) cargadas todavia: la tabla de TPs de `ESTADO.md`
  aparece vacia hasta que la catedra publique la entrega del proyecto final.
