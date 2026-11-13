def f(binary_number):
    return all(x in "01" for x in binary_number)


test1 = "1101111"
test2 = "1311a10100"

print(f'f("{test1}") returns {f(test1)}')
print(f'f("{test2}") returns {f(test2)}')

























