# Ejemplo base de Lagrange
def lagrange(x, y, x_val):
    n = len(x)
    suma = 0
    for i in range(n):
        termino = y[i]
        for j in range(n):
            if i != j:
                termino *= (x_val - x[j]) / (x[i] - x[j])
        suma += termino
    return suma

# Datos de prueba sencillos
x_puntos = [1.0, 2.0, 3.0]
y_puntos = [2.0, 4.0, 8.0]
x_eval = 1.5

resultado = lagrange(x_puntos, y_puntos, x_eval)
print("--- Ejemplo Base Lagrange ---")
print(f"El resultado en x = {x_eval} es {resultado:.2f}")