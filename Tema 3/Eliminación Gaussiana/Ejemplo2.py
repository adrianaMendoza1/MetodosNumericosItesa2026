import numpy as np

# x + y + z = 6
# 0x + 2y + 5z = -4
# 2x + 5y - z = 27
A = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
b = np.array([6, -4, 27])

print(f"Solución Ejemplo 2: {np.linalg.solve(A, b)}")