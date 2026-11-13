def f(product_code):
  kod = int(product_code)
  c4 = kod % 10
  c3 = (kod // 10) % 10
  c2 = (kod // 100) % 10
  c1 = kod // 1000
  return (c1 + c2 + c3) % 7 == c4
