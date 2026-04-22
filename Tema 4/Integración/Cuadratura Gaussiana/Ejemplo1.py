# Archivo: Ejercicio1.py
def f(x):
    return x**3 + x**2 - 5

def cuadratura_gaussiana_2p(a, b):
    nodos = [-0.5773502692, 0.5773502692]
    pesos = [1.0, 1.0]
    suma = 0
    for i in range(2):
        px = ((b - a) * nodos[i] + (a + b)) / 2
        suma += pesos[i] * f(px)
    return ((b - a) / 2) * suma

print(f"Ejercicio 1 - Integral de x^3 + x^2 - 5: {cuadratura_gaussiana_2p(1, 2):.4f}")