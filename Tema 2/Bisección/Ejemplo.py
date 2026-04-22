def f(x):
    return x**2 - 2

def biseccion_detallada(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Error: La función no cambia de signo en el intervalo.")
        return None

    print(f"{'Iter':<5} | {'a':<10} | {'b':<10} | {'c':<10} | {'f(c)':<10}")
    print("-" * 55)

    iteracion = 1
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        fc = f(c)
        
        # Imprime la fila actual de la tabla
        print(f"{iteracion:<5} | {a:<10.6f} | {b:<10.6f} | {c:<10.6f} | {fc:<10.6f}")

        if fc == 0:
            break
        elif f(a) * fc < 0:
            b = c
        else:
            a = c
        
        iteracion += 1
    
    return c

# Ejecución con intervalo [1, 2] y tolerancia de 0.01
raiz = biseccion_detallada(1, 2, 0.01)
print("-" * 55)
print(f"Resultado final: La raíz aproximada es {raiz:.4f}")