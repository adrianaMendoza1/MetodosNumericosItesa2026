# Ejemplo 2 de Runge-Kutta
def f(x, y): 
    return 2 * x

x0, y0, h, xf = 1.0, 0.0, 0.1, 0.3
while x0 < xf:
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + h/2, y0 + k1/2)
    k3 = h * f(x0 + h/2, y0 + k2/2)
    k4 = h * f(x0 + h, y0 + k3)
    y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
    x0 = round(x0 + h, 2)

print("--- Ejemplo 2 ---")
print(f"Resultado final en x = {x0}: y = {y0:.4f}")