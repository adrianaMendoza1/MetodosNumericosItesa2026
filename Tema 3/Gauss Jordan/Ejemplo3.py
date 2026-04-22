import numpy as np

# Sistema complejo de 4x4
A = np.array([[1, 1, 1, 1],
              [2, 3, 1, 5],
              [-1, 1, -5, 3],
              [3, 1, 7, -2]])
b = np.array([10, 31, -2, 18])

print(f"Solución Ejemplo 3: {np.linalg.solve(A, b)}")