# Ejemplo base de Runge-Kutta (RK4)
def f(x, y): 
    return x - y

x0, y0, h, xf = 0.0, 1.0, 0.1, 0.2
while x0 < xf:
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + h/2, y0 + k1/2)
    k3 = h * f(x0 + h/2, y0 + k2/2)
    k4 = h * f(x0 + h, y0 + k3)
    y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
    x0 = round(x0 + h, 2)

print("--- Ejemplo Base Runge-Kutta ---")
print(f"Resultado en x = {x0}: y = {y0:.4f}")