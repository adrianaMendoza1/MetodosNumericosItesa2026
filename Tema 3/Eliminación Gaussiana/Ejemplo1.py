import numpy as np

def resolver(A, b):
    return np.linalg.solve(A, b)

# 2x + 3y = 8
# 4x - y = 2
A = np.array([[2, 3], [4, -1]])
b = np.array([8, 2])

print(f"Solución Ejemplo 1: {resolver(A, b)}")