# Archivo: Ejemplo.py
def f(x):
    return x**4

def regla_simpson(a, b, n):
    if n % 2 != 0: n += 1 # Asegurar que n sea par
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        xi = a + i * h
        if i % 2 == 0:
            suma += 2 * f(xi) # Términos pares
        else:
            suma += 4 * f(xi) # Términos impares
            
    return (h / 3) * suma

a, b, n = 0, 2, 10
print(f"Ejemplo Simpson - Integral de x^4 de {a} a {b}:")
print(f"Resultado: {regla_simpson(a, b, n):.6f}")