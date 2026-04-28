# Demostración de cómo el redondeo afecta cálculos sucesivos
import math

v_real = math.pi
v_aprox = 3.1416

error = abs(v_real - v_aprox)
print(f"Valor de PI real: {v_real}")
print(f"Valor de PI redondeado: {v_aprox}")
print(f"Error generado por redondeo: {error:.10f}")