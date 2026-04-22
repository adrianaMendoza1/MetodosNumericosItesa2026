def f(x):
    return x**3 - 2*x**2 + x - 3

def df(x):
    return 3*x**2 - 4*x + 1

def newton(x0, tol):
    for i in range(100):
        divisor = df(x0)
        if divisor == 0: break 
        x1 = x0 - f(x0) / divisor
        if abs(x1 - x0) < tol: return x1
        x0 = x1
    return x0

print(f"Raíz Ejercicio 5: {newton(3, 0.0001)}")