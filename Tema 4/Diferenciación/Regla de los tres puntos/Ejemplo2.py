# Archivo: Ejercicio2.py
import math

def f(x):
    # f(x) = e^x
    return math.exp(x)

def regla_tres_puntos(x, h):
    return (-f(x + 2*h) + 4*f(x + h) - 3*f(x)) / (2 * h)

x0 = 0.0
h = 0.0001
print(f"Ejercicio 2 - Derivada de e^x en x={x0}: {regla_tres_puntos(x0, h):.6f}")