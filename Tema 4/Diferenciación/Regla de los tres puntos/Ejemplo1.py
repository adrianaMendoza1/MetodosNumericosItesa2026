# Archivo: Ejercicio1.py
def f(x):
    # f(x) = x^3 - 4x + 5
    return x**3 - 4*x + 5

def regla_tres_puntos(x, h):
    return (-f(x + 2*h) + 4*f(x + h) - 3*f(x)) / (2 * h)

x0 = 2.0
h = 0.01
print(f"Ejercicio 1 - Derivada en x={x0}: {regla_tres_puntos(x0, h):.6f}")