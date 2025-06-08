calificaciones = [6, 7, 9, 8, 5, 10, 7, 6, 9, 8]
print (f'la lista de califaciones es: {calificaciones}')
calificaciones.sort()
min = calificaciones [0]
max = calificaciones[-1]
print (f'La calificacion mas alta es: {max}')
print (f'La calificacion mas baja es: {min}')
veces9 = (calificaciones.count(9))
print(f'La calificacion 9 se repite: {veces9} veces')
print(calificaciones [2:-3])
calificaciones.clear()
print(f'las lista es: {calificaciones}')


