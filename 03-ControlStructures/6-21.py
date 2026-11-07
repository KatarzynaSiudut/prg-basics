amount = int(input("enter the amount: "))

print(f'the amount in PLN: {amount}')

coins_5 = amount // 5
amount = amount % 5

coins_2 = amount // 2
amount = amount % 2

coins_1 = amount // 1

print("5 PLN coins:", coins_5)
print("2 PLN coins:", coins_2)
print("1 PLN coins:", coins_1)
