# Archivo: Ejemplo.py
import math

def f(x):
    # f(x) = sin(x)
    return math.sin(x)

def regla_cinco_puntos(x, h):
    # Fórmula: F'(X) ≈ (-f(x + 2h) + 8f(x + h) - 8f(x - h) + f(x - 2h)) / 12h
    numerador = -f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)
    denominador = 12 * h
    return numerador / denominador

# Parámetros
x0 = math.pi / 4  # Punto a evaluar
h = 0.01          # Tamaño del paso
result = regla_cinco_puntos(x0, h)

print(f"Ejemplo (5 puntos) - Función: sin(x)")
print(f"Punto x={x0}, h={h}")
print(f"La derivada aproximada es: {result:.6f}")