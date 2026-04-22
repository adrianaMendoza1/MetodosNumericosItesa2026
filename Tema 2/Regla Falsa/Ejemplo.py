def f(x):
    return x**3 - 2*x - 5

def regla_falsa(a, b, tol):
    if f(a) * f(b) >= 0:
        return "El método falla: f(a) y f(b) deben tener signos opuestos."

    print(f"{'Iter':<5} | {'a':<10} | {'b':<10} | {'c':<10} | {'f(c)':<10}")
    print("-" * 55)

    c_ant = a
    for i in range(1, 100):
        # Fórmula de Regla Falsa (Interpolación lineal)
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        
        print(f"{i:<5} | {a:<10.6f} | {b:<10.6f} | {c:<10.6f} | {f(c):<10.6f}")

        if abs(f(c)) < tol or abs(c - c_ant) < tol:
            break
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c_ant = c
    return c

print(f"\nRaíz aproximada: {regla_falsa(1, 3, 0.0001)}")