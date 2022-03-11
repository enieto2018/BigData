#reduccion.py
#cat result-diabetes.csv | python mapeo.py | python reduccion.py

import sys

salida = {}

#Recoore cada linea enviada del mapeo
for line in sys.stdin:
    # Quitar espacios
    line = line.strip()
    #Departamento, municipio
    cod, valor = line.split('\t')

    # El departamento esta en el mapa (salida)?
    if cod in salida:
        #Si el departamento esta en el mapa busque el municipio en el mapa (valor) del departamento
            #Municipio esta en el mapa de municipios del departamento?
        if valor in salida[cod]:
            # Si el municipio esta acumule el valor del municipio (key)
            salida[cod][valor] = salida[cod][valor] + 1
        else:
            # Si el municipio no esta, agregue el municipio (key) con valor 1
            salida[cod][valor] = 1
    # Si el departamento no esta en el mapa (salida)
    else:
        # Agregue el departamento al mapa, y como valor agregue un diccionario con el municipio
            #Ejemplo:
            # Cod = "Risaralda"
            # valor = "Pereira"
            # Salida = {"Risaralda" :  {"Pereira": 1} }
        salida[cod] = {valor: 1}

# print (salida)

# Recorre todo el mapa de salida (Departamentos con municipios y PQRS por cada municipio)
for cod in salida.keys():
    # Variable para acumular las PQRS por municipio
    canPqrsXMun = 0
    # Recorro los municipios para el departamento (cod)
    for mun in salida[cod]:
        # Acumulo las PQRS de todos los municipios
        canPqrsXMun += salida[cod][mun]
    #Cuando termina de recorrer los municios, calculo la cantidad de municipios, obteniendo el largo
    #del dicionario de municipios
    numMunicipios = len(salida[cod])
    #Calculo promedio por departamento
    promedioDepartamento = canPqrsXMun/numMunicipios
    #Imprimo informacion al usuario
    print(f'{cod} : {promedioDepartamento} ')
