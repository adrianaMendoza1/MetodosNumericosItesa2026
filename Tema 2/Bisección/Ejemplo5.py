def f(x):
    return x**3 + x**2 - 1

def biseccion(a, b, tol):
    if f(a) * f(b) >= 0:
        return "El método falla en este intervalo."
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0: break
        if f(a) * f(c) < 0: b = c
        else: a = c
    return c

print(f"Raíz Ejercicio 5: {biseccion(0, 1, 0.0001)}")