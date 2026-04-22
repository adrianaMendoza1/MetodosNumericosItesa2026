import numpy as np

def eliminacion_gaussiana(A, b):
    n = len(b)
    # Matriz aumentada
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1).astype(float)
    print("Matriz Inicial:\n", Ab)

    # Proceso de eliminación
    for i in range(n):
        # Pivoteo parcial (opcional pero recomendado)
        for k in range(i + 1, n):
            if abs(Ab[i, i]) < abs(Ab[k, i]):
                Ab[[i, k]] = Ab[[k, i]]
        
        # Hacer ceros debajo del pivote
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
            print(f"\nEliminando fila {j} usando pivote en fila {i}:\n", Ab)

    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, n] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

# Sistema: 
# 3x + 2y - z = 1
# 2x - 2y + 4z = -2
# -x + 0.5y - z = 0
A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
b = np.array([1, -2, 0])

solucion = eliminacion_gaussiana(A, b)
print("\nSolución final:", solucion)