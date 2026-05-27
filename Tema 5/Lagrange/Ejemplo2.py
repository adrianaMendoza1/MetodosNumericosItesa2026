# Ejemplo 2: Curva de potencia de un motor
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

# Datos: RPM (en miles) vs Caballos de Fuerza (HP)
x_puntos = [1.0, 2.0, 3.0, 4.0]
y_puntos = [50.0, 120.0, 210.0, 280.0]
x_eval = 2.5

resultado = lagrange(x_puntos, y_puntos, x_eval)
print("--- Ejemplo 2 ---")
print(f"A {x_eval} mil RPM, la potencia estimada es de {resultado:.2f} HP")