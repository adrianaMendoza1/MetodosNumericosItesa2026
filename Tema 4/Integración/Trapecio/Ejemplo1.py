# Archivo: Ejercicio1.py
def f(x):
    return 3*x + 1

def metodo_trapecio(a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        suma += 2 * f(a + i * h)
    return (h / 2) * suma

print(f"Ejercicio 1 - Integral de 3x + 1: {metodo_trapecio(1, 3, 10):.4f}")