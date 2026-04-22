def f(x):
    return x**2 - 2

def df(x):
    # La derivada de x^2 - 2 es 2x
    return 2*x

def newton_raphson_detallado(x0, tol):
    print(f"{'Iter':<5} | {'xi':<10} | {'f(xi)':<10} | {'Error':<10}")
    print("-" * 50)
    
    xi = x0
    for i in range(1, 100):
        f_xi = f(xi)
        df_xi = df(xi)
        
        if df_xi == 0:
            print("Error: Derivada igual a cero. No hay solución.")
            return None
            
        # Fórmula: x_{i+1} = x_i - f(x_i) / f'(x_i)
        x_siguiente = xi - (f_xi / df_xi)
        error = abs(x_siguiente - xi)
        
        print(f"{i:<5} | {xi:<10.6f} | {f_xi:<10.6f} | {error:<10.6f}")
        
        if error < tol:
            print("-" * 50)
            return x_siguiente
            
        xi = x_siguiente
    return xi

# Punto inicial x0 = 1 y tolerancia 0.0001
raiz = newton_raphson_detallado(1, 0.0001)
print(f"Raíz aproximada: {raiz:.6f}")