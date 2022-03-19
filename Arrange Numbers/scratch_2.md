# Solving Arithmetic Arrenge
###Por Nicolás Bosoni Spinetto - Pycharm 3.2
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
> Este cuaderno NO ESTÁ pensado para ser ejecutado por bloques, la idea es que puedas leer y copiar el código paso a paso para que entiendas qué sucede y cómo se pensó en resolver el ejercicio. SI tratas de ir ejecutando cada código de forma separada probablemente tengas muchos errores.

> Al final del cuaderno he dejaré la totalidad del código y además en un py aparte.


En primer lugar debemos llevar una lista de strings a un formato reconocible por todos los niños que hagan una operación matemática es decir, mostrar como tabla una operación de suma o resta.

###Definición de la Función
1 - Identificamos que el arreglo puede tener dos formas una que nos entrega el resultado de forma automática y otra que nos entrega sólo la lista.
```python
r = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
r = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
```

Esto podemos resolverlo de forma sencilla, ya que una función, al recibir parámetros también puede definir valores por defecto. Entonces podemos pensar que si el parámetro no está definido por defecto sea FALSE para evitar que se caiga nuestro código. Entonces pasamos los dos parámetros como atributos de la función bajo el concepto de 'problem' (la lsita) y el valor booleano ('True')

Código:
```python
def arithmetic_arranger(problem, bol = False):
    #
   return some_var
```
### Reglas
2 - El problema presenta algunas reglas que copiaremos y resolveremos de forma práctica una a una afectando el funcionamiento de nuestro script
```markdown
Situaciones que pueden causar Errore:

A - Si hay demasiadas operaciones la función colapsará. Sólo se permiten 5 operaciones por lista; caso de error: "Demasiadas Operaciones a Ejecutar".

B - No se consideran otras operaciones distintas de la Suma y la Resta, si existe alguna operación relativa a la multiplicación o división, deberá indicar el caso de erro: "Sólo se permiten '+' o '-'

C - Cada numero puede contener sólo dígitos. De otra forma debe agregar el caso de error: Los números sólo pueden contener dígitos.

D - Cada número puede tener máximo 4 dígitos, esto quiere decir que el caso de error es el siguiente: 'Número no pueden tener más de 4 dígitos'.
```
####Regla A
Lo que vamos a hacer es preguntar inmediatamente al ingreso si el largo de la lista que recibimos tiene más de 5 objetos. Las listas son elementos iterables y podemos utilizar algunos métodos built in function (o propios de librerías) que se aplican a las mismas.
> **LEN()** Este método devuelve la longitud de un objeto, ya sea una lista, una cadena, una tupla o un diccionario. len() toma un argumento, que puede ser una secuencia (como una cadena, bytes, tupla, lista o rango) o colección (como un diccionario, conjunto o conjunto "set" congelado "set frozen").

Al igual que en otros lenguajes de programación utilizaremos los métodos condicionales if..else

Código:
```python
def arithmetic_arranger(problem, bol = False):
    # Regla 01 Máximo 5 opciones
    if len(problem) >= 5:
        print('Demasiadas Operaciones a Ejecutar')
    else:
        print('Code Here....')
```
####Regla B, C y D
Es importante leer bien las reglas antes de continuar ya que se hará más difícil separar, porque no son sólo parte de cada uno de los elementos que están conformando la lista si no que van un poco de la mano en los momentos que serán evaluadas.

>**¿Porqué vamos a preparar primero la regla C?**
> 
>Un poco por la lógica de los elementos, es decir si no son numéricos, no tiene sentido que busque si tiene 4 dígitos o si hay una multiplicación o división, o que pueda operar una suma; un poco es el orden jerárquico de las prioridades que vamos a evaluar.

Para la regla C debemos comparar si los dígitos son numéricos, es decir no deben haber síbolos ni caracteres en los operadores de arriba ni de abajo.
Para esto vamos a separar la cadena en 3 partes, un operador top, un operador bot, signos y también reservaremos un string para la suma en algunos pasos más.

Necesitamos ingresar a cada uno de los elementos que queremos resolver y poder iterarlos. Para esto podemos utilizar un loop o el conocido FOR

> FOR element IN range: EL Loop For nos permite iterar o recorrer elementos como listas, tuplas, diccionarios, series, arreglos..etc... donde "element" son los objetos que quiero recorrer y "range" corresponde al rango o iterable que contiene los elementos

Agregamos a la ejecución entonces el código y lo vamos a ejecutar para entender qué sucede. Vamos a observar cómo se genera la lectura "Por Cada STR conetenido en PROBLEM ejecuta lo siguiente: Muestra el Elemento STR"

Código:
```python
def arithmetic_arranger(problem, bol= False):
    # Regla 01 Máximo 5 opciones
    if len(problem) >= 5:
        print('Demasiadas Operaciones a Ejecutar')
    else:
        # Entramos ya a analizar los elementos dentro de la lista
         for str in problem:
             print(str)


# Debemos lidear primero con el True
r = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
```
Resultado:
```doctest
32 + 698
3801 - 2
45 + 43
123 + 49

Process finished with exit code 0
```
Hemos accedido entonces a los objetos/elementos que están contenidos en la lista y que son el problema que debemos resolver. Ahora tenemos que separarlos para poder trabajar con cada uno. Note que cada STR tiene 3 partes y cada una separada con un espacio.

Aquí podemos jugar de dos formas, la sensilla que es accediendo a la posición de cada substring o bien una más avanzada manejando el método index y la posición de las listas. Sin hacer mucha introducción, el método SPLIT() separa un objeto por defecto según el caracter "espacio" o por uno que especifique.

Comentamos el print anterior. Denominamos una lista que reciba los datos separados por cada iteración del string, aplicamos el método split() al string y mostramos la nueva lista.

Código:
```python
         for str in problem:
             # print(str)
             # separamos el str en substrings método: simple
            lst = str.split()
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
A diferencia del código anterior podemos ver claramente que los objetos fueron separados correctamente. Sin embargo debemos agruparlos en las variables correspondientes.
Un dato importante es que puedes asignar los elementos por su posición (En este caso 0, 1, 2  o si lo vez en reversa -1, 0 1). Esto nos puede facilitar el hecho de no tener que hacer un i iterable cuando son pocos objetos.
```doctest
        ['32', '+', '698']
    top_op,    sign,   bot_op
 Posición 0, posición 1, posición 2 o -1
```
Entendiendo esta pequeña conceptualización posicional de los iterables, ahora podemos asignar siempre siguiendo el método simplificado de asignación. Ahora <span style="color:red">**OJO**</span> miren lo que sucede al imprimir las variables de formas separadas y unidas. Podrán notar que el cambio es importante y ya da a pensar luego en cómo se podrían empezar a pensar maneras de mostrar resultados.

Código:

<table>
<tr>
<th>Vertical</th>
<th>Horizontal</th>
</tr>
<tr>
<td>

```python
# Entramos ya a analizar los elementos dentro de la lista
         for str in problem:
             # print(str)
             # separamos el str en substrings método: simple
            lst = str.split()
            # print(lst)
            x = lst[0] # top_op
            y = lst[1] # sign
            z = lst[-1] # bot_op
            print(x)
            print(y)
            print(z)
```

</td>
<td>

```python
        # Entramos ya a analizar los elementos dentro de la lista
         for str in problem:
             # print(str)
             # separamos el str en substrings método: simple
            lst = str.split()
            # print(lst)
            x = lst[0] # top_op
            y = lst[1] # sign
            z = lst[-1] # bot_op
            print(x,y,z)
```

</td>
</tr>
</table>

Te dejo además la forma Avanzada para la captura de datos que se hace entendiendo el método index y el posicionamiento dentro de las listas. Simplemente para que aprendas a usarlas mejor. De igual forma utilizaremos  X, Y, Z o el equivalente top_op, sign, bot_op

Códgo: ( -- Volveremos en unos pasos para hacer un pequeño cambio -- )
```python
for str in problem:
             # print(str)
             # separamos el str en substrings método: simple
            lst = str.split()
            # print(lst)
            top_op = str[:str.index(' ')]
            bot_op = str[str.index(' ')+3:]
            sign = str.find("+")
            if sign == - 1 : sign = '-'
            else: sign = '+'
            print(top_op,sign,bot_op)
```
Bien entonces ahora lo que toca verificar si cada uno de los caracteres del código es numerico.
> **isnumeric()**: Permite revisar todos los caracteres de un string y evulúa si son numéricos o no. Si TODOS son numéricos devolverá VERDADERO si hay uno que no lo sea, devolverá FALSO

> **AND, OR, NOT**: Operadores Lógicos comparativos, se usan para combinar estados condicionales.

Código:
```python
            # comparamos si es numérico
            if not top_op.isnumeric() or not bot_op.isnumeric():
                print('Sólo se puede operar cuando hay números')
```
Nos quedan dos comprobaciones, y una de ella la realizaremos modificando código anterior, esto es porque para efectos exploratorios del paso a paso, no quise hacer todos los cambios de súbito. Este paso tiene relación con el cambio de signos y nos hace retroceder donde dejamos la marca entre paréntesis que indica que debíamos regresar a hacer unas modificaciones. Nootros nos apoyaremos en IN o NOT IN depende de cómo queramos preguntar. Al decir "Cómo quiero preguntar", nos referimos a cómo será evaluado, es decir la pregunta de nuestra cabeza pasa a código. En este caso particular podríamos preguntar si los operadores que no corresponden se encuentran en la lista (Es decir si / y * están presentes) 
Código:
<table>
<tr>
<th>ANTES</th>
<th>CON EL CAMBIO</th>
</tr>
<tr>
<td>

```python

            sign = str.find("+")
            if sign == - 1 : sign = '-'
            else: sign = '+'
            # print(top_op,sign,bot_op)

            # comparamos si es numérico
            if not top_op.isnumeric() or not bot_op.isnumeric():
                print('Sólo se puede operar cuando hay números')
```

</td>
<td>

```python
            sign = str.find("+")
            if sign == - 1 :
                if '/' in str or '*' in str:
                    print('Sólo se permite operaciones de + o -')
                else:
                    sign = '-'
            else:
                sign = '+'
            # print(top_op,sign,bot_op)

            # comparamos si es numérico
            if not top_op.isnumeric() or not bot_op.isnumeric():
                print('Sólo se puede operar cuando hay números')
```

</td>
</tr>
</table>

¿Crees que puedes hacerlo con find()? Inténtalo.

