# Ejemplo base de Taylor de 2do Orden (y' = y, y'' = y)
x0, y0, h, xf = 0.0, 1.0, 0.1, 0.2
while x0 < xf:
    y0 = y0 + h * (y0) + (h**2 / 2) * (y0)
    x0 = round(x0 + h, 2)

print("--- Ejemplo Base Taylor ---")
print(f"Resultado en x = {x0}: y = {y0:.4f}")