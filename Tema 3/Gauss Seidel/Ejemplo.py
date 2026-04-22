import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy().astype(float)
    
    print(f"{'Iter':<5} | {'x':<10} | {'y':<10} | {'z':<10}")
    print("-" * 45)

    for k in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - suma) / A[i][i]
        
        # Imprimir progreso
        print(f"{k+1:<5} | {x[0]:<10.6f} | {x[1]:<10.6f} | {x[2]:<10.6f}")
        
        # Verificar convergencia (Error relativo)
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x
            
    return x

# Sistema diagonalmente dominante:
# 10x - y + 2z = 6
# -x + 11y - z = 25
# 2x - y + 10z = -11
A = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]])
b = np.array([6, 25, -11])
x_inicial = np.zeros(3)

solucion = gauss_seidel(A, b, x_inicial, 1e-4, 20)
print("-" * 45)
print(f"Solución final: {solucion}")