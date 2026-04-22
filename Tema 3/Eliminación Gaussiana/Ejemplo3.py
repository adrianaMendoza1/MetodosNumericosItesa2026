import numpy as np

# Sistema de 4 variables
A = np.array([[1, -1, 2, -1], 
              [2, -2, 3, -3], 
              [1, 1, 1, 0], 
              [1, -1, 4, 3]])
b = np.array([-8, -20, -2, 4])

print(f"Solución Ejemplo 3: {np.linalg.solve(A, b)}")