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
        
