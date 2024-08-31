#Inciso a)
Datos= {'ALUMNOS': []}

def agragarAlum(datos, nombre,apellido,dni,fecha_nacimiento,tutor,notas,faltas,amonestaciones):
    diccAlum= {
        'Nombre':nombre,
        'Apellido':apellido,
        'DNI':dni,
        'Fecha de nacimiento':fecha_nacimiento,
        'Tutor':tutor,
        'Notas': notas,
        'Faltas': faltas,
        'Amonestaciones':amonestaciones

    }

    datos['ALUMNOS'].append(diccAlum)

def mostrarAlum(datos):
    for i in datos['ALUMNOS']:
        print(f"Nombre: {i['Nombre']}")
        print(f"Apellido: {i['Apellido']}")
        print(f"DNI: {i['DNI']}")
        print(f"Fecha de nacimiento: {i['Fecha de nacimiento']}")
        print(f"Tutor: {i['Tutor']}")
        print(f"Notas: {i['Notas']}")
        print(f"Faltas: {i['Faltas']}")
        print(f"Amonestaciones: {i['Amonestaciones']}")
        print("------------------")      

def modificarAlum(datos, dni, nombre=None, apellido=None, fecha_nacimiento=None, tutor=None, notas=None, faltas=None, amonestaciones=None):
    for i in datos['ALUMNOS']:
        if i['DNI']== dni:
            if nombre is not None: 
                i['Nombre'] = nombre
            if apellido is not None:  
                i['Apellido'] = apellido
            if fecha_nacimiento is not None: 
                i['Fecha de nacimiento'] = fecha_nacimiento
            if tutor is not None:  
                i['Tutor'] = tutor
            if notas is not None:  
                i['Notas'] = notas
            if faltas is not None:  
                i['Faltas'] = faltas
            if amonestaciones is not None: 
                i['Amonestaciones'] = amonestaciones
            return
    print(f'No se encontró el alumno con DNI {dni}')

def expulsarAlum(datos, dni):
    for i in range(len(datos['ALUMNOS'])):#Obtengo todo del diccionario
        if datos['ALUMNOS'][i]['DNI'] == dni:
            del datos['ALUMNOS'][i] #Eliminando al alumno usando indice
            return
    print(f"No se encontró el alumno con DNI {dni}.")


#----------------------------------------------------
#Diccionario a Agregar alumnos
agragarAlum(Datos, "Juan", "Pérez", "12345678", "2005-06-15", "Ana Pérez", [8, 9, 10], 3, 1)
agragarAlum(Datos, "María", "Gómez", "87654321", "2006-07-20", "Luis Gómez", [7, 6, 8], 1, 0)

#   Muestra todo lo que hay en la base de datos del Diccionario
print()
print('         ALUMNOS')
mostrarAlum(Datos)

#------------------------------------------------------------------

# Modificar un alumno (ejemplo: cambiar el nombre y las notas de Juan)
modificarAlum(Datos, "12345678",
               nombre="Juan Carlos", notas=[9, 9, 10])

# Muestra los datos despues de modificar
print('         DESPUES DE MODIFICAR:')
mostrarAlum(Datos)

#------------------------------------------------------------------

# Expulsar un alumno (ejemplo: expulsar a María)
expulsarAlum(Datos, "87654321")#dni de María

# Muestra los datos despues de expulsar
print('         DESPUES DE EXPULSAR')
mostrarAlum(Datos)


