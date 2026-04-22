# Archivo: Ejercicio3.py
import math

def f(x):
    return math.sin(x)**2

def cuadratura_gaussiana_2p(a, b):
    nodos = [-0.5773502692, 0.5773502692]
    pesos = [1.0, 1.0]
    suma = 0
    for i in range(2):
        px = ((b - a) * nodos[i] + (a + b)) / 2
        suma += pesos[i] * f(px)
    return ((b - a) / 2) * suma

print(f"Ejercicio 3 - Integral de sin^2(x): {cuadratura_gaussiana_2p(0, math.pi):.4f}")