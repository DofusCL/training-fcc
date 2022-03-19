# Solving Arithmetic Arranger
### Por Nicolás Bosoni Spinetto - Pycharm 3.2
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

    
> Este cuaderno NO ESTÁ pensado para ser ejecutado por bloques, la idea es que puedas leer y desarrollar código paso a paso para que entiendas qué sucede y cómo se pensó en resolver el ejercicio. SI tratas de ir ejecutando cada código de forma separada probablemente tengas muchos errores.

**Reglas de Lectura:**

Primero debes leer con atención el problema original el cual he extendido en la parte superior para que puedas comprenderlo. Está en inglés, por lo tanto te recomiendo que lo leas detenidamente y entiendas muy bien cada una de las partes, ya que la mala interpretación puede llevar a tomar caminos erróneos en el proceso (me pasó por no leer completo 2 veces) y eso hace perder tiempo eficiencia para resolver los desafíos. Otra sugerencia importante es fijarse en las salidas; si esta indica un "punto final" al terminar el mensaje de salida, debes ponerlo o el template/pattern del sistema al que debes subir tu solución, no lo permitirá y arrojará errores. Debes entender muy bien la diferencia entre el statement PRINT y RETURN, no haré hincapié en ello, pero sugiero que leas y veas código o youtube para que te acostumbres y no llenes de breaks cosas por ahí pensando en que va a saltar algo fuera de la consola.

**Problema**

Se pide, dada una lista de problemas matemáticos de sumas y restas, reagrupar su formato al mismo que resuelven los niños en las escuelas.
```doctest
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```
La estructura qeu debemos resolver es la siguiente: (la notación del TRUE indica que se debe mostrar además la respuesta calulada)
```python
r = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
r = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
```

**Resumen de las reglas del Problema**

```
A - Se deben respetar los Mensajes de Eror que se piden en el Link original al pie de la letra Y EN INGLEÉS

B- Si hay demasiadas operaciones la función colapsará. Sólo se permiten 5 operaciones por lista; caso de error: "Demasiadas Operaciones a Ejecutar".

C - No se consideran otras operaciones distintas de la Suma y la Resta, si existe alguna operación relativa a la multiplicación o división, deberá indicar el caso de erroR: "Sólo se permiten '+' o '-'

D - Cada numero puede contener sólo dígitos. De otra forma debe agregar el caso de error: Los números sólo pueden contener dígitos.

E - Cada número puede tener máximo 4 dígitos, esto quiere decir que el caso de error es el siguiente: 'Número no pueden tener más de 4 dígitos'.

F - La salida debe tener 4 espacios entre operaciones, y sólo 1 espacio entre el signo y el operador de la segunda línea
```

**Análisis Previo**

- Sabemos mirando lo anterior que tenemos una función, y por lo tanto debe retornar algo.
- Entendemos que la función puede recibir dos parámetros pudiendoe star defindio o no, por lo tanto debemos resolver al recibir los parámetros
- Los elementos que componen la lista son strings y para poder operarlos tendremos que separarlos
- Observando la salida modelo ya entendemos que son 4 líneas las que necesitamos regresar
- Definidas esas 4 líneas de resultado debemos entender cómo unificarlas para regresar un único resultado al resto del programa.
- Sería bueno definir en qué orden se resolverán las reglas o apuntarlas en un esquema para ir desarrollando el código fácilmente.
- Recuerda ir ejecutando algunos prints, ya que este problema está diseñado para subirse a una plataforma específica y no necesariamente mostrará algo en tu Framework

## PARTE 1

**Definimos la Función**

Iremos modificando algunas cosas en el código a medida que avanzamos. En este caso lo que haremos será definir la función para recibir los parámetros de cualquiera de los dos métodos propuestos en el problema. La primera recibirá el parámetro dado por defecto que es una lista de problemas o de operaciones aritmeticas y la otra el valor booleaano (que puede ser True or False) y que inidca si debe mostrar el resultado. Tanto el nombre de la función como el de la variable final están dados en la documentación del problema, debemos respetarlos.
```python
def arithmetic_arranger(problem, bol = False):
    # some code...
   return arranged_problems
```

**Encabezados de Salida**

Como lo mencionamos en el análisis previo, evidentemente tendremos que definir alguna salida, y ya sabemos que a lo menos tendremos un operador superior, un signo, un operador inferior, una línea separadora y una operación matemática (puede ser suma o resta). Nosotros las definiremos de la siguiente manera:
```python
def arithmetic_arranger(problem, bol= False):
    ln_uno = ''
    ln_dos = ''
    separador = ''
    resultado = ''
    
    return arranged_problems
```
Noten que el código se irá extendiendo hacia abajo e iremos mostrando o partes o trozos completos, así que es importante que puedan en una seunda pantalla organizar su propio código, ya que esto es TODO lo que aprendí en 2 días de estudio y uno de resolución. (Puede que no sea lo más rápido, pero para mie stá bien)

**Resolviendo Regla 01**

La primera regla que vamos a resolver es la que determina básicamente si sigue o no el ejercicio. El sistema está diseñado para soportar máximo 5 problemas, si hay más se va a 'caer' el sistema y arrojará un eror de ejecución, para evitar que esto pase debemos controlarlo. Al igual que en otros lenguajes, utilizaremos los controladores de flujo IF..ELSE para aplicar la lógica a la regla. Depende de cómo "hagamos la pregunta" va a resultar el IF. Siempre se recomienda lo más corto en el IF y las extenciones de código en el ELSE (salvo que trabajemos sólo con llamadas a métodos, clases y funciones). A continuación de los encabezados que definimos, aplicamos nuestra sentencia condicional
```python
# Regla 01 Máximo 5 opciones
    if len(problem) > 5:
        # print('Demasiadas Operaciones a Ejecutar')
        # print("Error: Too many problems.")
        return 'Error: Too many problems.'
    else:
        # Entramos ya a analizar los elementos dentro de la lista
```
Como mencioné anteriormente se trata del call de una función y por lo tantos se espera que regrese un objeto, en este caso no que imprima por pantalla, si no que refrese algo. En ese sentido no podemos entregar un print como resultado, ya que la aplicación no gestionará el resto de "testing" que debe hacer, por otro los textos deben ir en inglés; entonces para comprobar que etamos avanzando iremos agregando algunos prints y luego al desarrollar los comentaremos. Dejaré prints en español e inglés por si genera confusión. El return de esta función se comparará con el template de la aplicación y eso permite verificar que está correcto.

Así se ve la suma del código hasta ahora: Recuerda la indentación es importante (la sangría) ya que determina a qué trozo de código pertenece cada cosa. Y hace que sea más simple entender dónde se definen las variables y las reglas.

> **LEN()** Este método devuelve la longitud de un objeto, ya sea una lista, una cadena, una tupla o un diccionario. len() toma un argumento, que puede ser una secuencia (como una cadena, bytes, tupla, lista o rango) o colección (como un diccionario, conjunto o conjunto "set" congelado "set frozen").

```python
def arithmetic_arranger(problem, bol= False):
    ln_uno = ''
    ln_dos = ''
    separador = ''
    resultado = ''
    
    # Regla 01 Máximo 5 opciones
    if len(problem) > 5:
        # print('Demasiadas Operaciones a Ejecutar')
        # print("Error: Too many problems.")
        return 'Error: Too many problems.'
    else:
        # Entramos ya a analizar los elementos dentro de la lista
        
    return arranged_problems
```

**Recorrer la Lista**

Una vez que determinamos la cantidad de problemaas, debemos recorrer la lista para poder empezara  analizar los elementos. La lista es un elemento iterable y para poder revisar su contenido necesitamos alguna función o método que nos permita ir revisando paso a paso cada uno de los problemas que se definen en ella. Para esto existe el FOR:

> FOR element IN range: EL Loop For nos permite iterar o recorrer elementos como listas, tuplas, diccionarios, series, arreglos..etc... donde "element" son los objetos que quiero recorrer y "range" corresponde al rango o iterable que contiene los elementos

Entonces haremos la lectura del for aplicado a nuestro caso: "Por cada OPERACIÓN contenida en PROBLEMA muéstrame la OPERACIÓN:" y esto se vería algo así, recuerda una vez chequeamos el print, lo comentamos para no repetir salidas innecesarias.

```python
    if len(problem) > 5:
        # print('Demasiadas Operaciones a Ejecutar')
        # print("Error: Too many problems.")
        return 'Error: Too many problems.'
    else:
        # Entramos ya a analizar los elementos dentro de la lista
         for oper in problem:
            # print(oper)
```
Si ejecutamos el print nos va a mostrar lo siguiente:
```doctest
32 + 698
3801 - 2
45 + 43
123 + 49

Process finished with exit code 0
```

**Separar los elementos de la Lista**

A continuación tenemos dos formas de separar los elementos, la primera y la forma simple accediendo al índice del objeto y rescatando su contenido, y la otra más avanzada es ententiendo el posicionamiento dentro de las listas. Mostraré la forma fácil y luego continuaré con la más avanzada; sugiero revisar el método split()

Código: **FORMA FÁICL**

```python
         for oper in problem:
             # print(oper)
             # separamos el str en substrings método: simple
            lst = oper.split()
            print(lst)
```
Resultado:
```doctest
['32', '+', '698']
['3801', '-', '2']
['45', '+', '43']
['123', '+', '49']

Process finished with exit code 0
```

**Asignando las Variables**
¿Recuerdas que ya habíamos definido unas variables al principio para la salida? Bien aquí comenzaremos a trabajar previo a transformar esas variables. En el paso anterior sólo dividimos la lista. Ese paso no es obligatorio si usas el método más avanzado de asignación. Entendamos cómo funciona la asignación primero para el paso simple. Y tu luego investigas por tu cuenta el movimiento o **desplazamiento dentro de la lista** para el avanzado.

Para que se entienda revisemos uno de los problemas que resultaron y cómo es que lo vamos a descomponer, este código es netamente conceptual: Top_op será el operador de arriba, luego viene sign que es el signo de la operación, y finalmente bot_op que es el operador de abajo y que **se acompaña** por el signo. Estos responden a 3 posiciones según el largo de la lista
```doctest
        ['32', '+', '698']
    top_op,    sign,   bot_op
 Posición 0, posición 1, posición 2 o -1[en reversa]
```
Entonces, asignamos y revisamos las salidas. ¿Qué es lo que observas? Luego de revisar qué pasa con los prints, comentalos y descomenta el último, ¿Notas una Diferencia?

```python
# Entramos ya a analizar los elementos dentro de la lista
         for oper in problem:
             # print(oper)
             # separamos el str en substrings método: simple
            lst = oper.split()
            # print(lst)
            x = lst[0] # top_op
            y = lst[1] # sign
            z = lst[-1] # bot_op
            print(x)
            print(y)
            print(z)
            #print(x,y,z)
```

**Resolviendo Regla 2 y Aplicando Forma Avanzada**

Bien en este paso resolveremos la regla para cuando el problema contiene una división o multiplicación que no están permitidas. Si estás usando la forma SIMPLE deberás entender cómo adaptar tu código para que se ajuste a la sentencia lógica y puedas hacer correctamente la comparación.
Aplicando la asignación de forma avanzada (desplazamiento en la lista) podemos inmediatamente jugar con los signos. **RECUERDA** estamos en medio de iteraciones por lo que se evalúa elemento a elemento.

> **FIND()** devuelve el índice más bajo en el que se encuentre el substring sub en el bloque str[start:end]. Si el substring sub no se encuentra, devuelve el valor -1. Si no se especifican los argumentos start o end, se toman como valores por defecto el comienzo y el final del string

Revisa la documentación sobre los operadores: https://www.w3schools.com/python/python_operators.asp

```python
 for oper in problem:
            # print(oper)
            
            # separamos el str en substrings método:
            top_op = oper[:oper.index(' ')]
            bot_op = oper[oper.index(' ')+3:]

            # dentro de la misma separación
            # Regla 02 Sólo Sumas y Restas
            sign = oper.find("+")
            if sign == - 1 :
                if '/' in oper or '*' in oper:
                    # print('Sólo se permite operaciones de + o -.')
                    # print("Error: operator must be '+' or '-'.")
                    return 'Error: Operator must be '+' or '-'.'
                else:
                    sign = '-'
            else:
                sign = '+'
            #print(top_op,sign,bot_op) # ChecK
```
Recuerda comentar y descomentar los prints mientras descubres y solucionas posibles errores en el código, recuerda aquí lo estamos particionando y poco a poco irems mostrarndo uno más completo.

**Resolver la Tercera y la Cuarta Regla**
Ya entendemos un poco de lógica y de condicionales, seguramente revisaste el link que te mostré de los operadores y te abrás percatado que existen de diferentes tipos, pero finalmente todos básicos y responden a un uso similar. Para revisar que cada uno de los caracteres de nuestro problema sea numerico, revisaremos la descomposición que hicimos y lo compararemos con el método isnumeric(). Luego para la regla 4 que debemos comparar que sean sólo 4 elementos y no más, utilizamos LEN() para comprobar que si el largo de la lista principal es mayor a 4, es decir, existan 5 o más problemas a resolver nos entregue el mensaje de error.

> **ISNUMERIC()**: Permite revisar todos los caracteres de un string y evulúa si son numéricos o no. Si TODOS son numéricos devolverá VERDADERO si hay uno que no lo sea, devolverá FALSO

> **AND, OR, NOT**: Operadores Lógicos comparativos, se usan para combinar estados condicionales.

Código:
```python
            # Regla 03 Deben ser numéricos
            if not top_op.isnumeric() or not bot_op.isnumeric():
                # print('Sólo se puede operar cuando hay números')
                # print('Error: Numbers must only contain digits.')
                return 'Error: Numbers must only contain digits.'

            # Regla 04 Comparamos si los números sin 4 wn cada etapa
            if len(top_op) > 4 or len(bot_op) > 4:
                # print('Error: Sólo se pueden calcular números de 4 dígitos')
                # print('Error: Numbers cannot be more than four digits')
                return 'Error: Numbers cannot be more than four digits.'
```

**Definiendo el máximo de líneas o rayas**

Parece algo simple pero es parte del código es importante notar que el TOP_OP se muestra solo, y que BOT_OP se muestra junto al signo, por lo tanto tiene un caracter más. Entonces para las líneas punteadas debemos determinar qué número es más grande. El código es un poco más largo porque está hecho de forma descriptiva, porque lo que se busca destacar es que al largo inicialmente se le suma 1 línea más por el signo y luego 1 línea adicional por el espacio obligatorio que se define en las reglas del problema.

```python
            # ancho de cada underline
            lenmax = max(len(top_op), len(bot_op))
            lenmax += 1
            lines = '-' * (lenmax+1)
            # lenmax = str(lenmax)
```

CÓDIGO COMPLETO HASTA PARTE 1:
```python
def arithmetic_arranger(problem, bol= False):
    ln_uno = ''
    ln_dos = ''
    separador = ''
    resultado = ''
    # Regla 01 Máximo 5 opciones
    if len(problem) > 5:
        # print('Demasiadas Operaciones a Ejecutar')
        # print("Error: Too many problems.")
        return 'Error: Too many problems.'
    else:
        # Entramos ya a analizar los elementos dentro de la lista
         for oper in problem:
            # print(oper)

            # separamos el str en substrings método:
            lst = oper.split()
            # print(lst)
            top_op = oper[:oper.index(' ')]
            bot_op = oper[oper.index(' ')+3:]

            # dentro de la misma separación
            # Regla 02 Sólo Sumas y Restas
            sign = oper.find("+")
            if sign == - 1 :
                if '/' in oper or '*' in oper:
                    # print('Sólo se permite operaciones de + o -.')
                    # print("Error: operator must be '+' or '-'.")
                    return 'Error: Operator must be '+' or '-'.'
                else:
                    sign = '-'
            else:
                sign = '+'
            #print(top_op,sign,bot_op) # Chekc Ok

            # Regla 03 Deben ser numéricos
            if not top_op.isnumeric() or not bot_op.isnumeric():
                # print('Sólo se puede operar cuando hay números')
                # print('Error: Numbers must only contain digits.')
                return 'Error: Numbers must only contain digits.'

            # Regla 04 Comparamos si los números sin 4 wn cada etapa
            if len(top_op) > 4 or len(bot_op) > 4:
                # print('Error: Sólo se pueden calcular números de 4 dígitos')
                # print('Error: Numbers cannot be more than four digits')
                return 'Error: Numbers cannot be more than four digits.'

            # ancho de cada underline
            lenmax = max(len(top_op), len(bot_op))
            lenmax += 1
            lines = '-' * (lenmax+1)
            # lenmax = str(lenmax)
            
            # Aquí viene más código.....
    return arranged_problems
```

## PARTE 2
En un par de horas más....

