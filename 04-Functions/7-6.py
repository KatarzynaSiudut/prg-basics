def hide(card_number):
  return card_number[:2] + "*" * (len(card_number) - 6) + card_number[-4:]

card_number = "5290312400019022"

masked_number = hide(card_number)

print(f'f("{card_number}") returns "{masked_number}"')









