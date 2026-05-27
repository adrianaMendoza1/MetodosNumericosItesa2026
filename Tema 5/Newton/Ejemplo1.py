# Ejemplo 1: Calibración de un sensor de presión industrial
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

# Datos: Voltaje (V) vs Presión (psi)
x_datos = [1.0, 2.0, 3.0, 5.0]
y_datos = [1.5, 4.2, 9.1, 25.4]
x_eval = 4.0

resultado = newton_interp(x_datos, y_datos, x_eval)
print("--- Ejemplo 1 ---")
print(f"Para un voltaje de {x_eval} V, la presión estimada es de {resultado:.2f} psi")