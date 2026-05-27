# Ejercicio 1: Altura de un proyectil en el tiempo
import numpy as np

x = np.array([0.0, 1.0, 2.0])
y = np.array([5.0, 19.7, 24.6])
x_val = 1.5

A = np.vstack([x**2, x, np.ones_like(x)]).T
a, b, c = np.linalg.solve(A, y)
y_val = a * (x_val**2) + b * x_val + c

print("--- Ejercicio 1 ---")
print(f"A los {x_val} segundos, la altura es de {y_val:.2f} metros")