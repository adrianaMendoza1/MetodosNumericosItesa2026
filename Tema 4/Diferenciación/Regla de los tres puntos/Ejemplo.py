# Archivo: Ejemplo.py
def f(x):
    # Definimos la función f(x) = x^2 + 2x
    return x**2 + 2*x

def regla_tres_puntos(x, h):
    # Fórmula: F'(X) ≈ (-f(x + 2h) + 4f(x + h) - 3f(x)) / 2h
    numerador = -f(x + 2*h) + 4*f(x + h) - 3*f(x)
    return numerador / (2 * h)

# Parámetros
x0 = 1.0  # Punto a evaluar
h = 0.001 # Tamaño del paso
resultado = regla_tres_puntos(x0, h)

print(f"Ejemplo - Función: x^2 + 2x")
print(f"La derivada aproximada en x={x0} es: {resultado:.6f}")