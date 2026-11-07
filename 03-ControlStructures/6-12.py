number_of_products = int(input("enter the number of products: "))
product_price = 40

if number_of_products > 2:
    amount_to_pay = 2 * product_price + (number_of_products - 2) * product_price * 0.75
else:
    amount_to_pay = number_of_products * product_price


print(f'product price: {product_price}')
print(f'amount to pay: {amount_to_pay:.2f}')