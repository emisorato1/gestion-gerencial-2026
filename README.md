# Gestión Gerencial 2026 — UTN FRSR

Material de la cátedra de **Gestión Gerencial** (5.º año, Ingeniería en Sistemas de
Información, UTN Facultad Regional San Rafael), ordenado para leerlo y buscarlo más rápido
que en el campus.

## Qué hay acá

```
Material Campus/
├── 00-INDICE.md          índice de todo
├── 00-TEXTO/             cada PDF pasado a Markdown (para grep)
├── Clase 1/ 2/ 3/        diapositivas
└── Proyecto Final/       consignas, guía, ejemplo y el BMC del grupo

sincronizacion-campus/    el script que baja todo esto del campus
```

Para buscar en todo el material sin abrir un solo PDF:

```bash
grep -ri "modelo de madurez" "Material Campus/00-TEXTO"
```

## El sincronizador

`sincronizacion-campus/` baja el material del campus (Moodle de la FRSR) y lo reordena en
`Material Campus/`, además de pasar los PDF a texto. Es sólo librería estándar de Python.

```bash
cd sincronizacion-campus
python3 sync.py --login       # pide legajo y contraseña, guarda el token en .secrets/
python3 sync.py --descargar   # baja lo que falte
python3 sync.py --curso 1340  # otra materia (ids en config.json)
```

La contraseña no se guarda: sólo queda un token de web service en `.secrets/wstoken`, que
está en el `.gitignore`. **Nunca lo subas.** Cada uno usa su propia cuenta del campus.

Ver `sincronizacion-campus/README.md` para el detalle.

## Cómo colaborar

Tenés permiso de escritura: cloná, hacé tus cambios y pusheá. Para algo grande, mejor una
rama y un PR así lo vemos entre todos.

```bash
git clone https://github.com/emisorato1/gestion-gerencial-2026.git
```

Si subís algo nuevo, agregalo también a `Material Campus/00-INDICE.md`.

## Qué NO va en este repo

Es un repo público, así que el `.gitignore` deja afuera a propósito:

| Qué | Por qué |
|---|---|
| `.secrets/`, `wstoken` | credenciales del campus |
| `ESTADO.md`, `data/snapshot-*.json` | reportes generados con nombre de alumno, notas y userid |
| `Material Campus/Foros/` | nombres de compañeros y un link de invitación al grupo |
| `Material Campus/Cátedra/`, `*.webloc` | mails personales de la cátedra y la sala de clase virtual |

Todo eso sigue estando en el campus, que es donde corresponde. El texto de la presentación
introductoria sí está en `00-TEXTO/`, con los contactos removidos.
