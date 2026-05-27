# Ejercicio 3: Solubilidad de sal en agua
x = [20.0, 40.0]
y = [36.0, 36.6]
x_val = 32.0

y_val = y[0] + ((y[1] - y[0]) / (x[1] - x[0])) * (x_val - x[0])

print("--- Ejercicio 3 ---")
print(f"A una temperatura de {x_val} °C, la solubilidad es de {y_val:.2f} g")