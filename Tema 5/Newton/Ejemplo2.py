# Ejemplo 2: Perfil de temperatura en una barra de metal
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

# Datos: Distancia desde el origen (cm) vs Temperatura (°C)
x_datos = [0.0, 1.0, 3.0, 6.0]
y_datos = [100.0, 85.0, 60.0, 30.0]
x_eval = 2.0

resultado = newton_interp(x_datos, y_datos, x_eval)
print("--- Ejemplo 2 ---")
print(f"A los {x_eval} cm del origen, la temperatura estimada es de {resultado:.2f} °C")