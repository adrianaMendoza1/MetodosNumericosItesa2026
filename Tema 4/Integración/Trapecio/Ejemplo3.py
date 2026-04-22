# Archivo: Ejercicio3.py
import math

def f(x):
    return math.exp(x)

def metodo_trapecio(a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        suma += 2 * f(a + i * h)
    return (h / 2) * suma

print(f"Ejercicio 3 - Integral de e^x: {metodo_trapecio(0, 2, 50):.4f}")