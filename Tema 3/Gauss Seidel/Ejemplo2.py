import numpy as np

def resolver_seidel(A, b, iteraciones=15):
    n = len(A)
    x = np.zeros(n)
    for _ in range(iteraciones):
        for i in range(n):
            # Suma de los elementos A[i][j] * x[j] excepto cuando i == j
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - s) / A[i][i]
    return x

# 4x + y = 5
# x + 3y = 4
A2 = np.array([[4, 1], [1, 3]])
b2 = np.array([5, 4])

print(f"Solución Ejemplo 2: {resolver_seidel(A2, b2)}")