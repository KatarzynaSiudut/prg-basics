
def f(name):
  slowa = name.split()
  akronim = ''
  for slowo in slowa:
    akronim += slowo[0]
  return akronim

print(f("Internet of Things"))

def f(name):
  slowa = name.split() #dzieli podany tekst na pojedyncze słowa, rozdzielając je spacjami.
  akronim = '' #Tworzy pusty ciąg znaków (''), do którego będziemy powoli dopisywać kolejne litery, tworząc wynikowy akronim.
  for slowo in slowa: #Uruchamia pętlę, która przechodzi po kolei przez każde słowo z listy slowa
    akronim += slowo[0] #slowo[0] pobiera pierwszą literę aktualnego słowa (indeks 0 to pierwszy znak).
  return akronim
