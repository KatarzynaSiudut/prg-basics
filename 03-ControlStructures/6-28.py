a = 0
b = 1
counter = 0

while counter < 20:
    print(a, end=" ")

    next_number = a + b
    a = b
    b = next_number

    counter = counter + 1