# Gestión Gerencial 2026 — UTN FRSR

Material de la cátedra de **Gestión Gerencial** (5.º año, Ingeniería en Sistemas de
Información, UTN Facultad Regional San Rafael), ordenado para leerlo y buscarlo más rápido
que en el campus.

## Qué hay acá

```
Material Campus/
├── 00-INDICE.md        índice de todo
├── 00-TEXTO/           cada PDF pasado a Markdown (para grep)
├── Clase 1/ 2/ 3/      diapositivas
└── Proyecto Final/     consignas, guía, ejemplo y el BMC del grupo
```

Para buscar en todo el material sin abrir un solo PDF:

```bash
grep -ri "modelo de madurez" "Material Campus/00-TEXTO"
```

## Cómo colaborar

Tenés permiso de escritura: cloná, hacé tus cambios y pusheá. Para algo grande, mejor una
rama y un PR así lo vemos entre todos.

```bash
git clone https://github.com/emisorato1/gestion-gerencial-2026.git
```

Si subís algo nuevo, agregalo también a `Material Campus/00-INDICE.md`.

## Qué NO va en este repo

Es un repo público, así que quedan afuera a propósito:

- los foros del campus (tienen nombres de compañeros y un link de invitación al grupo)
- el enlace a la sala de la clase virtual
- el PDF de la presentación introductoria (trae los mails personales de la cátedra); su
  texto sí está en `00-TEXTO/`, con los contactos removidos
- credenciales y tokens del campus

Todo eso sigue estando en el campus, que es donde corresponde.
