# Archivo: Ejemplo.py
def f(x):
    return x**2

def metodo_trapecio(a, b, n):
    # 1. Calcular h
    h = (b - a) / n
    # 2. Sumar f(a) y f(b)
    suma = f(a) + f(b)
    
    # 3. Sumar 2 * f(xi) para los puntos intermedios
    for i in range(1, n):
        xi = a + i * h
        suma += 2 * f(xi)
    
    # 4. Multiplicar por h/2
    resultado = (h / 2) * suma
    return resultado

# Parámetros: de 0 a 1 con 100 subintervalos
a, b, n = 0, 1, 100
print(f"Ejemplo - Integral de x^2 de {a} a {b}:")
print(f"Resultado: {metodo_trapecio(a, b, n):.6f}")