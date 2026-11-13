
def f(number, even):
    suma = 0
    for x in str(number):
        cyfra = int(x)
        if (cyfra % 2 == 0) == even:
            suma += cyfra
    return suma

print(f"f(3124, True) returns {f(3124, True)}")
print(f"f(3124, False) returns {f(3124, False)}")
print(f"f(20576, False) returns {f(20576, False)}")
print(f"f(20576, True) returns {f(20576, True)}")
print(f"f(13115, True) returns {f(13115, True)}")






    


