import numpy as np

def resolver_jacobi(A, b, iteraciones=15):
    n = len(A)
    x = np.zeros(n)
    for _ in range(iteraciones):
        x_nuevo = np.zeros(n)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x_nuevo[i] = (b[i] - s) / A[i][i]
        x = x_nuevo
    return x

A1 = np.array([[4, -1, 1], [4, -8, 1], [-2, 1, 5]])
b1 = np.array([7, -21, 15])
print(f"Solución Ejemplo 1: {resolver_jacobi(A1, b1)}")