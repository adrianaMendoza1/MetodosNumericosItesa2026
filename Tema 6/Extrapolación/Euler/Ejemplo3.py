# Ejemplo 3 de Euler
def f(x, y): 
    return x**2 + y

x0, y0, h, xf = 1.0, 2.0, 0.1, 1.3
while x0 < xf:
    y0 = y0 + h * f(x0, y0)
    x0 = round(x0 + h, 2)

print("--- Ejemplo 3 ---")
print(f"Resultado final en x = {x0}: y = {y0:.4f}")