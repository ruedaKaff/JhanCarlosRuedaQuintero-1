""" 9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad. """
import datetime
x = datetime.datetime.now()
xyears =x.year

nombre= input('Cual es tu nombre ? :')

telefono= input('ingresa tu telefono :')

añoIngreso= int(input('Año de ingreso a la empresa :'))

apellidos= input('Cual es tu apellido :')

edad= input('Cual es tu edad? :')

añosAntiguedad = (xyears - añoIngreso )
print (f"Tu nombre es: {nombre} {apellidos} y tiene {añosAntiguedad} ")

