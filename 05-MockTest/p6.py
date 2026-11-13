def f(number, even):
    suma = 0
    for x in str(number):
        cyfra = int(x)
        if (cyfra % 2 == 0) == even:
            suma += cyfra
    return suma