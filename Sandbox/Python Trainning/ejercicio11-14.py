
""" 1. Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, por tal razón, ha solicitado el diseño de
un programa que cuente con el siguiente menú como panel de
control: """

""" 1.CREAR GRUPO ARTEMIS:
    1.1 LISTAR CAMPERS DE ARTEMIS
    1.2 AGREGAR CAMPERS A ARTEMIS 
    1.3 ELIMINAR CAMPERS DE ARTEMIS
    1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS
    1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS

    2. CREAR GRUPO SPUTNIK:
    2.1 LISTAR CAMPERS DE SPUTNIK
    2.2 AGREGAR CAMPERS A SPUTNKIK
    2.3 ELIMINAR CAMPERS DE SPUTNIK
    2.4 ORDENAR ALFABETICAMENTE EN SPUTNIK
    2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK
    3. SALIR
    DIGITE OPCION: 
 """
nombre = ""
sputnik=[]
opc = 0
while opc !=3:
    print ('------------------------------\n')
    print(f'1.CREAR GRUPO ARTEMIS:\n 1.1 LISTAR CAMPERS DE ARTEMIS\n 1.2 AGREGAR CAMPERS A ARTEMIS \n 1.3 ELIMINAR CAMPERS DE ARTEMIS \n 1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS \n 1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS')
    print(f'\t2.CREAR GRUPO SPUTNIK:\n\t2.1 LISTAR CAMPERS DE SPUTNIK\n\t2.2 AGREGAR CAMPERS A SPUTNKIK\n\t2.4 ORDENAR ALFABETICAMENTE EN SPUTNIK\n\t2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK\n\t3.SALIR \n\t\tDIGITE UNA OPCION:')
 
    opc = float(input())
    if opc == 1:
        print ('------------------------------\n')
        print(f'Sputnik: {sputnik}\n')
    elif opc == 1.1:
        print ('\n------------------------------\nLISTA DE ESTUDIANTES ARTEMIS:')
        for i in sputnik: 
            print(f'* {i}')
    
    elif opc == 1.2:
        print ('------------------------------\n')
        nombre = input('Ingrese nombre completo del camper:')
        sputnik.insert(0,nombre)
        print(f'{nombre}+')
        
    elif opc == 1.3:
        print ('------------------------------\n')
        nombre = input('Ingrese el nombre a eliminar:')
        x= sputnik.index(nombre)    
        del sputnik[x]
        print(f'{nombre}-')

    elif opc ==1.4:
        print ('------------------------------\n')
        sputnik.sort()
        print ('\n------------------------------\nLISTA DE ESTUDIANTES ARTEMIS ORDENADOS:')
        for i in sputnik: 
            print(f'* {i}')
        
    elif opc == 1.5:
        print ('------------------------------\n')
        nombre = input('Ingrese el nombre del camper: ')
        for i in sputnik:
            if nombre == i:
                print (f'El camper: {i} \n Se encuentra en la lista ')
          

    else:
        print ('------------------------------\n Ingrese una opcion valida' )
        
""" 
2. N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.
Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.
Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros.

"""

atletas = {

}

record = 15.50
premio = 500

a = int(input("Ingrese la cantidad de participantes: "))

for i in range(a):
    nombreAtleta = input("Nombre del atleta : ")
    salto = float(input("Cuantos metros salto : "))
    atletas[nombreAtleta] = salto
    
mayor =  max(atletas, key=atletas.get)
print(f'-------------------------------------- ')
if atletas[mayor] > record:
    
    print(f"\nEl atleta ganador es: {mayor} con un salto de {atletas[mayor]} metros {premio} millones")
else:
    print(f"\nEl atleta ganador es: {mayor} no supero el record")

    """ 3. En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos. """



def calcular(basico, kilometros, kilomentrosL):

    sueldo = (basico * (kilometros-kilomentrosL)) + (kilomentrosL*(basico+(basico*0.25)))
    
    if kilometros >= 3277:
        print(f'-------------------------------------- ')
        print(f'\n El ciclista gano la vuelta a espana y es merecedor de 700 millones !!!!!')
        print(f'\nSu salario fue un total de:{sueldo} con un total de {kilometros} recorridos y {kilomentrosL} recorridos como lider ')
        print(f' {basico}----> Salario basico ')
    else:
        print(f'-------------------------------------- ')
        print(f'\n El ciclista no gano la vuelta a espana')
        print(f'\nSu salario fue un total de:{sueldo} con un total de {kilometros} recorridos y {kilomentrosL} recorridos como lider ')
        print(f' {basico}----> Salario basico ')

print('\n>>>>> Vuelta a Espana 3.277 KM <<<<<<')

basico = float(input('Ingrese el sueldo basico por kilomentro recorrido: '))
kilometros = float (input('Ingrese los kilometros recorridos totales: '))
kilometrosLider = float(input('Kilometros recorridos como lider '))

calcular(basico, kilometros, kilometrosLider)

