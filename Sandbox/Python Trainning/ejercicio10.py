""" 10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
- Mes de consumo - Valor kw
-Total kw consumido en el mes - estrato """

""" valor de kw por estrato """

estrato1 = 233.58
estrato2 = 291.98
estrato3 = 496.37
estrato4 = 583.97
estrato5y6 = 700.76 


def calcularTotal(estrato,totalKw):
    total = 0 

    if estrato == 1:
        total = totalKw * estrato1
    elif estrato == 2:
        total = totalKw * estrato2
    elif estrato == 3:
        total = totalKw * estrato3
    elif estrato == 4:
        total = totalKw * estrato4
    elif estrato == 5 or estrato == 6:
        total = totalKw * estrato5y6
    
    return total


opc = 0

while opc != 2:

    print('1.Calcular el valor del recibo\n 2.Salir')
    opc = int(input(': '))

    if opc == 1:
    
        estrato = int(input('Ingrese el estrato (numero): '))
        mes = str(input('Mes de consumo: (nombre):'))
        totalKw = float(input('Kw consumidos en el mes: '))

        totalPagar = calcularTotal(estrato,totalKw)
        print(f'\nMes: {mes}\nKw consumidos en el mes: {totalKw}\nEl valor Total a pagar es de : ${totalPagar}\n')

    elif opc != 1 and opc !=2:
        print('INGRESE UNA OPCION VALIDA')
