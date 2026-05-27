# Ejercicio 2: Resistencia eléctrica según la temperatura
import numpy as np

x = np.array([20.0, 50.0, 80.0])
y = np.array([10.5, 11.8, 13.4])
x_val = 60.0

A = np.vstack([x**2, x, np.ones_like(x)]).T
a, b, c = np.linalg.solve(A, y)
y_val = a * (x_val**2) + b * x_val + c

print("--- Ejercicio 2 ---")
print(f"A una temperatura de {x_val}°C, la resistencia es {y_val:.2f} Ohms")