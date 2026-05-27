# Tema_5
## Metodos_de_interpolación

#### Concepto

La interpolación en métodos numéricos es una técnica utilizada para aproximar valores de una función desconocida a partir de un conjunto discreto de puntos conocidos. Básicamente, consiste en encontrar una función que pase exactamente por los puntos dados. Esto es útil cuando se tiene un conjunto de datos discretos y se necesita estimar los valores de la función en puntos intermedios.

### Lineal
#### Concepto

El concepto básico de la interpolación lineal implica trazar una línea recta entre dos puntos conocidos en un gráfico, y luego utilizar esta línea para estimar el valor de la función en un punto que se encuentra entre estos dos puntos conocidos.

#### Algoritmo

  1. Obtener los puntos conocidos: Identifica los puntos conocidos (x0, y0) y (x1, y1) de los cuales deseas interpolar un valor en un punto x.
  2. Sustituir valores en la fórmula: Una vez que tengas los puntos conocidos y el punto en el que deseas interpolar (x), sustituye estos valores en la fórmula.
  3. Calcular el valor de y: Utiliza la fórmula para calcular el valor de y correspondiente al punto x utilizando los valores de x0, y0, x1, y1 y x.
  4. Resultado: El valor calculado de y es el resultado de la interpolación lineal en el punto x.

#### Implementación

* [Ejemplo](./Lineal/Ejemplo.py)

#### Ejercicios
* [Ejemplo 1](./Lineal/Ejercicio1.py)
* [Ejemplo 2](./Lineal/Ejercicio2.py)
* [Ejemplo 3](./Lineal/Ejercicio3.py)
---

### Cuadratica
#### Concepto

El concepto básico de la interpolación cuadrática implica seleccionar tres puntos de datos conocidos (x0, y0), (x1, y1) y (x2, y2)  y encontrar una parábola que pase exactamente a través de estos tres puntos.

#### Algoritmo
  1. Obtener los puntos conocidos: Identifica los tres puntos conocidos (x0, y0), (x1, y1) y (x2, y2) que utilizarás para realizar la interpolación cuadrática.
  2. Calcular el coeficiente cuadrático (𝑎): Utiliza la fórmula para calcular el coeficiente cuadrático 𝑎 utilizando los valores de los puntos conocidos.
  3. Calcular el coeficiente lineal (𝑏): Utiliza la fórmula para calcular el coeficiente lineal 𝑏 utilizando 𝑎 y los valores de los puntos conocidos.
  4. Calcular el término independiente (𝑐): Utiliza la fórmula para calcular el término independiente 𝑐 utilizando 𝑎, 𝑏 y los valores de los puntos conocidos.
  5. Evaluar el polinomio cuadrático: Utiliza el polinomio cuadrático 𝑦 = 𝑎𝑥^2 + 𝑏𝑥 + 𝑐 con los coeficientes calculados para evaluar el valor de 𝑦 en el punto de interés 𝑥.
  6. Mostrar el resultado: Muestra el valor interpolado de 𝑦 en el punto 𝑥.

#### Implementación
* [Ejemplo](./Cuadratica/Ejemplo.py)

#### Ejercicios
* [Ejemplo 1](./Cuadratica/Ejercicio1.py)
* [Ejemplo 2](./Cuadratica/Ejercicio2.py)
* [Ejemplo 3](./Cuadratica/Ejercicio3.py)

### Lagrange
#### Concepto
El método de Lagrange, también conocido como el método de interpolación de Lagrange, es una técnica matemática para encontrar un polinomio que pasa exactamente por un conjunto de puntos dados. Este método es muy útil en la interpolación de datos y en la aproximación de funciones. El polinomio resultante, llamado polinomio de interpolación de Lagrange, se construye de manera que cada valor del polinomio coincide con el valor de la función en cada uno de los puntos dados.
Dado un conjunto de n + 1 puntos distintos (x0, y0), (x1, y1), ..., (xn, yn) el objetivo es encontrar un polinomio P(x) de grado n

#### Algoritmo

  1. Inicializar el polinomio de interpolación:
     * 𝑃(𝑥) = 0.
  2. Para cada punto (𝑥𝑖,𝑦𝑖) en el conjunto de puntos:
     * Inicializar el polinomio básico de Lagrange 𝐿𝑖(𝑥)=1.
  3. Construir el polinomio básico 𝐿𝑖(𝑥) para cada 𝑖:
     * Para cada 𝑗 de 0 a 𝑛, donde 𝑗≠𝑖:
     * Actualizar 𝐿𝑖(𝑥) multiplicándolo por ((𝑥−𝑥𝑗)/(𝑥𝑖−𝑥𝑗))​.
  4. Actualizar el polinomio de interpolación 𝑃(𝑥):
     *Sumar al polinomio de interpolación 𝑃(𝑥) el término 𝑦𝑖⋅𝐿𝑖(𝑥).
  5. Simplificar
     *Simplificar 𝑃(𝑥) si es necesario para obtener el polinomio en su forma más simple.

#### Implementación
* [Ejemplo](./Lagrange/Ejemplo.py)

#### Ejercicios
* [Ejemplo 1](./Lagrange/Ejercicio1.py)
* [Ejemplo 2](./Lagrange/Ejercicio2.py)
* [Ejemplo 3](./Lagrange/Ejercicio3.py)

### Newton
#### Concepto

El método de interpolación de Newton es otra técnica para encontrar el polinomio que pasa por un conjunto de puntos dados. Se basa en las diferencias divididas de Newton y ofrece una forma alternativa al método de Lagrange para construir el polinomio de interpolación.
Dado un conjunto de n+1 puntos distintos (x0, y0), (x1, y1), ..., (xn, yn).

#### Algoritmo

  1. Inicializar las diferencias divididas:
     * Crear una tabla de diferencias divididas y asignar f(xi)=yi para i = 0, 1, 2, n
  2. Calcular las diferencias divididas:
     * Para cada 𝑗 desde 1 hasta 𝑛
       *Para cada 𝑖 desde 0 hasta 𝑛−𝑗
         *Calcular f[xi,xi+1,…,xi+j] usando la fórmula recursiva.
  3. Construir el polinomio de interpolación:
     * Iniciar el polinomio 𝑃(𝑥) con el primer coeficiente 𝑎0 = 𝑓[𝑥0].
     * Para cada 𝑘 desde 1 hasta 𝑛:
       *Añadir el término ak(x-x0)(x-x1)...(x-xk-1) al polinomio, donde ak = f[x0, x1, ..., xk]
​ ​ 
#### Implementación
* [Ejemplo](./Newton/Ejemplo.py)

#### Ejercicios
* [Ejemplo 1](./Newton/Ejercicio1.py)
* [Ejemplo 2](./Newton/Ejercicio2.py)
* [Ejemplo 3](./Newton/Ejercicio3.py)