# Ejemplo base de interpolación lineal
x = [1.0, 2.0]
y = [3.0, 5.0]
x_val = 1.5

# Fórmula directa
y_val = y[0] + ((y[1] - y[0]) / (x[1] - x[0])) * (x_val - x[0])

print("--- Ejemplo Base ---")
print(f"Para x = {x_val}, el resultado es y = {y_val}")