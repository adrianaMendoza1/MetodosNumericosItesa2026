# Ejemplo 3: Esfuerzo mecánico en un material deformado
import numpy as np

def newton_interp(x, y, x_val):
    n = len(y)
    tabla = np.zeros([n, n])
    tabla[:,0] = y
    for j in range(1, n):
        for i in range(n - j):
            tabla[i,j] = (tabla[i+1,j-1] - tabla[i,j-1]) / (x[i+j] - x[i])
    p = tabla[0,0]
    multiplicador = 1.0
    for i in range(1, n):
        multiplicador *= (x_val - x[i-1])
        p += tabla[0,i] * multiplicador
    return p

# Datos: Deformación (mm) vs Esfuerzo (MPa)
x_datos = [0.1, 0.2, 0.4, 0.7]
y_datos = [45.0, 90.0, 160.0, 230.0]
x_eval = 0.5

resultado = newton_interp(x_datos, y_datos, x_eval)
print("--- Ejemplo 3 ---")
print(f"Para una deformación de {x_eval} mm, el esfuerzo es de {resultado:.2f} MPa")