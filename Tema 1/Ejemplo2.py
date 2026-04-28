# Error al usar solo unos términos de una serie (Serie de Taylor para e^x)
import math

def exponencial_truncada(x, terminos):
    suma = 0
    for i in range(terminos):
        suma += (x**i) / math.factorial(i)
    return suma

real = math.exp(1) # e^1
aprox = exponencial_truncada(1, 3) # Solo 3 términos: 1 + x + x^2/2

print(f"e^1 Real: {real}")
print(f"e^1 Truncado (3 términos): {aprox}")
print(f"Error de truncamiento: {abs(real - aprox):.6f}")