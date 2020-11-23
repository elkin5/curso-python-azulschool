'''1.- Dada la cadena “El veloz murciélago hindú comía feliz cardillo y kiwi”, imprimir su variante justificada a la derecha rellenando con ‘>’, a la izquierda rellenando con ‘<‘ y centrada en 60 caracteres con asteriscos utilizando métodos de cadenas.'''

string = "El veloz murciélago hindú comía feliz cardillo y kiwi";
print(string.ljust(100, '>'));
print(string.rjust(60, '<'));
print(string.center(60, '*'));

# 5. Utilizando métodos de cadenas, crear una variable con una lista de números pares del 2 al 10 como cadenas e imprimir sus valores separados por un guión medio.

pares = ['2','4','6','8','10']
print('-'.join(pares))