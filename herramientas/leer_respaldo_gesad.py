"""Lector mínimo de export clásico de Oracle (exp v9) para el respaldo de GESAD.

Uso:  python -I leer_respaldo_gesad.py RUTA/vehiculo.dmp CARPETA_SALIDA

Escribe un CSV por tabla y _resumen.json con columnas, tipos, filas y si la lectura terminó bien.
Los CSV contienen datos personales: no se versionan (ver .gitignore)."""
import re, struct, sys, csv, json, datetime

src, out = sys.argv[1], sys.argv[2]
d = open(src, "rb").read()


def num(b):
    if not b:
        return None
    e = b[0]
    if e == 0x80:
        return 0
    if e & 0x80:
        exp = (e & 0x7F) - 65
        digs = [x - 1 for x in b[1:]]
        neg = False
    else:
        exp = ((~e) & 0x7F) - 65
        bb = b[1:]
        if bb and bb[-1] == 102:
            bb = bb[:-1]
        digs = [101 - x for x in bb]
        neg = True
    v = 0
    for k, dg in enumerate(digs):
        pw = exp - k
        v += dg * (100 ** pw) if pw >= 0 else dg / (100 ** (-pw))
    if isinstance(v, float):
        v = round(v, 6)
        if v.is_integer():
            v = int(v)
    return -v if neg else v


def fecha(b):
    if len(b) < 7:
        return None
    y = (b[0] - 100) * 100 + (b[1] - 100)
    try:
        return datetime.datetime(y, b[2], b[3], b[4] - 1, b[5] - 1, b[6] - 1).isoformat(sep=" ")
    except Exception:
        return "INVALIDA:" + b.hex()


def leer_tabla(p, n, types):
    rows, ok = [], True
    while True:
        if d[p:p + 2] == b"\xff\xff":
            break
        row = []
        try:
            for k in range(n):
                ln = struct.unpack_from("<H", d, p)[0]
                p += 2
                if ln == 0xFFFE:
                    row.append(None)
                    continue
                b = d[p:p + ln]
                p += ln
                ty = types[k]
                if ty == 2:
                    v = num(b)
                elif ty == 12:
                    v = fecha(b)
                elif ty in (1, 96, 8):
                    v = b.decode("latin-1")
                else:
                    v = f"<tipo {ty}: {ln} bytes>"
                row.append(v)
            if d[p:p + 2] != b"\x00\x00":
                return rows, False
            p += 2
            rows.append(row)
        except Exception:
            return rows, False
    return rows, ok


res = {}
for m in re.finditer(rb'INSERT INTO "([A-Z0-9_$#]+)" \(([^)]*)\) VALUES \([^)]*\)\n', d):
    t = m.group(1).decode()
    cols = [c.strip().strip('"') for c in m.group(2).decode().split(",")]
    p = m.end()
    n = struct.unpack_from("<H", d, p)[0]
    p += 2
    types = []
    for _ in range(n):
        ty, _ln = struct.unpack_from("<HH", d, p)
        p += 4
        if ty in (1, 96):
            p += 4
        types.append(ty)
    if d[p:p + 4] != b"\x00\x00\x00\x00":
        res[t] = {"cols": cols, "types": types, "rows": 0, "ok": False, "nota": "descriptor no reconocido"}
        continue
    rows, ok = leer_tabla(p + 4, n, types)
    res[t] = {"cols": cols, "types": types, "rows": len(rows), "ok": ok}
    with open(f"{out}/{t}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)

json.dump(res, open(f"{out}/_resumen.json", "w"), indent=1)
for t, r in sorted(res.items()):
    print(f"{t:32} {r['rows']:>9} {'OK' if r['ok'] else 'CORTE'}  {len(r['cols'])} col")
