from operator import truediv

empleado = "Mario Velázquez"
edad = "38"
salario = "20000"
edificio = "C"
activo = True

# PASO 6 IMPRESION DE TODA LA INFORMACION

# PASO 1 DATOS DEL TRABAJADOR
print ("Nombre del Empleado:",(empleado))
print ("Edad:", (edad), "años")
print ("Salario Mensual:",(salario)," MXN")
print ("Edificio Asignado:",(edificio))
print ("Trabajador Activo:",(activo))
print ("____________________")

# PASO 2 TIPOS DE DATOS INGRESADOS
print (type(empleado))
print (type(edad))
print (type(salario))
print (type(edificio))
print (type(activo))
print ("___________________")

#PASO 3 DATOS CONVERSION DE TIPO DE DATOS
empleado = "Mario Alberto Velázquez Sánchez"
edad = (int(edad))
salario = int(salario)
edad = int (edad)
salario = int(salario)
edificio = ord (edificio)
activo = int (activo)


print ("Nombre del Empleado:",(empleado))
print ("Edad:", (edad), "años")
print ("Salario Mensual:",(salario)," MXN")
print ("Edificio Asignado:",(edificio), "ASCII")
print ("Trabajador Activo:",(activo))
print ("_______________________")

# PASO 4 TIPOS DE DATOS CONVERTIDOS
print (type(empleado))
print (type(edad))
print (type(salario))
print (type(edificio))
print (type(activo))
print ("_______________________")

# PASO 5 ASCII DEL EDIFICIO
print ("Edificio Asignado:",(edificio), "ASCII")


