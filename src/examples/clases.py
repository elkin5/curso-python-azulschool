class Car:
    _parametroPrivado = "Privado"
    __parametroOculto = "Oculto"
    ruedas = 4 # Atributos de la clase; comunes para todos las instancias de la clase

    def __init__(self, color, marca): #Constructor
        self.color = color # Atributos del objeto; solo para la instancia creada
        self.marca = marca

    print(__parametroOculto)

car1 = Car("Blanco", "Mazda")
car2 = Car("Rojo", "Ferrari")

print(Car._parametroPrivado)

print(car1.color)
print(car2.color)

print(Car.ruedas)
print(Car.mro)
#Se puede acceder a un atributo oculto de la siguiente manera
print(Car._Car__parametroOculto)

# El atributo self permite:
print("El Atributo Self")
from math import sqrt
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, otroPunto):
        deltaX = self.x - otroPunto.x
        deltaY = self.y - otroPunto.y

        return sqrt(deltaX ** 2 + deltaY ** 2)

# 1. Acceder al metodo de 2 maneras
p1 = Punto(1,2)
p2 = Punto(3,4)

# 1.1 Llamando el metodo como prodiedad de un objeto
print(p1.distance(p2))

# 1.2 Llamando al metodo directamente desde la clase
print(Punto.distance(p1, p2))

# 2. Crear metodos y adicionarlos directamente a la clase
def pintarPuntos(self):
    print("(" + str(self.x) + "," + str(self.y) + ")")

Punto.pintar = pintarPuntos

p1.pintar()
Punto.pintar(p2)

#HERENCIA
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def hablar(self, mensaje):
             print(mensaje)

class Profesor(Persona):
    pass #No ejecutar nada

class Estudiante(Persona):
    pass

perso = Persona("persona", "Uno")
profe = Profesor("Profesor ", "Dos")
perso.hablar("Hola gente!")
profe.hablar("Hola alumnos!")
est = Estudiante("Estud", "Tres")
print(est.nombre)

# Redefinir datos: Agregar nuevo atributo a la clase nueva
class Circulo(Punto):
    def __init__(self, x, y, radio):
        super().__init__(x, y)
        self.radio = radio

c = Circulo(2, 7, 5)

print("x:", c.x)
print("y:", c.y)
print("r:", c.radio)

#Polimorfismo: Un mismo metodo diferente comportamiento
class Humano:
    def atacar(self):
        print("Puñetazo!")

class Rey(Humano):
    pass

class Mago(Humano):
    def atacar(self):
        print("Hechizo!")

class Guerrero(Humano):
    def atacar(self):
        print("Espada!")

if __name__ == '__main__':
    humano = Humano()
    rey = Rey()
    mago = Mago()

    humano.atacar()
    rey.atacar()
    mago.atacar()

# Herencia Multiple
class Humano:
    def atacar(self):
        print("Puñetazo!")


class Rey(Humano):
    pass


class Mago(Humano):
    def atacar(self):
        print("Hechizo!")


class Guerrero(Humano):
    def atacar(self):
        print("Espada!")


class Brujo(Mago, Guerrero):
    pass


if __name__ == '__main__':
    brujo = Brujo()
    brujo.atacar()

#Para saber el orden de resolucion de metodos se usa (method resolution order)
print(Brujo.__mro__)
# Primero busca en la clase si no encuentra entonces en la primera herencia, luego
# segunda herencia luego en la herencia de mago etc..

#MONKEY PATHCHING: Modificar el comportamiento de un metodo fuera de su definicion
#Como crear y agregar un nuevo methodo a la clase pero con el mismo nombre que se ha puesto
#en la definicion de la clase

#DUCK TYPING
#No necesitamos saber que un objeto en una instancia de un objeto si posee el comportamiento
# de dicho objeto entonces lo sera

class Vivienda:
    def abrir_puerta(self):
        print("Abriendo puerta.")


class Persona:
    def ingresar_vivienda(self, vivienda): # No necesito saber que vivienda es de un tipo especifico
        vivienda.abrir_puerta()
        # Asumimos que una vivienda debe poseer el método abrir_puerta

departamento = Vivienda()
perso = Persona()
perso.ingresar_vivienda(departamento)

#@PROPERTY
# Se desea validar que la base y la altura no sean valores negativos
# Una forma de validar seria
class Triangulo1:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    def set_base(self, base):
        if base < 0:
            raise ValueError("La base no puede ser un número negativo")
        self._base = base

    def set_altura(self, altura):
        if altura < 0:
            raise ValueError("La altura no puede ser un número negativo")
        self._altura = altura


t = Triangulo1(-4, 3)
#t.set_base(-4)

#Pero esta opcion solamente valida al setearlo no al crear el objeto por lo que
# deberiamos crear un nuevo validador

# La forma optima de hacerlo es usando @property que permite acceder un metodo como si
# fuese un atributo

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property #Etiqueta usada
    def base(self): # debe tener el mismo nombre del atributo
        return self._base

    @base.setter
    def base(self, base):
        if base < 0:
            raise ValueError("La base no puede ser un número negativo")
        self._base = base


t = Triangulo(4, 5)
print(t.base)

#DELETTERS
class Usuario:
    def __init__(self, password):
        self._passwords = []
        self.password = password

    @property
    def password(self):
        return None if not len(self._passwords) else self._passwords[-1]

    @password.setter
    def password(self, password):
        if len(password) < 8:
            raise ValueError("El password debe tener 8 dígitos como mínimo")
        self._passwords.append(password)

    @password.deleter
    def password(self):
        self._passwords = []


if __name__ == '__main__':
    user = Usuario("ClaveNumero1")
    print("Clave actual:", user.password)

    user.password = "SegundaClaveAsignada"
    print("Clave actual:", user.password)

    print("Historial de claves:", user._passwords)

    del user.password
    print("Clave actual:", user.password)
    print("Historial de claves:", user._passwords)
