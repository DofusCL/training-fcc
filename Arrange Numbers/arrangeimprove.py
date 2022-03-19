# versión Perfeccionada
def arithmetic_arranger(problem, bol= False):
    ln_uno = ''
    ln_dos = ''
    separador = ''
    resultado = ''
    # Regla 01 Máximo 5 opciones
    if len(problem) > 5:
        #print('Demasiadas Operaciones a Ejecutar')
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

            # definimos qué vamos a devolver
            ln_uno = ln_uno + str(top_op).rjust(lenmax+1)
            ln_dos = ln_dos + sign + str(bot_op).rjust(lenmax)
            separador = separador + lines

            # Realizamos la operación
            if bol is not False:
                if sign == '+':
                    sum_op = int(top_op) + int(bot_op)
                else:
                    sum_op = int(top_op) - int(bot_op)
            else:
                sum_op = 0
            resultado = resultado + str(sum_op).rjust(lenmax+1)

            if len(problem) > 1:
                ln_uno = ln_uno + '    '
                ln_dos = ln_dos + '    '
                separador = separador + '    '
                resultado = resultado + '    '

            if bol is not False:
                # arranged_problems = linea_uno + linea_dos + linea_tres + linea_cuatro
                arranged_problems = ln_uno.rstrip() + '\n' + ln_dos.rstrip() + '\n' + separador.rstrip() + '\n' + resultado.rstrip()
                # print(ln_uno + '\n' + ln_dos + '\n' + separador + '\n' + resultado)
            else:
                arranged_problems = ln_uno.rstrip() + '\n' + ln_dos.rstrip() + '\n' + separador.rstrip()
                # print(ln_uno + '\n' + ln_dos + '\n' + separador)
    return arranged_problems


# Debemos resolver pensando en primero con el True
r = arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'], True)
