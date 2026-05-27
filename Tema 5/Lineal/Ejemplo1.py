# Ejercicio 1: Temperatura de vapor de agua
x = [100.0, 150.0]
y = [99.61, 111.37]
x_val = 125.0

y_val = y[0] + ((y[1] - y[0]) / (x[1] - x[0])) * (x_val - x[0])

print("--- Ejercicio 1 ---")
print(f"A una presión de {x_val} kPa, la temperatura es {y_val:.2f} °C")