price = float(input('eneter the price: '))
discount = float(input('enter discount %: '))
reduction = price * discount/100
price_with_discount = price - reduction
print(f'price with discount {price_with_discount:.2f}')
print(f'reduction {reduction:.2f}')