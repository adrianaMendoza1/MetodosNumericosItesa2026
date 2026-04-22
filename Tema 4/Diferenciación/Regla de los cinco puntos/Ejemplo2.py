# Archivo: Ejercicio2.py
import math

def f(x):
    # f(x) = ln(x)
    return math.log(x)

def regla_cinco_puntos(x, h):
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12 * h)

x0 = 2.0  # La derivada real debe ser 1/2 = 0.5
h = 0.01
print(f"Ejercicio 2 - Derivada de ln(x) en x={x0}: {regla_cinco_puntos(x0, h):.6f}")