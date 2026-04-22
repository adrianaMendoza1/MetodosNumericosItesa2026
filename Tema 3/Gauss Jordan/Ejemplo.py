import numpy as np

def gauss_jordan(A, b):
    n = len(b)
    # Matriz aumentada
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1).astype(float)
    print("Matriz Inicial:\n", Ab)

    for i in range(n):
        # Hacer que el pivote sea 1
        pivot = Ab[i, i]
        Ab[i] = Ab[i] / pivot
        print(f"\nNormalizando fila {i} (Pivote = 1):\n", Ab)

        # Hacer ceros en toda la columna (arriba y abajo del pivote)
        for j in range(n):
            if i != j:
                factor = Ab[j, i]
                Ab[j] -= factor * Ab[i]
        print(f"Haciendo ceros en columna {i}:\n", Ab)
    
    return Ab[:, n]

# Sistema:
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3
A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b = np.array([8, -11, -3])

solucion = gauss_jordan(A, b)
print("\nSolución Final (x, y, z):", solucion)