def f(sentence):
  samogloski = 'aeiouy'
  return sum(1 for x in sentence if x in samogloski)