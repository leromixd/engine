# ---------- данные ----------
VAR = 1
if VAR == 1:
    t1, t2 = [(25, 24.8), (0.8, 0.78)], 7.386
    a, ea, b, eb = 12, 0.1, 4, 0.1
    L, eL, W, eW = 20, 0.1, 10, 0.1
else:
    t1, t2 = [(40, 39.6), (1.5, 1.47)], 12.467
    a, ea, b, eb = 15, 0.1, 5, 0.1
    L, eL, W, eW = 30, 0.1, 20, 0.1
t5 = [(2, 0.1), (9, 0.1), (9.8, 0.1)]
a5, ea5 = 10, 0.1


def task1():
    print("== 1. Δ и δ ==")
    for x, xa in t1:
        D = abs(x - xa)
        R = D / abs(x) * 100 if x else None
        print(f"x={x}, ~{xa}: Δ={D:g}, δ={'—' if R is None else f'{R:.3f}%'}")

def task2():
    print("\n== 2. Округление / усечение ==")
    r = round(t2, 2)
    u = int(t2 * 100) / 100         
    print(f"x={t2}: round={r:.2f}, Δ={abs(t2-r):.4f}, граница h/2=0.005")
    print(f"trunc={u:.2f}, Δ={abs(t2-u):.4f}, граница < 0.01")

def task3():
    print("\n== 3. Четыре действия ==")
    rows = [
        ("сумма",    *add(a, b, ea, eb)),
        ("разность", *sub(a, b, ea, eb)),
        ("произв.",  *mul(a, b, ea, eb)),
        ("частное",  *div(a, b, ea, eb)),
    ]
    for name, z, e in rows:
        print(f"{name:<10} z={z:g}, ε={e:.3f}, r={rel(z, e):.3f}%")

def add(x, y, ex, ey): return x + y, ex + ey
def sub(x, y, ex, ey): return x - y, ex + ey
def mul(x, y, ex, ey): return x*y, abs(x)*ey + abs(y)*ex + ex*ey
def div(x, y, ex, ey):
    if abs(y) <= ey:
        raise ValueError("|b| <= εb: интервал содержит ноль")
    z = x / y
    e = (ex + abs(z)*ey) / (abs(y) - ey)
    return z, int(e*1000 + 0.9999999) / 1000

def rel(z, e):
    return e / abs(z) * 100 if z else float("nan")

def task4():
    print("\n== 4. Площадь ==")
    S, eS = mul(L, W, eL, eW)
    Smin, Smax = (L-eL)*(W-eW), (L+eL)*(W+eW)
    lo, hi = 0.98*S, 1.02*S
    print(f"S={S:g} см², εS={eS:.3f} см², r={eS/S*100:.3f}%")
    print(f"Smin={Smin:g}, Smax={Smax:g}, ±2% = [{lo:g}; {hi:g}]")
    print("гарантировано" if Smin >= lo and Smax <= hi else "НЕ гарантировано")

def task5():
    print("\n== 5. Вычитание ==")
    for b5, eb5 in t5:
        z, e = sub(a5, b5, ea5, eb5)
        r = e / abs(z) * 100 if z else float("nan")
        lo = round(z - e, 10) + 0.0
        hi = round(z + e, 10)
        print(f"b={b5}: z={z:g}, ε={e:g}, r={r:.2f}%, [{lo:g}; {hi:g}]")

def checks():
    print("\n== Проверки ==")
    _, e = mul(6, 2, 0.1, 0.1)
    print(f"6·2, ε=0.81 → {e:.4f}")
    try:
        div(1, 0.1, 0.1, 0.1)
    except ValueError as ex:
        print(f"деление при b=0.1±0.1 → {ex}")
    try:
        if -0.1 < 0:
            raise ValueError("граница отрицательна")
    except ValueError as ex:
        print(f"отрицательная ε → {ex}")

def main():
    task1(); task2(); task3(); task4(); task5(); checks()

main()
