# Ejemplo base de Newton (Diferencias Divididas)
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

# Datos de prueba sencillos
x_datos = [1.0, 2.0, 3.0]
y_datos = [10.0, 20.0, 40.0]
x_eval = 2.5

resultado = newton_interp(x_datos, y_datos, x_eval)
print("--- Ejemplo Base Newton ---")
print(f"El resultado en x = {x_eval} es {resultado:.2f}")