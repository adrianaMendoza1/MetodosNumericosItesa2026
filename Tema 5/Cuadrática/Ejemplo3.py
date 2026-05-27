# Ejercicio 3: Costo de producción por volumen
import numpy as np

x = np.array([100.0, 200.0, 500.0])
y = np.array([50.0, 42.0, 35.0])
x_val = 300.0

A = np.vstack([x**2, x, np.ones_like(x)]).T
a, b, c = np.linalg.solve(A, y)
y_val = a * (x_val**2) + b * x_val + c

print("--- Ejercicio 3 ---")
print(f"Para producir {x_val} unidades, el costo estimado es de ${y_val:.2f}")