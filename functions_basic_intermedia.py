#1. Actualizar valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 

# Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
def cambiar_valor(list):
    for sublist in list:
        if 10 in sublist:
            index = sublist.index(10)
            sublist[index] = 15

cambiar_valor(x)
print(x)

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
    ]

# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
def cambiar_apellido(estudiantes,nuevo_apellido ):
    estudiantes[0]["last_name"] = nuevo_apellido

cambiar_apellido(estudiantes, "Bryant")
print(estudiantes)


directorio_deportes = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
    }

#En el directorio_deportes, cambia "Messi" por "Andrés". 

def cambiar_jugador(directorio, deporte, jugador_actual, nuevo_jugador):
    if deporte in directorio:
        lista_jugadores = directorio[deporte]
        if jugador_actual in lista_jugadores:
            index = lista_jugadores.index(jugador_actual)
            lista_jugadores[index] = nuevo_jugador

cambiar_jugador(directorio_deportes, "fútbol", "Messi", "Andrés")
print(directorio_deportes)

z = [ {'x': 10, 'y': 20} ]
# Cambia el valor 20 en z a 30.
def cambiar_valorz(list, directorio, nuevonumero):
   for elemento in list:
        elemento["y"] = nuevonumero
cambiar_valorz(z, 'y',30)
print(z)  


#2. Iterar a través de una lista de diccionarios: Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:

def iterateDictionary(some_list):
   for dictionary  in some_list:
        dicsalida = ""
        for key , value in dictionary.items():
            dicsalida += f"{key} - {value}, "
        print(dicsalida)    

estudiantes = [
         {'first_name':  'Michael', 'last_name': 'Jordan'},
         {'first_name': 'John', 'last_name': 'Rosales'},
         {'first_name': 'Mark', 'last_name': 'Guillen'},
         {'first_name': 'KB', 'last_name': 'Tonel'}
    ]

iterateDictionary(estudiantes) 


# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 3. Obtener valores de una lista de diccionarios Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

def iterateDictionary2(key_name, some_list):
    for dictionary  in some_list:
       for key , value in dictionary.items():
            if key == key_name :
                 print(value )  


iterateDictionary2("first_name", estudiantes) 
iterateDictionary2("last_name", estudiantes) 

# 4. Iterar a través de un diccionarios con valores de lista Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    
       for key , value in some_dict.items():
           print(len(value),key.upper() )   
           for list in value:
               print(list)
  
printInfo(dojo)

