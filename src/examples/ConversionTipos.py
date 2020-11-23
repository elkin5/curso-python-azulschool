class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if base < 0:
            raise ValueError("La base no puede ser un número negativo")
        self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if altura < 0:
            raise ValueError("La altura no puede ser un número negativo")
        self._altura = altura

    @property
    def area(self):
        return self.base * self.altura / 2

    #Utilizo esto para imprimir en string
    def __str__(self):
        return f'{type(self).__name__} de base {self.base} y altura {self.altura}.'

    #Utilizo esto para crear un objeto que al evaluarlo de la representacion de la creacion del objeto
    def __repr__(self):
        clase = type(self).__name__

        # retorna Triangulo(base, altura)
        return f'{clase}({self.base}, {self.altura})'

if __name__ == '__main__':
    t = Triangulo(4, 5)
    print("Área:", t.area)

    print("Es", t)

    print(repr(t))
    print(eval(repr(t)))

#Las namedtuple sirven para usar todos los metodos de una tupla en ena clase
from collections import namedtuple
from math import sqrt

_Punto = namedtuple("_Punto", "x,y,z")

class Punto(_Punto):

    def distancia(self, otro):
        """ Distancia entre dos puntos """

        dif_x = (self.x - otro.x) ** 2
        dif_y = (self.y - otro.y) ** 2
        dif_z = (self.z - otro.z) ** 2

        return sqrt(dif_x + dif_y + dif_z)


if __name__ == '__main__':
    p = Punto(5, 4, 7)

    print("p:", p)
    print("distancia:", p.distancia(Punto(8, 4, 9)))