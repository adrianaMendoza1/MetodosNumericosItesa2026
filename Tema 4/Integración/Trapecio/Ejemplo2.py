# Archivo: Ejercicio2.py
import math

def f(x):
    return math.sin(x)

def metodo_trapecio(a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        suma += 2 * f(a + i * h)
    return (h / 2) * suma

# Integrar de 0 a PI
print(f"Ejercicio 2 - Integral de sin(x): {metodo_trapecio(0, math.pi, 100):.4f}")