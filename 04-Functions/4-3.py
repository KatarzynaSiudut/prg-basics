###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s = (a+b+c)/2
    result = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return result

a =float(input("a = "))
b = float(input("b ="))
c = float(input("c = "))

print(f"The area of a triangle with sides {a}, {b}, {c} is {triangle_area(a, b, c)}")


print('The area of ​​a triangle with sides 3,4,5 is {triangle_area(a,b,c)}')
print('The area of ​​a triangle with sides ... is ...')
print('The area of ​​a triangle with sides ... is ...')