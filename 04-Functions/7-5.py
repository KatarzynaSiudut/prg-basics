def number_in_range(number, x, y):
    return x <= number <= y


number = 5
x, y = 2,15

if number_in_range(number, x, y):
    result = "yes"
else:
    result = "no"

print(f"Number {number} in the range <{x},{y}>: {result}")







