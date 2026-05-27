# Ejercicio 2: Estiramiento de un resorte
x = [10.0, 20.0]
y = [2.5, 5.2]
x_val = 15.0

y_val = y[0] + ((y[1] - y[0]) / (x[1] - x[0])) * (x_val - x[0])

print("--- Ejercicio 2 ---")
print(f"Con una fuerza de {x_val} N, el resorte se estira {y_val:.2f} cm")