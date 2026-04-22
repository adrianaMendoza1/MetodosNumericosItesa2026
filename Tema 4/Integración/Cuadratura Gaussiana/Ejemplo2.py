# Archivo: Ejercicio2.py
def f(x):
    return 1 / (1 + x)

def cuadratura_gaussiana_2p(a, b):
    nodos = [-0.5773502692, 0.5773502692]
    pesos = [1.0, 1.0]
    suma = 0
    for i in range(2):
        px = ((b - a) * nodos[i] + (a + b)) / 2
        suma += pesos[i] * f(px)
    return ((b - a) / 2) * suma

print(f"Ejercicio 2 - Integral de 1/(1+x) de 0 a 1: {cuadratura_gaussiana_2p(0, 1):.4f}")