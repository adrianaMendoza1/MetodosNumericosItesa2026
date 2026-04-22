import numpy as np

def resolver_seidel(A, b, iteraciones=20):
    n = len(A)
    x = np.zeros(n)
    for _ in range(iteraciones):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - s) / A[i][i]
    return x

# Sistema de 4 ecuaciones
A3 = np.array([[10, -1, 2, 0], 
               [-1, 11, -1, 3], 
               [2, -1, 10, -1], 
               [0, 3, -1, 8]])
b3 = np.array([6, 25, -11, 15])

print(f"Solución Ejemplo 3: {resolver_seidel(A3, b3)}")