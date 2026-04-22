import numpy as np

def jacobi(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy().astype(float)
    x_nuevo = np.zeros_like(x)
    
    print(f"{'Iter':<5} | {'x1':<10} | {'x2':<10} | {'x3':<10}")
    print("-" * 45)

    for k in range(max_iter):
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x_nuevo[i] = (b[i] - suma) / A[i][i]
        
        print(f"{k+1:<5} | {x_nuevo[0]:<10.6f} | {x_nuevo[1]:<10.6f} | {x_nuevo[2]:<10.6f}")
        
        if np.linalg.norm(x_nuevo - x, ord=np.inf) < tol:
            return x_nuevo
        
        x = x_nuevo.copy()
            
    return x

# Sistema diagonalmente dominante
A = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]])
b = np.array([6, 25, -11])
x_ini = np.zeros(3)

solucion = jacobi(A, b, x_ini, 1e-4, 20)
print("-" * 45)
print(f"Solución final Jacobi: {solucion}")