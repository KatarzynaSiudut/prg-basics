def f(amount_to_pay):
  monety_5 = amount_to_pay // 5
  reszta = amount_to_pay % 5
  monety_2 = reszta // 2
  monety_1 = reszta % 2
  return monety_5 + monety_2 + monety_1


