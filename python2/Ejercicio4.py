nombres = ["Carlos", "Alberto", "Lucía", "Fernanda"]
apellidos = ["Ramírez", "Torres", "Hernández", "López"]
clave_escuela = ["MZ1234S2", "KX5566T1", "HY0912G3", "RA8407M0"]
nom1 = nombres[0]
ape1 = apellidos[0]
clave1 = clave_escuela[0]
nom2 = nombres[1]
ape2 = apellidos[1]
clave2 = clave_escuela[1]
nom3 = nombres[2]
ape3 = apellidos[2]
clave3 = clave_escuela[2]
nom4 = nombres[3]
ape4 = apellidos[3]
clave4 = clave_escuela[3]

# Ejercicio estudiante 1
nom1m = nom1[0]
ape1 = ape1[::-1]
nc1 = (f'{nom1}{ape1}')
nom1c = len(nc1)
clave_m1 = clave1[-2]
codigo1 = (f'{nom1m.upper()}{ape1[:2]}{clave1[:3]}{(nom1c)}{clave_m1.upper()}')
print (f' El codigo generico escolar de {nombres[0]} '
f'{apellidos[0]} {clave_escuela[0]} es: {codigo1}')

# Ejercicio estudiante 2
nom2m = nom2[0]
ape2 = ape2[::-1]
nc2 = (f'{nom2}{ape2}')
nom2c = len(nc2)
clave_m2 = clave2[-2]
codigo2 = (f'{nom2m.upper()}{ape2[:2]}{clave2[:3]}{(nom2c)}{clave_m2.upper()}')
print (f' El codigo generico escolar de {nombres[1]} '
f'{apellidos[1]} {clave_escuela[1]} es: {codigo2}')

# Ejercicio estudiante 3
nom3m = nom3[0]
ape3 = ape3[::-1]
nc3 = (f'{nom3}{ape3}')
nom3c = len(nc3)
clave_m3 = clave3[-2]
codigo3 = (f'{nom3m.upper()}{ape3[:2]}{clave3[:3]}{(nom3c)}{clave_m3.upper()}')
print (f' El codigo generico escolar de {nombres[2]} '
f'{apellidos[2]} {clave_escuela[2]} es: {codigo3}')

# Ejercicio estudiante 4
nom4m = nom4[0]
ape4 = ape4[::-1]
nc4 = (f'{nom4}{ape4}')
nom4c = len(nc4)
clave_m4 = clave4[-2]
codigo4 = (f'{nom4m.upper()}{ape4[:2]}{clave4[:3]}{(nom4c)}{clave_m4.upper()}')
print (f' El codigo generico escolar de {nombres[3]} '
f'{apellidos[3]} {clave_escuela[3]} es: {codigo4}')