# Archivo: Ejercicio3.py
def f(x):
    # f(x) = x^4 - 3x^2
    return x**4 - 3*x**2

def regla_cinco_puntos(x, h):
    # Esta regla es de orden h^4, por lo que con h=0.0001 debe ser muy precisa
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12 * h)

x0 = 0.5  # La derivada real es 4x^3 - 6x = -2.5
h = 0.0001
print(f"Ejercicio 3 - Derivada en x={x0}: {regla_cinco_puntos(x0, h):.6f}")