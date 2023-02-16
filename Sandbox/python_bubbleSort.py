cadena = 'Miguel trainer'
lengthCadena= len(cadena)
print (lengthCadena)
arrayCadena=[]  
for i in range(lengthCadena):
    print (range(lengthCadena))
    arrayCadena.append(cadena[i:i+1])
        
""" for i in range(n-1):
    print(i)
    for j in range(n-1-i):
        if listaAleatoria[j] < listaAleatoria[j+1]:
                listaAleatoria[j], listaAleatoria[j+1] = listaAleatoria[j+1], listaAleatoria[j] """

  
print(arrayCadena)   

for i in range(lengthCadena-1):
    print(i)
    for j in range(lengthCadena-1-i):
        arrayCadena[j], arrayCadena[j+1]= arrayCadena[j+1], arrayCadena[j]
print(arrayCadena)    