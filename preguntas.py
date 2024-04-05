"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
input_file = 'data.csv'

# Función para leer el archivo CSV y convertirlo en una matriz
def csv_matriz(archivo_csv):
    matriz = []
    with open(input_file, newline='') as csvfile:
        for linea in csvfile:
            fila = linea.strip().replace('\t', ' ').split(' ')  # Dividir la línea en elementos por el espacio
            matriz.append(fila)
    return matriz

def pregunta_01(sequence):
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sum = 0
    for i in sequence:
        sum += int(i[1])
    return sum



def pregunta_02(sequence):
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    new_sequence = []
    for i in sequence:
        new_sequence.append((i[0], 1))

    new_sequence = sorted(new_sequence, key=lambda x: x[0])#ordena alfabeticamente
    
    dic={}
    for key, value in new_sequence:
        if key not in dic.keys():
            dic[key] = []
        dic[key].append(value)
    
    new_sequence = []  
    for key, value in dic.items():
        tupla = (key, sum(value))
        new_sequence.append(tupla)
        
    return new_sequence



def pregunta_03(sequence):
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    new_sequence = []
    for i in sequence:
        new_sequence.append((i[0], int(i[1])))
    new_sequence = sorted(new_sequence, key=lambda x: x[0])#ordena alfabeticamente
    
    dic={}
    for key, value in new_sequence:
        if key not in dic.keys():
            dic[key] = []
        dic[key].append(value)
    
    new_sequence = []  
    for key, value in dic.items():
        tupla = (key, sum(value))
        new_sequence.append(tupla)
    return new_sequence


def pregunta_04(sequence):
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    new_sequence = []
    for i in sequence:
        i[2] = i[2].split("-")
        new_sequence.append((i[2][1],1))
    new_sequence = sorted(new_sequence, key=lambda x: x[0])#ordena 

    dic={}
    for key, value in new_sequence:
        if key not in dic.keys():
            dic[key] = []
        dic[key].append(value)
    
    new_sequence = []  
    for key, value in dic.items():
        tupla = (key, sum(value))
        new_sequence.append(tupla)
    return new_sequence



def pregunta_05(sequence):
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    new_sequence = []
    for i in sequence:
        new_sequence.append((i[0],int(i[1])))
    new_sequence = sorted(new_sequence, key=lambda x: x[0])#ordena alfabeticamente

    dic={}
    for key, value in new_sequence:
        if key not in dic.keys():
            dic[key] = []
        dic[key].append(value)
        
    new_sequence = []  
    for key, value in dic.items():
        tupla = (key, max(value), min (value))
        new_sequence.append(tupla)
    return new_sequence


def pregunta_06(sequence):
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    new_sequence = []
    for i in sequence:
        i[4] = i[4].split(",")
        for j in range(len(i[4])):
            new_sequence.append((i[4][j].split(":")))
            new_sequence[-1][-1]=int(new_sequence[-1][-1])
    new_sequence = sorted(new_sequence, key=lambda x: x[0])#ordena 
    
    dic={}
    for key, value in new_sequence:
        if key not in dic.keys():
            dic[key] = []
        dic[key].append(value)
    

    new_sequence = []  
    for key, value in dic.items():
        tupla = (key, min(value), max(value))
        new_sequence.append(tupla)
    return new_sequence


def pregunta_07(sequence):
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    new_sequence = []
    for i in sequence:
        new_sequence.append((int(i[1]), i[0]))
    new_sequence = sorted(new_sequence, key=lambda x: x[0])#ordena alfabeticamente
    

    dic={}
    for key, value in new_sequence:
        if key not in dic.keys():
            dic[key] = []
        dic[key].append(value)
    new_sequence = []  
    for key, value in dic.items():
        tupla = (key, (value))
        new_sequence.append(tupla)
    return new_sequence


def pregunta_08(sequence):
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    new_sequence = []
    for i in sequence:
        new_sequence.append((int(i[1]), i[0]))
    new_sequence = sorted(new_sequence, key=lambda x: x[0])#ordena alfabeticamente
    
    dic={}
    for key, value in new_sequence:
        if key not in dic.keys():
            dic[key] = []
        if value not in dic[key]:
            dic[key].append(value)
    new_sequence = [] 
    
    for key, value in dic.items():
        tupla = (key, sorted(value))
        new_sequence.append(tupla)
    return new_sequence


def pregunta_09(sequence):
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    new_sequence = []
    for i in sequence:
        i[4] = i[4].split(",")
        for j in range(len(i[4])):
            new_sequence.append((i[4][j].split(":")))
            new_sequence[-1][-1] = 1
    new_sequence = sorted(new_sequence, key=lambda x: x[0])#ordena 
    

    new_sequence = sorted(new_sequence, key=lambda x: x[0])#ordena alfabeticamente
    
    dic={}
    for key, value in new_sequence:
        if key not in dic.keys():
            dic[key] = 0
        dic[key] += value
    new_sequence = []   
    return dic

def pregunta_10(sequence):
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    new_sequence = []
    for i in sequence:
        i[3] = i[3].split(",")
        i[4] = i[4].split(",")
        new_sequence.append(( i[0], len(i[3]),len(i[4])))
    return new_sequence

def pregunta_11(sequence):
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    new_sequence = []
    for i in sequence:
        i[3] = i[3].split(",")
        for j in i[3]:
            new_sequence.append((j, int(i[1]) ))
    new_sequence = sorted(new_sequence, key=lambda x: x[0])

    dic={}
    for key, value in new_sequence:
        if key not in dic.keys():
            dic[key] = 0
        dic[key] += value
    new_sequence = []   
    return dic
    

def pregunta_12(sequence):
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    new_sequence = []
    for i in sequence:
        i[4] = i[4].split(",")
        for k in i[4]:
            k = k.split(":")
            new_sequence.append((i[0], int(k[-1]))) #para tener solo los números y unirlos con la columna 1
    new_sequence = sorted(new_sequence, key=lambda x: x[0])
    dic={}
    for key, value in new_sequence:
        if key not in dic.keys():
            dic[key] = 0
        dic[key] += value
    new_sequence = []   
    return dic
sequence=csv_matriz(input_file)
pregunta12 = pregunta_12(sequence)
print(pregunta12)
