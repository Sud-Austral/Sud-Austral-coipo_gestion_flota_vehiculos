# Herramientas

## `leer_respaldo_gesad.py`

Convierte el respaldo de GESAD (export clásico de Oracle 9.2, archivo `.dmp`) en un CSV por tabla, sin necesidad de instalar Oracle. Lo usó la UIA para el [análisis de GESAD](../docs/gesad/analisis-gesad.md).

```
python -I leer_respaldo_gesad.py ruta/al/vehiculo.dmp carpeta_salida
```

Genera en `carpeta_salida`:
- un archivo `TABLA.csv` por tabla, con encabezado;
- `_resumen.json`, con las columnas, los tipos Oracle, el número de filas y si la lectura de cada tabla terminó bien.

Convierte números (`NUMBER`), fechas (`DATE`) y texto (`VARCHAR2`, `CHAR`, `LONG`). Las fechas inválidas se marcan como `INVALIDA:<bytes>` en vez de descartarse. Con el respaldo del 22-10-2026 las 77 tablas se leyeron completas.

**El respaldo y los CSV contienen datos personales y no se suben a este repositorio.** El archivo `.gitignore` excluye `*.dmp`, `*.csv` y la carpeta `datos/`. Se trabajan sólo en el entorno de la UIA.
