# Ejemplo base de interpolación cuadrática
import numpy as np

x = np.array([0.0, 1.0, 2.0])
y = np.array([5.0, 20.0, 25.0])
x_val = 1.5

# Resolver las constantes de la parábola (a, b, c)
A = np.vstack([x**2, x, np.ones_like(x)]).T
a, b, c = np.linalg.solve(A, y)

# Calcular el resultado
y_val = a * (x_val**2) + b * x_val + c

print("--- Ejemplo Base Cuadrática ---")
print(f"El resultado en x = {x_val} es y = {y_val:.2f}")