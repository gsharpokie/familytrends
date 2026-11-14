"""Rebuilds the data block for index.html from the Census Bureau's historical tables.

Usage:  python3 build_data.py FOLDER_WITH_XLS_FILES > data.js
Needs:  pip install xlrd
Files (from https://www2.census.gov/programs-surveys/demo/tables/families/time-series/):
  marital/ms2.xls  children/ch1.xls  households/hh1.xls  households/hh4.xls
  households/hh6.xls  adults/ad1.xls
Where a year has an original and a revised ("r") row, the revised row is used.
For 2007 in CH-1, the row using the newer two-parent method ("y") is used.
The divorce and nonmarital-birth series are typed by hand in index.html (see README).
"""
import sys, re, json, xlrd

def rows(path):
    sh = xlrd.open_workbook(path).sheet_by_index(0)
    return [[c.value for c in sh.row(r)] for r in range(sh.nrows)]

def year_key(v):
    """Returns (year, rank). Higher rank wins when a year appears twice."""
    s = str(v).strip().lstrip(".")
    m = re.match(r"(\d{4})(?:\.0)?\s*(.*)", s)
    if not m: return None
    y, tag = int(m.group(1)), m.group(2).lower()
    if "census" in tag: return (y, 1)
    rank = 1
    if "r" in tag.replace("census", ""): rank = 3
    if "x" in tag: rank = 0
    return (y, rank)

def series(path, fn, start=None, stop=None):
    out, best = {}, {}
    for r in rows(path)[start:stop]:
        k = year_key(r[0])
        if not k: continue
        try: v = fn(r)
        except (ValueError, TypeError, ZeroDivisionError): continue
        if v is None: continue
        y, rank = k
        if y not in best or rank > best[y]:
            best[y] = rank; out[y] = v
    return dict(sorted(out.items()))

num = lambda x: float(x)
pct = lambda a, b: round(100 * num(a) / num(b), 1)
d = sys.argv[1].rstrip("/") + "/"

S = {}
S["AGE_M"] = series(d + "ms2.xls", lambda r: num(r[1]))
S["AGE_W"] = series(d + "ms2.xls", lambda r: num(r[2]))
S["KID_TWO"] = series(d + "ch1.xls", lambda r: pct(r[2], r[1]))
S["KID_MOM"] = series(d + "ch1.xls", lambda r: pct(r[5], r[1]))
S["KID_DAD"] = series(d + "ch1.xls", lambda r: pct(r[6], r[1]))
S["KID_NONE"] = series(d + "ch1.xls", lambda r: pct(num(r[8]) + num(r[9]), r[1]))
S["HH_MARRIED"] = series(d + "hh1.xls", lambda r: pct(r[3], r[1]))
S["HH_ALONE"] = series(d + "hh4.xls", lambda r: pct(r[2], r[1]))
S["HH_SIZE"] = series(d + "hh6.xls", lambda r: round(num(r[2]), 2))

# AD-1 has two blocks: ages 18-24, then 25-34
ad = rows(d + "ad1.xls")
i24 = next(i for i, r in enumerate(ad) if "18 to 24" in str(r[0]))
i34 = next(i for i, r in enumerate(ad) if "25 to 34" in str(r[0]))
S["YA_M_1824"] = series(d + "ad1.xls", lambda r: round(num(r[3]), 1), i24, i34)
S["YA_W_1824"] = series(d + "ad1.xls", lambda r: round(num(r[7]), 1), i24, i34)
S["YA_M_2534"] = series(d + "ad1.xls", lambda r: round(num(r[3]), 1), i34)
S["YA_W_2534"] = series(d + "ad1.xls", lambda r: round(num(r[7]), 1), i34)

for k, v in S.items():
    print("const %s = {%s};" % (k, ",".join("%d:%s" % (y, json.dumps(x)) for y, x in v.items())))
