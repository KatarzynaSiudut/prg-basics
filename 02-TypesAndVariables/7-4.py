import math

circumference = float(input('Enter tree circumference in cm: '))
diameter = circumference / math.pi
can_be_cut_down = diameter >= 50
print(f'Tree can be cut down: {can_be_cut_down}')
