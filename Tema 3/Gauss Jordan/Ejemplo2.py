import numpy as np

# x + 2y + 3z = 9
# 4x + 5y + 6z = 24
# 3x + y - 2z = 4
A = np.array([[1, 2, 3], [4, 5, 6], [3, 1, -2]])
b = np.array([9, 24, 4])

print(f"Solución Ejemplo 2: {np.linalg.solve(A, b)}")