def suma(*args):
    num = 0
    for arg in args:
        num += arg
    return num

def producto(*args):
    num = 1
    for arg in args:
        num *= arg
    return num

OPERACIONES = {
    "suma": suma,
    "producto": producto,
}

def operacion(*args, **kwargs):
    return OPERACIONES.get(kwargs.get("operacion"))(*args)

print(operacion(2, 3, 4, operacion="suma"))
print(operacion(2, 3, 4, operacion="producto"))

def matriz(numa=1, numb=1):
    for n in range(numb):
        print("X" * numa)

matriz(4, 3)

def paresImpares(lista):
    num_impares = [n for n in lista if n%2]
    num_pares = [n for n in lista if n%2 == 0]
    return [num_impares, num_pares]
        
print(paresImpares([1,2,3,4,5,6,7,8]))
