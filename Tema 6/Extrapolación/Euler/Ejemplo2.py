# Ejemplo 2 de Euler
def f(x, y): 
    return x - y

x0, y0, h, xf = 0.0, 0.5, 0.2, 0.6
while x0 < xf:
    y0 = y0 + h * f(x0, y0)
    x0 = round(x0 + h, 2)

print("--- Ejemplo 2 ---")
print(f"Resultado final en x = {x0}: y = {y0:.4f}")