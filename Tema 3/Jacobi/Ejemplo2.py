import numpy as np

def resolver_jacobi(A, b, iteraciones=10):
    n = len(A)
    x = np.zeros(n)
    for _ in range(iteraciones):
        x_n = np.zeros(n)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x_n[i] = (b[i] - s) / A[i][i]
        x = x_n
    return x

A2 = np.array([[3, 1], [1, 2]])
b2 = np.array([5, 4])
print(f"Solución Ejemplo 2: {resolver_jacobi(A2, b2)}")