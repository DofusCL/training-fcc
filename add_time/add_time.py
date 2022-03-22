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

# Caso que cumple la mayoría de las entradas
add_time("11:40 AM", "0:25")
# Returns: 12:05 PM

'''
Monday – MUN – day.
Tuesday – TUEZ – day.
Wednesday – WENZ – day.
Thursday – THURZ – day.
Friday – FRY – day.
Saturday – SAH-DER-day.
Sunday – SUN – day.
'''


