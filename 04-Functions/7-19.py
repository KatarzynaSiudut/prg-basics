def f(number):
    x = str(number)
    return sum(int(y) for y in x if x.count(y) > 1)

print(f(12032332))
print(f(35827))





