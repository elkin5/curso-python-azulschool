def sum(*args):
    sum = 0
    for a in args:
        sum += a
    return sum

def mul(*args):
    mul = 1
    for a in args:
        mul *= a
    return mul

def res(*args):
    res = 0
    for a in args:
        res -= a
    return res

def div(*args):
    div = 1
    for a in args:
        div /= a
    return div

if __name__ == '__main__':
    print(sum(1,2,3))