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
        


