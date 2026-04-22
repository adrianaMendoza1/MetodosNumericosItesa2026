# Archivo: Ejercicio3.py
import math

def f(x):
    # f(x) = cos(x)
    return math.cos(x)

def regla_tres_puntos(x, h):
    return (-f(x + 2*h) + 4*f(x + h) - 3*f(x)) / (2 * h)

x0 = math.pi / 2 # Evaluando en 90 grados
h = 0.01
print(f"Ejercicio 3 - Derivada de cos(x) en x=pi/2: {regla_tres_puntos(x0, h):.6f}")