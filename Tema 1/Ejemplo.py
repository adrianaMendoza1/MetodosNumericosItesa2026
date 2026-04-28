# Cálculo general de errores
def calcular_errores(v_real, v_aprox):
    e_absoluto = abs(v_real - v_aprox)
    e_relativo = e_absoluto / abs(v_real)
    e_porcentual = e_relativo * 100
    
    print(f"Valor Real: {v_real}")
    print(f"Valor Aproximado: {v_aprox}")
    print("-" * 30)
    print(f"Error Absoluto: {e_absoluto:.6f}")
    print(f"Error Relativo: {e_relativo:.6f}")
    print(f"Error Porcentual: {e_porcentual:.4f}%")

# Ejemplo: Medir un tornillo de 10cm que se midió como 9.92cm
calcular_errores(10, 9.92)