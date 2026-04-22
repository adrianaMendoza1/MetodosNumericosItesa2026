import numpy as np

# 3x + 2y = 7
# x - y = -1
A = np.array([[3, 2], [1, -1]])
b = np.array([7, -1])

# Usamos linalg.solve que es el estándar de la industria
print(f"Solución Ejemplo 1: {np.linalg.solve(A, b)}")