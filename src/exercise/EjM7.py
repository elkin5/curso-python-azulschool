"""
1.- Importe namedtuple y utilizando la misma, cree una clase Pizza con los atributos tamanyo, precio e ingredientes. Luego, cree una lista vacía pizzas.

2.- Dada la lista “pedidos”, agruéguela al código, recorra la misma, cree instancias de la clase Pizza y agregue las mismas a la lista “pizzas”.

3.- Utilizando collections.Counter, cree un objeto ranking_ingredientes que contenga todos los ingredientes de las instancias en la lista “pizzas” (incluyendo repetidos). Luego imprima el ingrediente más utilizado con la cantidad de pedidos que incluyeron el mismo.
** La impresión debe devolver [(‘Queso’, 6)]

4.- Utilizando collections.defaultdict, cree un objeto con el tipo int por defecto. Luego, actualice el objeto con los valores de la variable ranking_ingredientes del paso anterior. Para finalizar, imprima el valor de las claves “Pepperoni” y “Pepinillos”; deben devolver 3 y 0 respectivamente.

5.- Obtenga e imprima en pantalla el precio mínimo y máximo de cada tamaño de pizza existente en la lista “pizzas”. Considere utilizar defaultdict.
"""
from collections import namedtuple

Pizza = namedtuple("Pizza", "tamanyo, precio, ingredientes")
pizzas = []
pedidos = ["Mesa 1", "Mesa 2", "Mesa 3"]

for pedido in pedidos:
    pizza = ("grande", 500, ["pina", "peperoni"])
    pizzas.append(pizza)
    print(pedido)


