# Ejemplo 2 de Taylor de 2do Orden
x0, y0, h, xf = 0.0, 0.5, 0.2, 0.4
while x0 < xf:
    y0 = y0 + h * (y0) + (h**2 / 2) * (y0)
    x0 = round(x0 + h, 2)

print("--- Ejemplo 2 ---")
print(f"Resultado final en x = {x0}: y = {y0:.4f}")