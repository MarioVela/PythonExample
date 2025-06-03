# codigo de seguridad
nombre = input('Nombre completo del usuario: ')
apellido_p = input('Apellido paterno del usuario: ')
apellido_m = input('Apellido materno del usuario: ')
curp = input('Ingrese su CURP: ')
año = input('Año que ingreso a la empresa: ')
ape_mat = (f'{apellido_m[:3]}')
print(f'Su codigo de seguridad es: {nombre[2]}{apellido_p[-1]}{ape_mat[::-1]}{curp[-6:]}{nombre[0:8:2]}{año[-2:]}')