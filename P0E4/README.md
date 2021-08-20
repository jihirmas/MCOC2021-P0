# MCOC2021-P0

# P0-E4

* Comentario Completo: Para el problema A, es decir, donde hay que resolver Ax=b, se usaron bastantes variaciones de una misma función, además de compararla con el caso bruto (hacerlo directamente como si fuese a papel). En el gráfico solve float.png y solve double.png, se puede apreciar que, independiente del tipo de dato, el tiempo de resolución es menor mientras más sobrepociciones hayan, es decir, overwrite_a o overwrite_b = True. En términos de procesador, se puede notar que se usa paralelismo y eso genera que la CPU no llegue al 100%. En cuanto a memoria, se obsera lo mismo que la entrega P0E3. En cuanto al problema B, de los vectores propios, se nota inmediatamente que es un problema mucho más complejo y largo de resolver. Se probaron los 9 casos descritos en el enucniado, y se observa que el que resuleve con mayor rapidez es el método con sus valores por defecto, donde el que más asombra es el overwrite_a, pues en las otras entregas se ha visto que esto mejora el rendimiento pero aquí eso no se cumple. Cabe destacar que para el caso de los vectores propios con tipo de dato double, se redujo el número de N hasta 2000 en vez de los 12500 que se utilizó en los otros. Esto se decidió ya que el timepo de ejecución estaba siendo extremadamente alto. (superior a la hora por cada caso)
* Respondiendo a las preguntas...
1) Para los vectores propis, se puede ver que la variabilidad del tiempo es cada vez mayor según aumenta el tamaño de la matriz, sin contar los valores inciales (pequeños). En cambio, para el método solve, se aprecia que la variación entre métodos se puede mantener constante.

2) El que gana en solve es el caso 7, es decir, con los overwrites True y assume por defecto. En cuanto a los vectores propios, gana el método con sus parámetros por defecto.

3) Claro que depende del tamaño de la matriz, ya que mientras mayor es esta, más recursos y tiempo toma la resolución de la misma.

4) Se debe a que en el caso de solve, el sobrescrimiento de datos sugiere un mejor uso del tiempo y de los recursos, ya que se utiliza menos ram. En cuanto a los vecotres propios, la eficiencia de la función es la destaca, siendo los parámetros adicionales solo modificaciones de la misma.

5) Si se utiliza más de un procesador, de hecho, durante toda la corrida se utilizaron todos los procesadores. La imagen del administrador de tareas era similar a la que se subió para la P0E3.

6) El uso de memoria crece logarítimicamente con factor N, es decir, en conjunto con el crecimiento de los N.

# P0-E3

* Para la primera parte, se destaca que para numpy.linalg.inv, los tipos de datos half y longdouble no son admitidos debido a la codificación de tal librería. Para scipy funcionan los 4 tipos de datos
* Al correr todos los scripts, se nota que usar overwrite_a=True mejora notablemente el tiempo de ejecución, no así la cantidad de memoria.

Respondiendo a las preguntas...

¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta. 

-> Para el método de numpy.linalg.inv(), basicamente usa el algoritmo solve(A,I), donde I es la identidad, y lo resuelve mediante el algoritmo de factorización LU de lapack's. En cuanto a scipy.linalg.inv(), resuleve la inversa usando el método del pivoteo y la factorización LU. Scipy.linalg.inv() puede tener como parámetro overwrirte_a = (1,0), al ser 1, trabaja con los datos de la matriz entregada, mientras que en caso contrario, retornará una matriz creada desde 0. Usar el parámetro overwrite_a=True, mejoró notablemente el proceso de inversión en tiempo.

¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 

-> El paralelismo incide de manera positiva en el desempeño de cada caso, pues al usar todos los recursos disponibles (sin contar los autorizados por SUDO), la resolución de problemas es desarrollada de manera más rápida. El paralelismo se puede ver claramente en la siguiente imagen.

![image](https://user-images.githubusercontent.com/70209467/129839372-fe587cef-21d2-4312-957b-e51ff4266498.png)

# P0-E2

* Difiere en que mi gráfico contiene menos tamaños de matrices, es decir, el largo de la lista N es menor a que la del profesor.
* Las diferencias entre cada corrida se puede deber a que al momento de la ejecución del programa hay otros procesos en ejecución, por lo que hay variaciones pequeñas en la cantidad de recursos disponibles para la ejecución del py.
* Esto es justo por lo explicado en la pregunta anterior, ya que al tener menos recursos disponibles, el tiempo puede sufrir variaciones, ya sean de pérdida o de ganancia de tiempo.
* Versión 3.8
* Versión 1.20.2
* Si, se usa más de un procesador.
![image](https://user-images.githubusercontent.com/70209467/128419321-9774b867-c7bb-40f9-907a-c99a5cca2935.png)


# P0-E1 

* Marca/modelo: HP Pavilion Gaming Laptop 16-a0004la
* Tipo: Notebook
* Año adquisición: 2021
* Procesador:
  * Marca/Modelo: Intel Core i7-10750H
  * Velocidad Base: 2.60 GHz
  * Velocidad Máxima: 5.00 GHz
  * Numero de núcleos: 6
  * Humero de hilos: 12
  * Arquitectura: x86_64
  * Set de instrucciones: MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, EM64T, VT-x, AES, AVX, AVX2, FMA3 (Todos Intel)
* Tamaño de las cachés del procesador
  * L1d: 32KB
  * L1i: 32KB
  * L2: 256KB
  * L3: 12 MB
* Memoria 
  * Total: 16 GB
  * Tipo memoria: DDR4
  * Velocidad 2933 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: Nvidia GeForce RTX 2060 con diseño Max-Q 
  * Memoria dedicada: 6 GB
  * Resolución: 1920 x 1080
* Disco 1: 
  * Marca: Samsung
  * Tipo: SSD
  * Tamaño: 512 GB
  * Particiones: 1
  * Sistema de archivos: NTFS
  
* Dirección MAC de la tarjeta wifi: FC:B3:BC:33:E8:70
* Dirección IP (Interna, del router): 192.168.0.89
* Dirección IP (Externa, del ISP): 201.223.26.106
* Proveedor internet: VTR Banda Ancha S.A.