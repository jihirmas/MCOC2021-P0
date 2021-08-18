# MCOC2021-P0

#P0-E1 Mi computador principal

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

# P0-E2

* Difiere en que mi gráfico contiene menos tamaños de matrices, es decir, el largo de la lista N es menor a que la del profesor.
* Las diferencias entre cada corrida se puede deber a que al momento de la ejecución del programa hay otros procesos en ejecución, por lo que hay variaciones pequeñas en la cantidad de recursos disponibles para la ejecución del py.
* Esto es justo por lo explicado en la pregunta anterior, ya que al tener menos recursos disponibles, el tiempo puede sufrir variaciones, ya sean de pérdida o de ganancia de tiempo.
* Versión 3.8
* Versión 1.20.2
* Si, se usa más de un procesador.
![image](https://user-images.githubusercontent.com/70209467/128419321-9774b867-c7bb-40f9-907a-c99a5cca2935.png)

# P0-E3

* Para la primera parte, se destaca que para numpy.linalg.inv, los tipos de datos half y longdouble no son admitidos debido a la codificación de tal librería. Para scipy funcionan los 4 tipos de datos
* Al correr todos los scripts, se nota que usar overwrite_a=True mejora notablemente el tiempo de ejecución, no así la cantidad de memoria.

Respondiendo a las preguntas...
¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta. 
-> Para el método de numpy.linalg.inv(), basicamente usa el algoritmo solve(A,I), donde I es la identidad, y lo resuelve mediante el algoritmo de factorización LU de lapack's. En cuanto a scipy.linalg.inv(), resuleve la inversa usando el método del pivoteo y la factorización LU. Scipy.linalg.inv() puede tener como parámetro overwrirte_a = (1,0), al ser 1, trabaja con los datos de la matriz entregada, mientras que en caso contrario, retornará una matriz creada desde 0. Usar el parámetro overwrite_a=True, mejoró notablemente el proceso de inversión en tiempo.
¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 
-> El paralelismo incide de manera positiva en el desempeño de cada caso, pues al usar todos los recursos disponibles (sin contar los autorizados por SUDO), la resolución de problemas es desarrollada de manera más rápida. El paralelismo se puede ver claramente en la siguiente imagen.

![image](https://user-images.githubusercontent.com/70209467/129839372-fe587cef-21d2-4312-957b-e51ff4266498.png)
