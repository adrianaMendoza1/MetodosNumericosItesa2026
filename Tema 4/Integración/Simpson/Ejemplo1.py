# Archivo: Ejercicio1.py
def f(x):
    return x**2 - x + 2

def regla_simpson(a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h
        suma += (4 * f(xi) if i % 2 != 0 else 2 * f(xi))
    return (h / 3) * suma

print(f"Ejercicio 1 - Simpson: {regla_simpson(0, 3, 20):.4f}")