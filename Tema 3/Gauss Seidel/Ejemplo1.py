import numpy as np

def resolver_seidel(A, b, iteraciones=10):
    n = len(A)
    x = np.zeros(n)
    for _ in range(iteraciones):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - s) / A[i][i]
    return x

# Sistema: 5x - 2y + 3z = -1 | -3x + 9y + z = 2 | 2x - y - 7z = 3
A1 = np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]])
b1 = np.array([-1, 2, 3])
print(f"Solución Ejemplo 1: {resolver_seidel(A1, b1)}")