###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
import math
a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
volume = a*b*c
surface = 2*a*b + 2*a*c + 2*b*c
print(f'the volume is {volume}')
print(f'the surface is {surface}')