def f(x):
    return x**2 - 4

def metodo_secante(x0, x1, tol, max_iter):
    print(f"{'Iter':<5} | {'x0':<10} | {'x1':<10} | {'x_nueva':<10} | {'Error':<10}")
    print("-" * 55)
    
    for i in range(1, max_iter + 1):
        if f(x1) - f(x0) == 0:
            print("División por cero. El método falló.")
            return None
        
        # Fórmula del método de la Secante
        x_nueva = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        error = abs(x_nueva - x1)
        
        print(f"{i:<5} | {x0:<10.6f} | {x1:<10.6f} | {x_nueva:<10.6f} | {error:<10.6f}")
        
        if error < tol:
            return x_nueva
        
        x0 = x1
        x1 = x_nueva
        
    return x1

# Ejecución: x0=0, x1=1, tol=0.0001
raiz = metodo_secante(0, 1, 0.0001, 20)
print("-" * 55)
print(f"Raíz aproximada: {raiz:.6f}")