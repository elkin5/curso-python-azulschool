from src.examples import test
from src.examples import ultima_modificacion as um
from src.examples import Operaciones as op

test.printMess()

print(um.ultima_modificacion("2019-11-14"))
print(op.sum(1,2,3))

ingreso = input("Ingrese datos separados por comas: ")
valores = [float(n) for n in ingreso.split(",")]

print(op.sum(*valores))
print(op.res(*valores))
print(op.mul(*valores))
print(op.div(*valores))