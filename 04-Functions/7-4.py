def count_letter(text, letter):
  return text.count(letter)

def count_letter(text, letter):
    count = 0
    for x in text:
        if x == letter:
            count += 1
    return count

text = "You never get a second chance to make a first impression"
letter = "e"

# Obliczenie liczby wystąpień za pomocą funkcji z modułu
result = count_letter(text, letter)

# Wyświetlenie wyniku zgodnie z przykładem
print(text)
print(f"The number of letter '{letter}': {result}")











    