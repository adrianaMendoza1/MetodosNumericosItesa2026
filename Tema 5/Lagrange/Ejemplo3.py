# Ejemplo 3: Densidad de un fluido según la presión
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

# Datos: Presión (atm) vs Densidad (kg/m3)
x_puntos = [10.0, 20.0, 30.0, 40.0]
y_puntos = [1.2, 2.5, 3.9, 5.1]
x_eval = 25.0

resultado = lagrange(x_puntos, y_puntos, x_eval)
print("--- Ejemplo 3 ---")
print(f"A una presión de {x_eval} atm, la densidad es de {resultado:.2f} kg/m3")