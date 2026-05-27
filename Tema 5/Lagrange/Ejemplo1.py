# Ejemplo 1: Crecimiento biológico de bacterias
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

# Datos: Horas vs Población
x_puntos = [0.0, 2.0, 4.0, 6.0]
y_puntos = [100.0, 250.0, 600.0, 1350.0]
x_eval = 3.5

resultado = lagrange(x_puntos, y_puntos, x_eval)
print("--- Ejemplo 1 ---")
print(f"La población estimada en la hora {x_eval} es de {resultado:.2f} bacterias")