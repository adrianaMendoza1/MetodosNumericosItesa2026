# Archivo: Ejercicio1.py
def f(x):
    # f(x) = x^3 - 2x + 1
    return x**3 - 2*x + 1

def regla_cinco_puntos(x, h):
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12 * h)

x0 = 1.0
h = 0.001
print(f"Ejercicio 1 - Derivada de x^3 - 2x + 1 en x={x0}: {regla_cinco_puntos(x0, h):.6f}")