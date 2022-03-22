# Solving Time Calculator
### Por Nicolás Bosoni Spinetto - Pycharm 3.2
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

    
> Este cuaderno NO ESTÁ pensado para ser ejecutado por bloques, la idea es que puedas leer y desarrollar código paso a paso para que entiendas qué sucede y cómo se pensó en resolver el ejercicio. SI tratas de ir ejecutando cada código de forma separada probablemente tengas muchos errores.


**Reglas de Lectura:**

Primero debes leer con atención el problema original el cual he extendido en la parte superior para que puedas comprenderlo. Está en inglés, por lo tanto te recomiendo que lo leas detenidamente y entiendas muy bien cada una de las partes, ya que la mala interpretación puede llevar a tomar caminos erróneos en el proceso (me pasó por no leer completo 2 veces) y eso hace perder tiempo eficiencia para resolver los desafíos. Otra sugerencia importante es fijarse en las salidas; si esta indica un "punto final" al terminar el mensaje de salida, debes ponerlo o el template/pattern del sistema al que debes subir tu solución, no lo permitirá y arrojará errores. Debes entender muy bien la diferencia entre el statement PRINT y RETURN, no haré hincapié en ello, pero sugiero que leas y veas código o youtube para que te acostumbres y no llenes de breaks cosas por ahí pensando en que va a saltar algo fuera de la consola.

**Problema**

Se pide agregar tiempo dato en formato de horas (cualquier número y minutos) a una hora inicial. Se indica la hora, minutos, el meridiano y opcionalmente puede indicar el día de la semana

```
add_time("11:43 AM", "00:20")
Returns: 12:03 PM

add_time("11:30 AM", "2:32", "Monday")
Returns: 2:02 PM, Monday

add_time("10:10 PM", "3:30")
Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
Returns: 12:03 AM, Thursday (2 days later
```


**Resumen de las reglas del Problema**

```
A - Entradas obligatorias: 2; Tiempo de Inicio con Meridiano, Tiempo agregado.
B - Entrada Opcional: Día de la Semana de Inicio.
C - No importe Librerías, el usuario siempre ingresará lo espablecido en el modelo anterior
D - El tiempo de incio debe ir en Formato de 12 horas y con su meridiano.
E - El tiempo agregado puede ser cualquier número en las horas y los minutos en formato de 60 minutos.
F - La salida resultante debe considerar el formato horario de 12 horas con meridiano, si es el día siguiente debe indicar el día y (next day)
G - Si la salida son más de n días, debe indicar el día y (n days later)

```

**Análisis Previo**

Identificamos inmediatamente que debemos definir un valor por defaul para los días, y las salidas claramente deben resultar en dias, horas y minutos. Dada la capacidad numérica, trabajaremos en el formato de 24 horas, para transformar los números a minutos y horas y realizar las operaciones correspondientes. En este sentido ya hemos complicado el análisis, teniendo en cuenta que vamos a dividir cada uno de los elementos en partes.

EL formato de 24 hora tiene algunas condiciones, por ejemplo las 12:00AM corresponden a las 00:00, desde las 1:am a las 11:59 se corresponde pero desde las 12.00PM hasta las 11:59 PM el formato de 24 horas cambia y suma 12 dígitos. Este ejercicio no requiere funciones así que probablemente nos demos algunas vueltas en if..elif y algún while. Sería bueno, sabiendo que trabajaremos con un día de semana, tener una lista en caso "de" con los días.



## PARTE 1

**Definimos la Función**

Comenzamos definiendo la función del problema. Notese que agregamos inmediatamente la variable dia como vacío en valor default.

```python
def add_time(start, duration, day =''):
    # definimos los elementos que vamos a usar
   return new_time
```

**Encabezados de Salida**

Vamos a recibir el tiempo de inicio y lo vamos a dividir 2 elementos (hora:minutos, meridiano), el tiempo de duración lo mantenemos por ahora y tomamos, de lo que mencionamos anteriormente, la lista con los dáis de la semana.

>**split()**: 

```python
def add_time(start, duration, day =''):
    # definimos los elementos que vamos a usar
     st_time = start.split()
    dr_time = duration
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    return new_time
```

**Separando los elementos**

Tenemos que entender a esta altura y muy bien, como manipular una lista a través de un índice o a travéz del desplazamiento. Primero obtendremos la Hora mediante el índice en la posición 0 del elemento que separamos.
Este elemento debe estar en el formato ##:## ya que es numerico pero iene los ':' entremedio. Rápidamente con un desplazamiento dentro de ese elemento podemos obtener sus partes con el index()

> **index()**: 

En el índice 1 se encuentra en este momento el meridiano, notese ue debe estar en mayúsculas porque está dentro del formato solicitado así que utilizaremos la función upper() para tansformarlo.

>**upper()**

```python
    # Separo la Hora en Partes
    stt_time = st_time[0] # obtengo la Hora
    stt_hour = int(stt_time[:stt_time.index(':')])
    stt_minutes = int(stt_time[stt_time.index(':')+1:])
    stt_cicle = st_time[1].upper()
```
Entonces tenemos la Hora, los minutos y el Meridiano cada uno en sus variables. Replicamos sólo la búsqueda posicional en el tiempo de duración ya que al no tener meridiano no requiere separarlo en partes.

```python
    # Separo la Hora en Partes
    stt_time = st_time[0] # obtengo la Hora
    stt_hour = int(stt_time[:stt_time.index(':')])
    stt_minutes = int(stt_time[stt_time.index(':')+1:])
    stt_cicle = st_time[1].upper()
    
        # Separo el tiempo de duración
    drt_hour = int(dr_time[:dr_time.index(':')])
    drt_minutes = int(dr_time[dr_time.index(':')+1:])
```

**Resolviendo los tiempos**

Creo que es una de las cosas que más me dio dificultades, ya que debía considerar el meridiano por cada una de las proseciones del tiempo.
Para tener una idea, primero vamos a calular las horas totales y los minutos totales que tenemos, como números duros, sin transformar; esto nos va a permitir operar luego en el formato de 24 horas y realizar las transformaciones finales más adelante.

```python
  # Tiempos Totales en minutos
    min_plus = drt_minutes + stt_minutes
    hr_plus = drt_hour + stt_hour
```

Ahora necesitamos pasar estas horas y minutos a un formato que sea cómodo y sin tanto condicional dado por el meridiano (AM y PM), entonces para cada caso evaluaremos el meridiano y la Hora.
Además, cada veaz que los minutos sobrepasen los 60 minutos, debemos pasarle los dígitos que correspondan a las horas y dejar el residual de los minutos. Es parte de las reglas del ejercicio.

>**// o % (conocido como mod)**: 

```python
 # si la hora está entre las las 00.00 AM y las 11.59 AM (siguen igual)
    if(stt_cicle.upper() == 'AM' and stt_hour == 12):
        hr_plus = drt_hour + (min_plus //60)
        min_plus = min_plus % 60

    # si la Hora está entre las 1PM y las 11.59PM Le suma 12 horas
    elif(stt_cicle.upper() == 'PM' and (stt_hour >= 1 and stt_hour <= 11)):
            hr_plus = hr_plus + (min_plus //60) + 12
            min_plus = min_plus % 60
    else:
            hr_plus = hr_plus + (min_plus //60)
            min_plus = min_plus % 60
            
     print(f'Hora Original: {stt_time} {stt_cicle}')
     print(f'Check OP: {hr_plus} hr y {min_plus} min Acumulados')
```
Con los prints anteriores, mirando además los datos de entrada, nos podemos hacer una idea sobre qué estamos haciendo realmente.

Hasta Ahora el código acumulado va así:
```python
def add_time(start, duration, day =''):
    # definimos los elementos que vamos a usar
    st_time = start.split()
    dr_time = duration
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Separo la Hora en Partes
    stt_time = st_time[0] # obtengo la Hora
    stt_hour = int(stt_time[:stt_time.index(':')])
    stt_minutes = int(stt_time[stt_time.index(':')+1:])
    stt_cicle = st_time[1].upper()

    # Separo el tiempo de duración
    drt_hour = int(dr_time[:dr_time.index(':')])
    drt_minutes = int(dr_time[dr_time.index(':')+1:])

    # Tiempos Totales en minutos
    min_plus = drt_minutes + stt_minutes
    hr_plus = drt_hour + stt_hour

    # si la hora está entre las las 00.00 AM y las 11.59 AM (siguen igual)
    if(stt_cicle.upper() == 'AM' and stt_hour == 12):
        hr_plus = drt_hour + (min_plus //60)
        min_plus = min_plus % 60

    # si la Hora está entre las 1PM y las 11.59PM Le suma 12 horas
    elif(stt_cicle.upper() == 'PM' and (stt_hour >= 1 and stt_hour <= 11)):
            hr_plus = hr_plus + (min_plus //60) + 12
            min_plus = min_plus % 60
    else:
            hr_plus = hr_plus + (min_plus //60)
            min_plus = min_plus % 60

    #print(f'Hora Original: {stt_time} {stt_cicle}')
    #print(f'Check OP: {hr_plus} hr y {min_plus} min Acumulados')
    
    # Aquí viene más Cödigo...
    
    return new_time
```

## PARTE 2
Bien trabajamos los número en el formato de 24 horas porque era más simple operarlos, pero ahora tenemos que empezar a bajarlos al formato de 12 horas porque tenemos que mostrarlos.¿porqué? porque es más fácil decir que vas a sumar las 18 horas que identificar antes si es mañana o tarde y después sumarlo; entonces ahora que ya los operamos, podemos calcular los días, las horas que pasaron. Además mientras identificamos el meridiano correspondiente, podemos transformar las horas cómodamente.
Calculamos los días, en base a las 24 horas y luego las horas (como las horas dependen de la misma variable que los días, se los restamos para que nos e repitan)

Ahora empezaremos a trabajar con Strings e integers mezclados, así que ojo.

```python
  dias = hr_plus // 24
  horas = hr_plus - (dias * 24)
    
 if horas == 0:
        horas = '12'
        meridian ='AM'
    elif horas == 12:
        meridian = 'PM'
    elif hr_plus > 12 and  hr_plus <= 23:
        horas = horas -12
        meridian = 'PM'
    else:
        meridian ='AM'
        
```
Por otro lado, debemos considerar los minutos. Para transformarlos a string de salida correspondiente para los números menores a 10 debemos agregarle el 0 al string, ya que el integer por defecto no lo muestra.
Y con esa transformación, o agregación, podemos visualizar algunas cosas.

```python
    minutos = min_plus
    if minutos < 10:
        minutos = '0' + str(minutos)
    # print(f' Pasaron: {dias} dias y {horas} horas - Meridiano Nuevo {meridian}')  
```

Bien tenemos Días, Horas y minutos. ¿Qué nos falta? La variable opcional dle día. Ojo los días son Case sensitive, esto queire decir que no es lo mismo una 'S' que una 's'.
Entonces lo primero que vamos a hacer es preguntar si día viene con algún valor (no hacemos nada si está vacío porque es el valor por defecto.); entonces is hay algún valor, lo pasamos a minúscula con lower() y fijaremos una posición de inicio con el método index, si es que está presente en la lista de los días.
(Recordemos que una de las reglas, si lees el problema original, es que nod ebemos validar el texto ya que se presume que el usuairo ingresará todo correctamente).

Bien, entonces tendremos la palabra y la posición de la palabra. ahora debemos saber, por ejemplo, qué día de salida toca. Es decir, si pasaron 20 días, debemos encontrar el nuevo index del día y definir qué día será.
Para esto vamos a recorrer la lista tantas veces como días tengamos  pero cada vez que recorre la lista, regresaremos al inicio para vovler a recorrerla. En este ejercicio utilizaremos un While (porque hemos usado muchos for en otros)
así que definimos el indice de búsqueda n u el índice de repetición q.

```python
if day != '':
        day = day.lower()
        dia = days.index(day)
        q = 1
        n = dia
        # days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        while q <= dias:
            if n == 6:
                n = 0
            else:
                n = n+1
            q = q+1

        d_name = days[n]
```

Ahora nos queda la última parte, que podríamos integrar al código anterior, pero que por un tema explicativo y demostrativo preferí dejar separado.
Entonces, si es que el día está vacío, mostramos los resultados concatenados (debemos REGRESAR algo en la función) y si no, mostramos integrando los nombres; utilizaremos el método capitalize() para respetar la salida propuesta en los ejemplos

>**capitalize**


```python
   if day == '':
        #respuesta sin días
        if dias == 0:
            new_time = str(horas) + ':' + str(minutos) + ' ' + str(meridian)
        elif dias == 1:
            new_time = str(horas) + ':' + str(minutos) + ' ' + str(meridian) +' (next day)'
        else:
            new_time = str(horas) + ':' + str(minutos) + ' ' + str(meridian) + ' (' + str(dias) + ' days later)'
    else:
        # rptas con días
        if dias == 0:
            new_time = str(horas) + ':' + str(minutos) + ' ' + str(meridian) + ', ' + d_name.capitalize()
        elif dias == 1:
            new_time = str(horas) + ':' + str(minutos) + ' ' + str(meridian) + ', ' + d_name.capitalize() + ' (next day)'
        else:
            new_time = str(horas) + ':' + str(minutos) + ' ' + str(meridian) + ', ' + d_name.capitalize() + ' (' + str(dias) + ' days later)'
```

### CÓDIGO COMPLETO

```python
def add_time(start, duration, day =''):
    # definimos los elementos que vamos a usar
    st_time = start.split()
    dr_time = duration
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Separo la Hora en Partes
    stt_time = st_time[0] # obtengo la Hora
    stt_hour = int(stt_time[:stt_time.index(':')])
    stt_minutes = int(stt_time[stt_time.index(':')+1:])
    stt_cicle = st_time[1].upper()

    # Separo el tiempo de duración
    drt_hour = int(dr_time[:dr_time.index(':')])
    drt_minutes = int(dr_time[dr_time.index(':')+1:])

    # Tiempos Totales en minutos
    min_plus = drt_minutes + stt_minutes
    hr_plus = drt_hour + stt_hour

    # si la hora está entre las las 00.00 AM y las 11.59 AM (siguen igual)
    if(stt_cicle.upper() == 'AM' and stt_hour == 12):
        hr_plus = drt_hour + (min_plus //60)
        min_plus = min_plus % 60

    # si la Hora está entre las 1PM y las 11.59PM Le suma 12 horas
    elif(stt_cicle.upper() == 'PM' and (stt_hour >= 1 and stt_hour <= 11)):
            hr_plus = hr_plus + (min_plus //60) + 12
            min_plus = min_plus % 60
    else:
            hr_plus = hr_plus + (min_plus //60)
            min_plus = min_plus % 60

    #print(f'Hora Original: {stt_time} {stt_cicle}')
    #print(f'Check OP: {hr_plus} hr y {min_plus} min Acumulados')

    dias = hr_plus // 24
    horas = hr_plus - (dias * 24)

    if horas == 0:
        horas = '12'
        meridian ='AM'
    elif horas == 12:
        meridian = 'PM'
    elif hr_plus > 12 and  hr_plus <= 23:
        horas = horas -12
        meridian = 'PM'
    else:
        meridian ='AM'

    minutos = min_plus
    if minutos < 10:
        minutos = '0' + str(minutos)
    # print(f' Pasaron: {dias} dias y {horas} horas - Meridiano Nuevo {meridian}')

    if day != '':
        day = day.lower()
        dia = days.index(day)
        q = 1
        n = dia
        # days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        while q <= dias:
            if n == 6:
                n = 0
            else:
                n = n+1
            q = q+1

        d_name = days[n]

    if day == '':
        #respuesta sin días
        if dias == 0:
            new_time = str(horas) + ':' + str(minutos) + ' ' + str(meridian)
        elif dias == 1:
            new_time = str(horas) + ':' + str(minutos) + ' ' + str(meridian) +' (next day)'
        else:
            new_time = str(horas) + ':' + str(minutos) + ' ' + str(meridian) + ' (' + str(dias) + ' days later)'
    else:
        # rptas con días
        if dias == 0:
            new_time = str(horas) + ':' + str(minutos) + ' ' + str(meridian) + ', ' + d_name.capitalize()
        elif dias == 1:
            new_time = str(horas) + ':' + str(minutos) + ' ' + str(meridian) + ', ' + d_name.capitalize() + ' (next day)'
        else:
            new_time = str(horas) + ':' + str(minutos) + ' ' + str(meridian) + ', ' + d_name.capitalize() + ' (' + str(dias) + ' days later)'

    return new_time
```

