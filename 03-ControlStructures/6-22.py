number = 1
while number <= 30:
    if number % 3 == 0 and number % 5 == 0:
        print("BINGO", end=" ")
    elif number % 3 == 0:
        print("THREE", end=" ")
    elif number % 5 == 0:
        print("FIVE", end=" ")

    else:
        print(number, end = " ")

    number = number + 1
