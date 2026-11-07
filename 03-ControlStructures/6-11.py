current_product_price = float(input("enter current product price: "))
previous_product_price = float(input("enter previous product price: "))
procent = (previous_product_price - current_product_price) / previous_product_price * 100

if procent >= 10:
    print("Buy the product!!!")

print(f'product price reduced by {procent} %')