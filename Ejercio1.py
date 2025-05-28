# Codigo unico del alumno:

alumno = input("nombre del alumno: ")
apellido_p = input("apellido paterno: ")
apellido_m = input("apellido materno: ")
clave = input("clave del escolar: ")
clave2 =(f'{clave[:4]}')

print (f'{alumno[1]}{apellido_m[-1]}{clave2[::-1]}{alumno[::2]}{clave[-2:]}')