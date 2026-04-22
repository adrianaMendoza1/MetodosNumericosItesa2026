# Archivo: Ejemplo.py
import math

def f(x):
    return math.exp(x)

def cuadratura_gaussiana_2p(a, b):
    # Puntos (nodos) y Pesos de Gauss para n=2 en el intervalo [-1, 1]
    nodos = [-0.5773502692, 0.5773502692]
    pesos = [1.0, 1.0]
    
    # Ajuste de intervalo [a, b] a [-1, 1]
    suma = 0
    for i in range(2):
        # Fórmula de cambio de variable
        punto_x = ((b - a) * nodos[i] + (a + b)) / 2
        suma += pesos[i] * f(punto_x)
    
    return ((b - a) / 2) * suma

print("Ejemplo Cuadratura Gaussiana (2 puntos)")
print(f"Integral de e^x de 0 a 1: {cuadratura_gaussiana_2p(0, 1):.6f}")