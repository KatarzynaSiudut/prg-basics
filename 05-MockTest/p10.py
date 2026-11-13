def f(sentence):
  suma_ascii = sum(ord(x) for x in sentence)
  return suma_ascii % 3 == 0