file = open("lorem.txt")
print(file.tell())  # Ubicacion del puntero de lectura
print(type(file))
print(file.read(2))
print(file.readlines(1))
# print(file.tell()) Cuando uso readlinea no puedo usar tell()
file.close()  # Fichero que se abre se cierra

# abrimos y guardamos en variable file No es necesario cerrar
with open("lorem.txt") as file:
    # imprimimos el contenido en caso de ser posible
    print(file.read() if file.readable() else "No se puede leer.")

print("***************")
with open("lorem.txt") as file:
    # imprimimos hasta encontrar un salto de línea
    print(file.readline())

with open("lorem.txt") as file:
    # guardamos e imprimimos hasta encontrar un salto de línea
    lineas = file.readlines(1)
    print(type(lineas), "| Elementos:", len(lineas))
    print("Var lineas:", lineas)

    # [print(line) for line in file.readlines()]

import webbrowser

fileName = "pagina_python.html"
lineas = [
    '<!DOCTYPE html>\n',
    '<html lang="es">\n',
    '\t<head>\n',
    '\t\t<meta charset="utf-8">\n',
    '\t\t<title>Python Web</title>\n',
    '\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n',
    '\t</head>\n',
    '\t<body>\n',
    '\t\t<p>Esto es una página web creada en Python!!</p>\n',
    '\t</body>\n',
    '</html>\n',
]

with open(fileName, mode="w", encoding="utf-8") as file:
    file.writelines(lineas)

# Crear archivo json
import json

data = {
    "personas": [
        {
            "nombre": "Lucas",
            "apellido": "Lucyk",
            "pais": "Argentina"
        },
        {
            "nombre": "Juan",
            "apellido": "Perez",
            "pais": "México"
        },
        {
            "nombre": "Ana",
            "apellido": "Gonzalez",
            "pais": "Uruguay"
        },
    ]
}

with open('datos.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# Leer archivo Json
with open('datos.json', encoding="utf-8") as file:
    data = json.load(file)

    print(type(data))

    for persona in data["personas"]:
        [print(k, v) for k, v in persona.items()]

# Un diccionario python tiene la estructura de un objeto json
