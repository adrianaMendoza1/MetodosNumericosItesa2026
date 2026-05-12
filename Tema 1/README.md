# Tema 1: Teoría de Errores

## Concepto
En métodos numéricos, los errores son la diferencia entre el valor real de una magnitud y el valor calculado mediante un algoritmo. Las computadoras tienen una precisión finita, lo que genera pequeñas desviaciones que pueden acumularse.

Existen tres tipos principales de errores:
1. **Error Absoluto:** Es la diferencia física entre el valor real y el aproximado.
2. **Error Relativo:** Es el error absoluto dividido entre el valor real (da una idea de la importancia del error).
3. **Error Porcentual:** Es el error relativo multiplicado por 100.

### Fórmulas:
* **Error Absoluto:** $E_a = |V_{real} - V_{aprox}|$
* **Error Relativo:** $E_r = \frac{E_a}{|V_{real}|}$
* **Error Porcentual:** $E_p = E_r \times 100\%$

---

## Implementación y Ejemplos

### Ejemplo de Referencia
* [Cálculo de Errores Base](./Tema%201/Ejemplo.py)

### Ejemplos Prácticos
* [Ejemplo 1: Error de Redondeo](./Tema%201/Ejemplo1.py)
* [Ejemplo 2: Error de Truncamiento (Serie de Taylor)](./Tema%201/Ejemplo2.py)
* [Ejemplo 3: Precisión de Máquina (Épsilon)](./Tema%201/Ejemplo3.py)
* [Ejemplo 4: Error en Operaciones Aritméticas](./Tema%201/Ejemplo4.py)
* [Ejemplo 5: Conversión Decimal a Binario](./Tema%201/Ejemplo5.py)