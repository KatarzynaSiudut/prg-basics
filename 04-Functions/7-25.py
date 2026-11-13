def f(x, y):
  wynik = 0
  for n in range(x, y + 1):
    if n % 6 == 0 and n % 4 != 0:
      wynik += n
  return wynik