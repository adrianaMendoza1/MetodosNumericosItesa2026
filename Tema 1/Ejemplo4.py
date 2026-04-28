# Cómo se suma el error en operaciones
a_real, a_aprox = 5.0, 4.9
b_real, b_aprox = 10.0, 9.8

suma_real = a_real + b_real
suma_aprox = a_aprox + b_aprox

print(f"Error en la suma: {abs(suma_real - suma_aprox)}")